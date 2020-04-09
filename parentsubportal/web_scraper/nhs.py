from bs4 import BeautifulSoup
import requests
import time


BASE_URL = 'https://www.nhs.uk/'

BASE_PATH = 'conditions/'


def nhs_conditions_scraper():

    page_response = requests.get(BASE_URL + BASE_PATH)

    page_content = BeautifulSoup(page_response.content, 'html.parser')

    links = page_content.select('a.nhsuk-list-panel__link')

    nhs_conditions = []

    for link in links:

        cond = {}

        cond_url = BASE_URL + link['href']

        cond['name'] = link.text
        cond['url'] = cond_url

        cond_resp = requests.get(cond_url)

        cond_content = BeautifulSoup(cond_resp.content, 'html.parser')

        details = cond_content.select('a.nhsuk-contents-list__link')

        if len(details) > 0:
            for detail in details:
                title = detail.text.lower()
                cond[title] = BASE_URL + detail['href']

        nhs_conditions.append(cond)

    return nhs_conditions


if __name__ == '__main__':
    print('Scraping conditions from NHS...')
    results = nhs_conditions_scraper()
    print(results)
    print('Done')
