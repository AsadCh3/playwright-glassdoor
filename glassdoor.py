import time
import csv
from collections import OrderedDict
import pandas as pd
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
from playwright_stealth import stealth_sync
from concurrent.futures import ThreadPoolExecutor


final_companies = open('finalglassdoorcompanies.csv', 'a', newline='', encoding='utf-8')
writer = csv.DictWriter(final_companies, fieldnames=['conm', 'cusip', 'cik', 'tic', 'gvkey', 'ResultCompanyID', 'ResultCompanyName'])
df_companies = pd.read_csv('glassdoordata.csv', sep='\t')

all_companies = df_companies.iloc[:, 0].to_list()


with sync_playwright() as p:
    browser = p.chromium.launch(headless=True, slow_mo=50)
    context = browser.new_context(
        viewport={ 'width': 1280, 'height': 1024 },
        user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
        java_script_enabled=True
    )

    def newPage(company_dict):
        companyName = company_dict['conm']
        print('new page called:', companyName)
        new_page = context.new_page()
        stealth_sync(new_page)
        new_page.goto(f'https://www.glassdoor.com/Search/results.htm?keyword={companyName}')
        print('---nor')
        soup = BeautifulSoup(new_page.content(), 'html.parser')
        # print(soup)

        first_company = soup.find('a', class_='company-tile')
        print(first_company)

        if first_company:
            CompanyIDString = first_company['data-brandviews']

            # Actual data required
            company_dict['ResultCompanyID'] = CompanyIDString.split('eid=')[-1]
            company_dict['ResultCompanyName'] = first_company.find('h3', class_='d-sm-block').text
            writer.writerow(company_dict)
            new_page.close()

    # for company in df_companies.to_dict(orient="records")[1:]:
    #     company = OrderedDict(company)
    #     newPage(company)

    inputs = [OrderedDict(company) for company in df_companies.to_dict(orient="records")[1:]]
    with ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(newPage, inputs)


# page = browser.new_page()
# page.goto('https://www.glassdoor.com', wait_until='domcontentloaded', timeout=0)
# page.wait_for_timeout(100)
# page.fill('input#inlineUserEmail', 'asad.ali@villaextechnologies.com')
# page.click('button[type=submit]')
# page.fill('input#inlineUserPassword', 'Asadali12612@')
# page.click('button[type=submit]')
# page.is_visible('li[data-test=site-header-companies]')
# page.click('li[data-test=site-header-companies] > a')
