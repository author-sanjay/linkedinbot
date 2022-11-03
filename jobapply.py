import html
import os,random,time

from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from  selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.keys import Keys

def jobapplylinked(preferedjobtitle,preferedlocation):
    driverlink="/home/sanju/Downloads/chromedriver"
    links=[]
    service=Service(executable_path=driverlink)
    driver=webdriver.Chrome(service=service)

    baseurl="https://www.linkedin.com/"
    website=baseurl+"/uas/login?fromSignIn=true&trk=cold_join_sign_in"
    for a in preferedjobtitle:
        x = a.replace(" ", "%20").lower();
        for b in preferedlocation:
            y = b.replace(" ", "%20").lower();
            driver.get("https://www.linkedin.com/jobs/search/?keywords="+x+"&location="+y);
            time.sleep(5)

            for i in range(1,10):
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(4)

            def getlinks(soup):
                ul=soup.find('ul',{'class':'jobs-search__results-list'} )

                alllinks=ul.findAll('a')

                for all in alllinks:
                    temp=all['href'];
                    temp2=temp.split("/")
                    if(temp2[3]=="jobs"):
                        links.append(all['href'])
    # hrefs=[];
    # for a in alllinks:
    #     hrefs.append(a.findNext('href'))
    # print(hrefs)

            getlinks(BeautifulSoup(driver.page_source))
            for i in links:
                print(i)
