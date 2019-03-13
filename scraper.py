"""

"""
from urllib.request import urlopen
from selenium import webdriver
from bs4 import BeautifulSoup as soup
import json
from multiprocessing.dummy import Pool  
from multiprocessing import cpu_count


def scrap_to_json(url):    
    driver=webdriver.Chrome()
    driver.get(url)
    f = driver.page_source
    page_soup = soup(f, 'html.parser')
    driver.close()
    containers = page_soup.find_all('div', {'class':'jobsearch-SerpJobCard row result clickcard'})
    jobs = []
    for container in containers:
        job_container = container.find('a',{'class':'turnstileLink'})
        job_title = job_container.get('title')
        job_link = "https://www.indeed.co.in"
        link = job_container.get('href')
        job_link = job_link + link
        company_container = container.find('span',{'class':'company'})
        company = company_container.get_text().strip()
        # Exception handling if the job doesn't contain the salary details
        try:
            salary_container = container.find('span',{'class':'salary no-wrap'})
            salary = salary_container.get_text().strip().replace('\u20b9','').replace(',','')
        except:
            salary = "None"
        # Create a dictionary for all the required values
        job_dict = {
            "Job Title":job_title,
            "Company":company,
            "Job Url":job_link,
            "Salary":salary
        }  
        jobs.append(job_dict)
    return jobs

if __name__ == "__main__":
    base_url = "https://www.indeed.co.in/jobs?q=software+developer&l=Bengaluru,+Karnataka&start="
    url_list = []
    for page in range(0,100,10):
        url_list.append(base_url+str(page))
    # Creates a Pool with cpu_count number of threads  
    pool = Pool(cpu_count())  
    results = pool.map(scrap_to_json, url_list)
    pool.close()
    # Dump all the values to json file 
    with open('jobs.json', 'w') as f:
        f.write(json.dumps(results, indent=4))
