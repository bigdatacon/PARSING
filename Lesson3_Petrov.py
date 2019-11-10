import requests
from pprint import pprint
import json
from bs4 import BeautifulSoup as bs
import re

##### Сделоно только для HH


headers = {'accept': '*/*','user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}



base_urlp='https://hh.ru/search/vacancy?area=1&text=Python&page='

job = []
def hh_parse(base_urlp, headers):

    m = 0
    for n in range(3):


        session = requests.Session()
        request = session.get(base_urlp + str(m), headers=headers)
        # if request.status_code == 200:
        soup = bs(request.content, 'html.parser')
        divs = soup.find_all('div', attrs={'data-qa': 'vacancy-serp__vacancy'})
        # print(len(divs))
        for div in divs:
            job_data = {}
            title = div.find('a', attrs={'data-qa': 'vacancy-serp__vacancy-title'}).text
            href = div.find('a', attrs={'data-qa': 'vacancy-serp__vacancy-title'})['href']
            company = div.find('a', attrs={'data-qa': 'vacancy-serp__vacancy-employer'}).text
            salary = div.find('div', attrs={'data-qa': 'vacancy-serp__vacancy-compensation'})
            # print(salary.replace(' ', ''))
            if not salary:
                salary_min = 0
                salary_max = 0
            elif 'от' in salary.getText():

                salary_min = int(re.findall("\d+", salary.getText())[0].replace('\xa0',''))


                salary_max = 0
                salary = salary.getText().replace('\xa0', '')
            elif 'до' in salary.getText():
                salary_min = 0
                salary_max = salary.getText().replace('\xa0', '')
                salary = salary.getText().replace('\xa0', '')
            elif '-' in salary.getText():
                salary_min = int(re.findall("^\d*.\d*", salary.getText())[0].replace('\xa0',''))

                salary_max = re.findall("\d+.\d+\w+", salary.getText())[1].replace('\xa0','')
                salary = salary.getText().replace('\xa0', '')

            job_data['job_link'] = href
            job_data['salary_min'] = salary_min
            job_data['salary_max'] = salary_max
            job_data['salary'] = salary

            job.append(job_data)
        m +=1
    return job


spis = hh_parse(base_urlp, headers)


from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client['bd256']
letters = db.letters

parametr = int(input('input salary constraint: '))

for i in spis:
    letters.insert_one(i)
    objects = letters.find({'salary_min':{'$gte':parametr}})
    for obj in objects:
        pprint(obj)
















