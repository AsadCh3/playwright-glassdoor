import time
import csv
from collections import OrderedDict
import pandas as pd
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
from playwright_stealth import stealth_async
import asyncio
from playwright.async_api import async_playwright
from playwright_stealth import stealth_async




final_companies = open('finalglassdoorcompanies.csv', 'a', newline='', encoding='utf-8')
writer = csv.DictWriter(final_companies, fieldnames=['conm', 'cusip', 'cik', 'tic', 'gvkey', 'ResultCompanyID', 'ResultCompanyName'])
df_companies = pd.read_csv('glassdoordata.csv', sep='\t')

all_companies = df_companies.iloc[:, 0].to_list()


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=50)
        context = await browser.new_context(
            viewport={ 'width': 1280, 'height': 1024 },
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
            java_script_enabled=True
        )

        new_page = await context.new_page()

        stealth_async()

        def newPage(company_dict, page):
            companyName = company_dict['conm']
            print('new page called:', companyName)
            new_page = browser.new_page()
            new_page.goto(f'https://www.glassdoor.com/Search/results.htm?keyword={companyName}')
            time.sleep(20)
            new_page.screenshot(path='ss.png')
            print(new_page.content())

            soup = BeautifulSoup(new_page.content(), 'html.parser')
            print(soup)

            # first_company = soup.find('a', class_='company-tile')
            # print(first_company)
            # if first_company:
            #     CompanyIDString = first_company['data-brandviews']

            #     # Actual data required
            #     company_dict['ResultCompanyID'] = CompanyIDString.split('eid=')[-1]
            #     company_dict['ResultCompanyName'] = first_company.find('h3', class_='d-sm-block').text
            #     writer.writerow(company_dict)
            #     print(company_dict['ResultCompanyName'])
            
            #     new_page.close()

        for company_dic in df_companies.to_dict(orient="records")[:1]:
            company_dic = OrderedDict(company_dic)
            print(company_dic)
            newPage(company_dic, new_page)



# page = browser.new_page()
# page.goto('https://www.glassdoor.com', wait_until='domcontentloaded', timeout=0)
# page.wait_for_timeout(100)
# page.fill('input#inlineUserEmail', 'asad.ali@villaextechnologies.com')
# page.click('button[type=submit]')
# page.fill('input#inlineUserPassword', 'Asadali12612@')
# page.click('button[type=submit]')
# page.is_visible('li[data-test=site-header-companies]')
# page.click('li[data-test=site-header-companies] > a')
