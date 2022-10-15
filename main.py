import os,random,sys,time
from urllib.parse import urlparse
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service


file=open("/home/sanju/PycharmProjects/pythonProject/config.txt")

line=file.readlines()

my_username=line[0]
my_password=line[1]


website="https://www.linkedin.com/uas/login?fromSignIn=true&trk=cold_join_sign_in"

service=Service(executable_path='/home/sanju/Downloads/chromedriver')

driver=webdriver.Chrome(service=service)

driver.get(website)


#login to linkedin
elementID=driver.find_element(by="id",value='username')

elementID.send_keys(my_username)

elementID=driver.find_element(by="id",value='password')

elementID.send_keys(my_password)

elementID.submit()




#for posting post
l=driver.find_element(by="xpath",value='/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/div[1]/div/div[1]/button')

driver.execute_script("arguments[0].click();",l)

time.sleep(5)

writer=driver.find_element(by="xpath",value='/html/body/div[3]/div/div/div[2]/div/div/div[1]/div[2]/div/div/div[2]/div/div/div[1]')

driver.execute_script("arguments[0].click();",writer)

writer.send_keys("Hello, I am testing my automation Bot Today here")

time.sleep(5)

post=driver.find_element(by="xpath",value='/html/body/div[3]/div/div/div[2]/div/div/div[2]/div[2]/div[3]/button')

driver.execute_script("arguments[0].click();",post)
# elementID.submit()