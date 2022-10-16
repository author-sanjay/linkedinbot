import os,random,sys,time
from urllib.parse import urlparse
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service

def sendconnection():
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


    query="tcs%20hr"
    searchhr(query)

    visitingID='/in/authorsanju'
    completelink=baseurl+visitingID

    visitedProfiles=[]
    profilesQueued=[]


    time.sleep(5)
    containers=driver.find_elements(by="xpath",value='//*[@id="main"]/div/div/div[1]/ul/li')

    for i in range(1,10):
        find="/html/body/div[5]/div[3]/div[2]/div/div[1]/main/div/div/div[1]/ul/li["+str(i)+"]/div/div/div[3]/div/button"
        connectbutton = driver.find_element(by="xpath",value=find)
        driver.execute_script("arguments[0].click();", connectbutton)
        time.sleep(2)
        try:
            addnote=driver.find_element(by="xpath",value='/html/body/div[3]/div/div/div[3]/button[1]')
            driver.execute_script("arguments[0].click();", addnote)
            notetext=driver.find_element(by="xpath",value='//*[@id="custom-message"]')
            driver.execute_script("arguments[0].click();", notetext)
            notetext.send_keys("Hello, I would like to connect to you regarding the latest oppotunities in your company")
            sendnote=driver.find_element(by="xpath",value='/html/body/div[3]/div/div/div[3]/button[2]');
            driver.execute_script("arguments[0].click();", sendnote)
            time.sleep(5)
        except:
            print("continue")
            time.sleep(5)


    time.sleep(3)


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
preferedjobtitle="Software Developer"
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
    time.sleep(45)
    # login complete



    # search job
    jobtitle=driver.find_element(by="xpath",value='//*[@id="text-input-what"]')
    driver.execute_script("arguments[0].click();", jobtitle)
    jobtitle.send_keys(preferedjobtitle)
    if(len(preferedjobLocation)!=0):
        joblocation=driver.find_element(by="xpath",value='//*[@id="text-input-where"]')
        driver.execute_script("arguments[0].click();", joblocation)
        joblocation.send_keys(preferedjobLocation)
    else:
        print("No job location selected. No worries")
    findjob=driver.find_element(by="xpath",value='//*[@id="jobsearch"]/button')
    driver.execute_script("arguments[0].click();", findjob)
