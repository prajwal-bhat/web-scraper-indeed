# web-scraper-indeed


A web scrapper in python using BeautifulSoup and Selenium web scraping framework and scrape top 1000 job posts from indeed using url "https://www.indeed.co.in/jobs?q=&amp;l=Bengaluru%2C+Karnataka" for software developer role in Bangaluru.

### Requirements

* Python 3.6
* Selenium 3.14.0
* BeautifulSoup 4

The script requires the above packages to be installed to run

### Installation for Ubuntu 18.04 and above
Installation of Python3 on Ubuntu 18.04 and above

```sh
$ sudo apt update
$ sudo apt install python3.6
$ sudo apt-get install python3-pip
```
Installation of BeautifulSoup4 on Ubuntu 18.04 and above

```sh
$ pip3 install beautifulsoup4
$ pip3 install -U selenium
```
If Chrome webdriver is not installed .
* Visit https://sites.google.com/a/chromium.org/chromedriver/downloads
* Download the correct webdriver for the installed version of chrome 
* Extract the file with 
* Inside the extracted folder . Open Terminal and run
```sh
$ chmod +x chromedriver
$ sudo mv chromedriver /usr/local/bin/
```

### Running the Scraper
From Terminal where the python code is located.
```sh
$ python3 scraper.py
```
or If any other IDE is used. Run the python script accordingly.