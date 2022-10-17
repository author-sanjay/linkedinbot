import os,random,sys,time
from urllib.parse import urlparse
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

# Handle Websites to apply for job

# https://in.indeed.com/
baseUrl="https://in.indeed.com/"
# passwordfile="/home/sanju/PycharmProjects/pythonProject/config.txt"
driverlink="/home/sanju/Downloads/chromedriver"
jobwebsiteemail="lifebadlegi@gmail.com"
jobwebsitepassword="Sanjay@7866"


# go to website
service = Service(executable_path=driverlink)
driver = webdriver.Chrome(service=service)
driver.get(baseUrl)
preferedjobtitle=["Software Developer","React Js Developer","Node Js Developer","Full Stack Developer","Front End Developer","BackEnd Developer"]

preferedjobLocation=""
# click login
login=driver.find_element(by="xpath",value='/html/body/div/div[1]/nav/div/div/div[2]/div[2]/div[3]/a')
driver.execute_script("arguments[0].click();", login)
time.sleep(3)
loginemail=driver.find_element(by="xpath",value='/html/body/div/div[2]/main/div/div/div[2]/div/form/div/span/input')
driver.execute_script("arguments[0].click();", loginemail)
loginemail.send_keys(jobwebsiteemail)
loginemail.submit()



#select signin with password
time.sleep(45)
try:
    loginemail.submit()
except:
    time.sleep(5)
finally:
    time.sleep(5)
    selectpassword=driver.find_element(by="xpath",value='/html/body/div/div[2]/main/div/div/div[2]/div/a')
# print(selectpassword)
    driver.execute_script("arguments[0].click();", selectpassword)
    time.sleep(2)
    enterpassword=driver.find_element(by="xpath",value='/html/body/div/div[2]/main/div/div/div[2]/div/form/div[1]/span/input')
    driver.execute_script("arguments[0].click();", enterpassword)
    enterpassword.send_keys(jobwebsitepassword)
    enterpassword.submit()
    time.sleep(60)
    # login complete

    links = []
    for ele in preferedjobtitle:
        # search job
        jobtitle = driver.find_element(by="xpath", value='//*[@id="text-input-what"]')
        driver.execute_script("arguments[0].click();", jobtitle)
        jobtitle.send_keys(Keys.CONTROL+"a")
        jobtitle.send_keys(Keys.DELETE)
        time.sleep(2)
        jobtitle.send_keys(ele)
        if (len(preferedjobLocation) != 0):
            joblocation = driver.find_element(by="xpath", value='//*[@id="text-input-where"]')
            driver.execute_script("arguments[0].click();", joblocation)
            joblocation.send_keys(Keys.CONTROL+"a")
            jobtitle.send_keys(Keys.DELETE)
            time.sleep(2)
            joblocation.send_keys(preferedjobLocation)
        else:
            print("No job location selected. No worries")
        findjob = driver.find_element(by="xpath", value='//*[@id="jobsearch"]/button')
        driver.execute_script("arguments[0].click();", findjob)

        # traversing to job posts
        jobresults = driver.find_elements(by="xpath", value='//*[@id="mosaic-provider-jobcards"]/ul/li');
        # "/html/body/main/div/div[1]/div/div/div[5]/div[1]/div[5]/div/ul/li[1]/div/div[1]/div/div[1]/div/table[1]/tbody/tr/td/div[1]/h2/a"

        for i in range(1, 19):
            temppath = '//*[@id="mosaic-provider-jobcards"]/ul/li[' + str(
                i) + ']/div/div[1]/div/div[1]/div/table[1]/tbody/tr/td/div[1]/h2/a'
            time.sleep(2)
            try:
                joblink = driver.find_element(by="xpath", value=temppath).get_attribute("href")
                print("added"+joblink)
                links.append(joblink)
            except:
                continue

        print(len(links))

