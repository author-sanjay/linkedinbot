import os,random,sys,time
from urllib.parse import urlparse
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from indeed import indeed
from jobapply import jobapplylinked

namesofcompanyapplying = []
def sendconnection():
    baseurl="https://www.linkedin.com"
    passwordfile="/home/sanju/PycharmProjects/pythonProject/config.txt"
    driverlink="/home/sanju/Downloads/chromedriver"
    file=open(passwordfile)
    line=file.readlines()
    my_username=line[0]
    my_password=line[1]


    # List Of Company to send connection request

    preferedjobtitle = ["Softwa?re Developer", "React Js Developer", "Node Js Developer", "Full Stack Developer",
                        "Front End Developer", "BackEnd Developer"]
    preferedlocation=["Delhi","Mumbai","Pune","United states","Germany","London"]
    # flag for remote
        # & f_WT = 2=remote
        # & f_WT = 1=onsite
        # & f_WT = 3= hybrid
    flag="&f_WT=2"

    jobapplylinked(preferedjobtitle,preferedlocation,flag)
    indeed(namesofcompanyapplying,preferedjobtitle)
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
listofhr=[]
def searchhr(query):
    website2 = "https://www.linkedin.com/search/results/people/?keywords=" + query + "&origin=SWITCH_SEARCH_VERTICAL&sid=AYI"
    driver.get(website2)

    for i in range(1, 3):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

    def getlinks(soup):
        s = soup.find('ul', {'class': 'reusable-search__entity-result-list list-style-none'})
        # print(s)

        # ul=s.find_all('li',{'class':'reusable-search__result-container'})
        # # print(ul)
        alink = s.findAll('a')
        for all in alink:
            temp = all['href'];
            listofhr.append(temp)

    getlinks(BeautifulSoup(driver.page_source))

time.sleep(3)

sendconnection()
for ele in namesofcompanyapplying:
    x = ele.replace(" ", "%20").lower()
    searchhr(x)

for hr in listofhr:
    driver.get(hr);
    time.sleep(3)
    try:
        driver.find_element(by="xpath",
                        value='/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div/div[1]/button').click()
        try:

            driver.find_element(by="xpath",value='/html/body/div[3]/div/div/div[3]/button[1]').click()
            driver.find_element(by="xpath",value='//*[@id="custom-message"]').send_keys("Hello, I found that your company is hiring developers. I would like to connect to you regardig the same and learn more about this opportunity")
            driver.find_element(by="xpath",value='/html/body/div[3]/div/div/div[3]/button[2]').click()
        except:
            driver.find_element(by="xpath",value='/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div/div[3]/button').click()
            driver.find_element(by="xpath",value='/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div/div[3]/div/div/ul/li[4]/div').click()
            driver.find_element(by="xpath",value='/html/body/div[3]/div/div/div[3]/button[1]').click()
            driver.find_element(by="xpath",value='//*[@id="custom-message"]').send_keys("Hello")
            driver.find_element(by="xpath",value='/html/body/div[3]/div/div/div[3]/button[2]').click()
        finally:
            continue
    except:
        continue