import os,random,sys,time
from urllib.parse import urlparse
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys


def monster():
    preferedjobtitle = ["Software Developer", "React Js Developer", "Node Js Developer", "Full Stack Developer",
                        "Front End Developer", "BackEnd Developer"]
    passwordfile = "/home/sanju/PycharmProjects/pythonProject/config.txt"
    file = open(passwordfile)
    line = file.readlines()
    my_username = line[8]
    my_password = line[9]
    websiteurl="https://www.monsterindia.com/"
    driverlink = "/home/sanju/Downloads/chromedriver"
    service = Service(executable_path=driverlink)
    driver = webdriver.Chrome(service=service)

    driver.get(websiteurl)
    time.sleep(2)
    driver.find_element(by="xpath",value='/html/body/div[3]/header/header/div/div[2]/div/a').click()
    time.sleep(2)
    loginemail=driver.find_element(by="xpath",value='//*[@id="signInName"]')
    driver.execute_script("arguments[0].click();", loginemail)
    loginemail.send_keys(my_username)
    loginpassword=driver.find_element(by="xpath",value='//*[@id="password"]')
    driver.execute_script("arguments[0].click();", loginpassword)
    loginpassword.send_keys(my_password)
    signin=driver.find_element(by="xpath",value='//*[@id="signInbtn"]').click()
    time.sleep(3)

    #heading to job search

    for i in preferedjobtitle:
        navbar=driver.find_element(by="xpath",value='//*[@id="wsnavtoggle"]').click()
        time.sleep(2)
        driver.find_element(by="xpath",value='//*[@id="130"]/label/a').click()

        time.sleep(3)


        search=driver.find_element(by="xpath",value='//*[@id="adv_keyword_autocomplete"]')
        driver.execute_script("arguments[0].click();", search)
        search.send_keys(Keys.CONTROL + "a")
        search.send_keys(Keys.DELETE)
        search.send_keys(i)
        driver.find_element(by="xpath",value='//*[@id="themeDefault"]/div[1]/div[1]/div[2]/div[1]/div/div[2]/div/div/div/div/div/form/div[7]/input').click()
        time.sleep(3)

monster()