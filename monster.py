import os,random,sys,time
from urllib.parse import urlparse
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service



def monster():
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




monster()