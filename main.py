import os,random,sys,time
from urllib.parse import urlparse
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service

baseurl="https://www.linkedin.com"
passwordfile="/home/sanju/PycharmProjects/pythonProject/config.txt"
driverlink="/home/sanju/Downloads/chromedriver"
file=open(passwordfile)
line=file.readlines()
my_username=line[0]
my_password=line[1]


website=baseurl+"/uas/login?fromSignIn=true&trk=cold_join_sign_in"
service=Service(executable_path=driverlink)
driver=webdriver.Chrome(service=service)
driver.get(website)


# #login to linkedin
elementID=driver.find_element(by="id",value='username')
elementID.send_keys(my_username)
elementID=driver.find_element(by="id",value='password')
elementID.send_keys(my_password)
elementID.submit()
#



#for posting post
# l=driver.find_element(by="xpath",value='/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/div[1]/div/div[1]/button')
# driver.execute_script("arguments[0].click();",l)
time.sleep(30)
# writer=driver.find_element(by="xpath",value='/html/body/div[3]/div/div/div[2]/div/div/div[1]/div[2]/div/div/div[2]/div/div/div[1]')
# driver.execute_script("arguments[0].click();",writer)
# writer.send_keys("Hello, I am testing my automation Bot Today here")
# time.sleep(5)
# post=driver.find_element(by="xpath",value='/html/body/div[3]/div/div/div[2]/div/div/div[2]/div[2]/div[3]/button')
# driver.execute_script("arguments[0].click();",post)
# time.sleep(5)




def searchhr(query):
    website2 = "https://www.linkedin.com/search/results/people/?keywords="+query+"&origin=SWITCH_SEARCH_VERTICAL&sid=AYI"
    driver.get(website2)
    time.sleep(3)
    # filter only hr
    # hrlist = driver.find_element(by="xpath",value='/html/body/div[5]/div[3]/div[2]/section/div/nav/div/ul/li[4]/button')
    # driver.execute_script("arguments[0].click();", hrlist)

query="tcs%20hr"
searchhr(query)

visitingID='/in/authorsanju'
completelink=baseurl+visitingID

visitedProfiles=[]
profilesQueued=[]


time.sleep(5)
containers=driver.find_elements(by="xpath",value='//*[@id="main"]/div/div/div[1]/ul/li')

for i in range(1,10):
    find="/html/body/div[5]/div[3]/div[2]/div/div[1]/main/div/div/div[1]/ul/li["+str(i)+"]/div/div/div[2]/div[1]/div[1]/div/span/span/a"
    link = driver.find_element(by="xpath",value=find).get_attribute("href")
    print(link)
    if link not in visitedProfiles:
        profilesQueued.append(link)

time.sleep(3)

while(profilesQueued):
    visitingprofileID=profilesQueued.pop();
    driver.get(visitingprofileID)
    time.sleep(8)
    hrprofile=driver.find_element(by="xpath",value='/html/body/div[4]/div[3]/div/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div/div[1]/button')
    driver.execute_script("arguments[0].click();", hrprofile)
    time.sleep(2)
    addnote=driver.find_element(by="xpath",value='/html/body/div[3]/div/div/div[3]/button[1]')
    driver.execute_script("arguments[0].click();", addnote)
    typeing=driver.find_element(by="xpath",value='/html/body/div[3]/div/div/div[2]/div[1]/textarea')
    driver.execute_script("arguments[0].click();", typeing)
    typeing.send_keys("Hello")
    break

