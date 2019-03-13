from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import csv

base_url = "https://www.indeed.co.in/jobs?q=software+developer&l=Bengaluru,+Karnataka&start="

for i in range(0, 1000, 10):
    url = base_url+str(i)
    driver=webdriver.Chrome()
    driver.get(url)
    f = driver.page_source
    page_soup = soup(f, 'html.parser')
    driver.close()
    containers = page_soup.find_all('div', {'class':'jobsearch-SerpJobCard row result clickcard'})
    for container in containers:
        job_container = container.find('a',{'class':'turnstileLink'})
        job_title = job_container.get('title')
        job_link = "https://www.indeed.co.in"
        link = job_container.get('href')
        job_link = job_link + link
        try:
            salary_container = container.find('span',{'class':'salary no-wrap'})
            salary = salary_container.get_text().strip()
        except:
            salary:"None"
        print(job_title)
        print(job_link)
        print(salary)
    