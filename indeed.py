import os,random,sys,time
from urllib.parse import urlparse
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import json
from selenium.webdriver.common.by import By
# Handle Websites to apply for job


def indeed(namesofcompanyapplying):

    details=open("/home/sanju/PycharmProjects/pythonProject/personaldetails.json")
    data=json.load(details)

    print(data['cover_letter'])

# https://in.indeed.com/
    baseUrl="https://in.indeed.com/"
    passwordfile="/home/sanju/PycharmProjects/pythonProject/config.txt"
    driverlink="/home/sanju/Downloads/chromedriver"
    file = open(passwordfile)
    line = file.readlines()
    jobwebsiteemail=line[4]
    jobwebsitepassword=line[5]
    resume="/home/sanju/Downloads/ReactResume.pdf"
    file=os.path.abspath(resume)
    print(file)




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

    time.sleep(80)






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
            temppath = '//*[@id="mosaic-provider-jobcards"]/ul/li[' + str(i) + ']/div/div[1]/div/div[1]/div/table[1]/tbody/tr/td/div[1]/h2/a'
            time.sleep(2)
            try:
                joblink = driver.find_element(by="xpath", value=temppath).get_attribute("href")
                print("added"+joblink)
                links.append(joblink)

            except:
                continue

        print(len(links))





    # adding apply to job
    for i in links:
        driver.get(i)
        time.sleep(3)
        try:
            companyname = driver.find_element(by="xpath",
                                              value='//*[@id="viewJobSSRRoot"]/div[2]/div/div[3]/div/div/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div/div[1]/div[2]/div/a').text
            namesofcompanyapplying.append(companyname)
            print(companyname)
            applybutton = driver.find_element(by="xpath", value='//*[@id="indeedApplyButton"]')
            driver.execute_script("arguments[0].click();", applybutton)
            time.sleep(2)

            # firstname

            firstname = driver.find_element(by="xpath", value='//*[@id="input-firstName"]')
            driver.execute_script("arguments[0].click();", firstname)
            firstname.send_keys(Keys.CONTROL + "a")
            firstname.send_keys(Keys.DELETE)
            firstname.send_keys(data['fname'])

            # lastname
            lname = driver.find_element(by="xpath", value='//*[@id="input-lastName"]')
            driver.execute_script("arguments[0].click();", lname)
            lname.send_keys(Keys.CONTROL + "a")
            lname.send_keys(Keys.DELETE)
            lname.send_keys(data['lname'])

            # phonenumber
            phno = driver.find_element(by="xpath", value='//*[@id="input-phoneNumber"]')
            driver.execute_script("arguments[0].click();", phno)
            phno.send_keys(Keys.CONTROL + "a")
            phno.send_keys(Keys.DELETE)
            phno.send_keys(data['Phone'])

            # city
            city = driver.find_element(by="xpath", value='//*[@id="input-location.city"]')
            driver.execute_script("arguments[0].click();", city)
            city.send_keys(Keys.CONTROL + "a")
            city.send_keys(Keys.DELETE)
            city.send_keys(data['City,State'])

            # click continue
            nextpage = driver.find_element(by="xpath",
                                           value='/html/body/div[2]/div/div[1]/div/main/div[2]/div[2]/div/div/div[2]/div/button')
            driver.execute_script("arguments[0].click();", nextpage)

            time.sleep(2)

            # find apply resume

            try:
                uploadresume = driver.find_element(by="xpath", value='//*[@id="resume-upload"]').send_keys(file)
                time.sleep(2)

            except:
                updateresume = driver.find_element(by="xpath",value='//*[@id="resume-display-content"]/div/label/input').send_keys(file)
                time.sleep(2)
                # updateresume.send_keys(resume)
            finally:
                toemployeedetails = driver.find_element(by="xpath",value='//*[@id="ia-container"]/div/div[1]/div/main/div[2]/div[2]/div/div/div[2]/div/button')
                driver.execute_script("arguments[0].click();", toemployeedetails)

                time.sleep(8)

                prevexptitile = driver.find_element(by="xpath", value='//*[@id="jobTitle"]')
                driver.execute_script("arguments[0].click();", prevexptitile)
                prevexptitile.send_keys(data['job_title'])

                prevcompany = driver.find_element(by="xpath", value='//*[@id="companyName"]')
                driver.execute_script("arguments[0].click();", prevcompany)
                prevcompany.send_keys(data['experience_company'])

                tocoverletter = driver.find_element(by="xpath",
                                                    value='//*[@id="ia-container"]/div/div[1]/div/main/div[2]/div[2]/div/div/div[2]/div/button')
                driver.execute_script("arguments[0].click();", tocoverletter)
                time.sleep(2)
                try:
                    applywithoutcoverletter = driver.find_element(by="xpath",
                                                                  value='//*[@id="write-cover-letter-selection-card"]')
                    driver.execute_script("arguments[0].click();", applywithoutcoverletter)
                    applywithoutcoverletter.send_keys(data['cover_letter'])
                    reviewapplication = driver.find_element(by="xpath",
                                                            value='//*[@id="ia-container"]/div/div[1]/div/main/div[2]/div[2]/div/div/div[2]/div/button')
                    driver.execute_script("arguments[0].click();", applywithoutcoverletter)
                    time.sleep(3)
                except:
                    addextracoverletter = driver.find_element(by="xpath",
                                                              value='//*[@id="additional_links_section_empty-documents"]/a')
                    driver.execute_script("arguments[0].click();", addextracoverletter)
                    time.sleep(2)
                    applywithoutcoverletter = driver.find_element(by="xpath",
                                                                  value='//*[@id="write-cover-letter-selection-card"]')
                    driver.execute_script("arguments[0].click();", applywithoutcoverletter)
                    text=driver.find_element(by="xpath",value='//*[@id="coverletter-textarea"]')
                    driver.execute_script("arguments[0].click();", text)
                    time.sleep(1)
                    text.send_keys(Keys.CONTROL + "a")
                    text.send_keys(Keys.DELETE)
                    text.send_keys(data['cover_letter'])

                    reviewapplication = driver.find_element(by="xpath",
                                                            value='//*[@id="ia-container"]/div/div[1]/div/main/div[2]/div[2]/div/div/div[2]/div/button')
                    driver.execute_script("arguments[0].click();", reviewapplication)
                    time.sleep(2)

                    finalsubmit = driver.find_element(by="xpath",
                                                      value='//*[@id="ia-container"]/div/div/div/main/div[2]/div[2]/div/div/div[2]/div/button')
                    driver.execute_script("arguments[0].click();", finalsubmit)

        except:
            continue

