from bs4 import BeautifulSoup
from health_data.models import HealthCondition, HealthInfo
import requests
import pickle
import time


BASE_URL = 'https://www.nhs.uk'

BASE_PATH = '/conditions/'


def run_fetch_nhs():

    import pdb
    #results = nhs_conditions_scraper()
    results = pickle.load(open('nhs.pkl', 'rb'))
    #pickle.dump(results, open())
    #pdb.set_trace()
    for cond in results:
        condition = HealthCondition(
            name=cond['name'],
            url=cond['url'])

        condition.save()
        print(condition)
        for info in cond['info']:
            information = HealthInfo(
                name=info,
                url=cond['info'][info],
                health_condition_id=condition)

            information.save()

            print(information)
    print('Done')


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
        cond['info'] = {}
        if len(details) > 0:
            for detail in details:
                title = detail.text.lower()

                cond['info'][title] = BASE_URL + detail['href']

        nhs_conditions.append(cond)

    return nhs_conditions
