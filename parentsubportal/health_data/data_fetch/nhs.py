from bs4 import BeautifulSoup
import requests
import pickle
import time
from health_data.models import HealthCondition, HealthInfo

BASE_URL = 'https://www.nhs.uk'

BASE_PATH = '/conditions/'


def run_fetch_nhs():

    results = nhs_conditions_scraper()

    for cond in results:

        condition = HealthCondition.objects.filter(url=cond['url']).first()

        if condition is None:
            condition = HealthCondition(
                name=cond['name'],
                url=cond['url'])

            condition.save()
        else:
            print(f'Health condition {cond["name"]} already exists')

        for info in cond['info']:
            hi_query = HealthInfo.objects.filter(
                url=cond['info'][info], health_condition_id=condition)

            if len(hi_query) == 0:
                information = HealthInfo(
                    name=info,
                    url=cond['info'][info],
                    health_condition_id=condition)

                information.save()

            else:
                print(f'Health info {info} already exists')

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