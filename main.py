import time

from selenium import webdriver
from  selenium.webdriver.chrome.service import Service
from bs4 import  BeautifulSoup

from indeed import indeed

driverlink="/home/sanju/Downloads/chromedriver"
service=Service(executable_path=driverlink)
baseurl="https://www.linkedin.com"
driver=webdriver.Chrome(service=service)
my_username="sanjaykumar73189@gmail.com"
my_password="TELL MY NAME"
website=baseurl+"/uas/login?fromSignIn=true&trk=cold_join_sign_in"
namesofcompanyapplying=[]
preferedjobtitle = ["Software Developer", "React Js Developer", "Node Js Developer", "Full Stack Developer",
                        "Front End Developer", "BackEnd Developer"]
preferedlocation=["Delhi","Mumbai","Pune","United states","Germany","London"]
# namesofcompanyapplying.append("jellyfish")
indeed(namesofcompanyapplying,preferedjobtitle)
driver.get(website)

elementID=driver.find_element(by="id",value='username')
elementID.send_keys(my_username)
elementID=driver.find_element(by="id",value='password')
elementID.send_keys(my_password)
elementID.submit()


listofhr=[]

def searchhr(query):
    website2 = "https://www.linkedin.com/search/results/people/?keywords="+query+"&origin=SWITCH_SEARCH_VERTICAL&sid=AYI"
    driver.get(website2)

    for i in range(1, 3):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
    try:
        def getlinks(soup):
            try:
                s = soup.find('ul', {'class':'reusable-search__entity-result-list list-style-none'})
                # print(s)

                # ul=s.find_all('li',{'class':'reusable-search__result-container'})
                # # print(ul)
                try:
                    alink=s.findAll('a')
                    for all in alink:
                        temp=all['href'];
                        listofhr.append(temp)
                except:
                    print("Hello")
            except:
                print("Hello")
        getlinks(BeautifulSoup(driver.page_source))
    except:
        print("Hello")

time.sleep(3)
for ele in namesofcompanyapplying:
    x = ele.replace(" ", "%20").lower()
    x=x+"%20hr"
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
            driver.find_element(by="xpath",value='//*[@id="custom-message"]').send_keys("Hello, I found that your company is hiring developers. I would like to connect to you regardig the same and learn more about this opportunity")
            driver.find_element(by="xpath",value='/html/body/div[3]/div/div/div[3]/button[2]').click()
        finally:
            continue
    except:
        continue