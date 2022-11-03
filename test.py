import html
import os,random,time

from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from  selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.keys import Keys

driverlink="/home/sanju/Downloads/chromedriver"

service=Service(executable_path=driverlink)
driver=webdriver.Chrome(service=service)

baseurl="https://www.linkedin.com/"
website=baseurl+"/uas/login?fromSignIn=true&trk=cold_join_sign_in"

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3334677903&f_WT=2&geoId=103644278&location=United%20States&refresh=true")
time.sleep(5)
# div=driver.find_element(by="xpath",value='//*[@id="main-content"]/section[2]')
for i in range(1,10):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(4)

def getlinks(soup):
    ul=soup.find('ul',{'class':'jobs-search__results-list'} )

    alllinks=ul.findAll('a')

    for all in alllinks:
        print(all['href'])
    # hrefs=[];
    # for a in alllinks:
    #     hrefs.append(a.findNext('href'))
    # print(hrefs)

getlinks(BeautifulSoup(driver.page_source))
