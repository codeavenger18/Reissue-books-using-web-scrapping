from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import json
from datetime import datetime
from collections import OrderedDict
from selenium.common.exceptions import NoSuchElementException


total=0
ttf=0
login_page="http://14.139.108.229/w27/MyInfo/w27MyInfo.aspx"
#browser = webdriver.Firefox()
chromedriver = r'''C:\Users\Divakar Singh\Downloads\Compressed\chromedriver'''
#browser=webdriver.PhantomJS()
browser=webdriver.Chrome(chromedriver)
chrome_options = Options()

file=open("fe.txt","w")
fi=open('new_fe.txt','w')
with open("fe_reg.txt","r") as f:
    data=f.readlines()
for x in range(0,295):
    t=data[x]
    if(int(t[0:6])<99999):
        r=t[0:5]
    if(int(t[0:6])>99999):
        r=t[0:6]
    browser.get("http://14.139.108.229/W27/login.aspx?ReturnUrl=%2fw27%2fMyInfo%2fw27MyInfo.aspx")
    time.sleep(3)
    if(browser.current_url == "http://14.139.108.229/W27/login.aspx?ReturnUrl=%2fw27%2fMyInfo%2fw27MyInfo.aspx" ):        
        try:
            email = browser.find_element_by_id("txtUserName")
            email.send_keys(r)
        except NoSuchElementException as exception:
                    time.sleep(1)
                    print ("1"+"\t"+r)
                    browser.get("http://14.139.108.229/w27/MyInfo/w27MyInfo.aspx")                    
                    continue
        try:
            pwd = browser.find_element_by_id("Password1")
            pwd.send_keys("MEMBER")
        except NoSuchElementException as exception:
                    time.sleep(1)
                    print ("2"+"\t"+r)
                    browser.get("http://14.139.108.229/w27/MyInfo/w27MyInfo.aspx")
                    i=1
                    while i==1:
                        try:
                            logout = browser.find_element_by_link_text('Logout')
                            logout.click()
                            time.sleep(1)
                            i=0
                        except NoSuchElementException as exception:
                                time.sleep(1)
                                print ("4"+"\t"+r)
                                browser.get("http://14.139.108.229/w27/MyInfo/w27MyInfo.aspx")                      
                                i=1
                    continue
        try:
            login = browser.find_element_by_id("Submit1")
            login.click()
        except NoSuchElementException as exception:
                    time.sleep(1)
                    print ("3"+"\t"+r)
                    browser.get("http://14.139.108.229/w27/MyInfo/w27MyInfo.aspx")
                    i=1
                    while i==1:
                        try:
                            logout = browser.find_element_by_link_text('Logout')
                            logout.click()
                            time.sleep(1)
                            i=0
                        except NoSuchElementException as exception:
                                time.sleep(1)
                                print ("4"+"\t"+r)
                                browser.get("http://14.139.108.229/w27/MyInfo/w27MyInfo.aspx")                      
                                i=1
                    continue
        if(browser.current_url == login_page):
            text=browser.find_element_by_id("ctl00_ContentPlaceHolder1_CtlMyLoans1_lblTotFineAmt").text
            nob=browser.find_element_by_id("ctl00_ContentPlaceHolder1_CtlMyLoans1_lblItems").text
            print (r+"\t"+text+"\t"+nob)
            n=int(nob)
            total=total+int(text)
            file.write(r+"\t"+text+"\t"+nob)
            tf=0
            if n>4:
                n=5
            
            for i in range (0,n):
                content = browser.find_element_by_css_selector("#ctl00_ContentPlaceHolder1_CtlMyLoans1_grdLoans > tbody > tr:nth-child("+str(i+2)+") > td:nth-child(5)").text
                fine=browser.find_element_by_id("ctl00_ContentPlaceHolder1_CtlMyLoans1_grdLoans_ctl0"+str(i+2)+"_lblFine").text
                if int(fine)>=2 :
                    #print (fine+"\t"+content)
                    file.write(fine+"\t"+content)
                    tf=tf+int(fine)
                fi.write(content+"\t"+r+"\n")
                #e.setdefault(content, {})[r]=1
            file.write("Total = "+ str(tf)+"\n")
            #print ("TOTAL = "+ str(tf)+"\n")
            ttf=ttf+tf
            time.sleep(1)
            i=1
            while i==1:
                try:
                    logout = browser.find_element_by_link_text('Logout')
                    logout.click()
                    time.sleep(1)
                    i=0
                except NoSuchElementException as exception:
                        time.sleep(1)
                        print ("4"+"\t"+r)
                        browser.get("http://14.139.108.229/w27/MyInfo/w27MyInfo.aspx")                      
                        i=1
        else:
            continue
    else:
        print ("5"+"\t"+r)
        browser.get("http://14.139.108.229/w27/MyInfo/w27MyInfo.aspx")
        i=1
        while i==1:
            try:
                logout = browser.find_element_by_link_text('Logout')
                logout.click()
                time.sleep(1)
                i=0
            except NoSuchElementException as exception:
                    time.sleep(1)
                    print ("4"+"\t"+r)
                    browser.get("http://14.139.108.229/w27/MyInfo/w27MyInfo.aspx")                      
                    i=1
        continue
    
#ordered_data = OrderedDict(
 #   sorted(e.items(), key = lambda x:datetime.strptime(x[0], '%d-%b-%Y'), reverse=False))

#di=dict(ordered_data)
#ordered = OrderedDict(sorted(e.items(), key=lambda t: t[0]))
#print (ordered)
#for key,value in sorted(di.items()):
   # print (key,value)
   # fi.write(str(key)+'\t'+str(value)+'\n\n')

#print (ordered_data)
#fi.write(ordered_data)
file.write("\n\nTotal : "+str(total)+"\nFine can be saved : "+str(ttf))
file.close()
f.close()
fi.close()
#print (str(total)+"\t"+str(ttf))
browser.close()

#https://www.aitpune.com/Applied-Science.aspx
#form1 > div:nth-child(3) > section > div > div > div > div > ul > li.tabs-3.resp-tab-item.hor_1 > span
#comp-1
#miyazaki > tbody > tr:nth-child(1) > td:nth-child(2)
#miyazaki > tbody > tr:nth-child(2) > td:nth-child(2)
#comp-2
#form1 > div:nth-child(3) > section > div > div > div > div > div > div.fc-tab-3.resp-tab-content.hor_1.resp-tab-content-active > ul > li:nth-child(2) > a
#entc-1
#form1 > div:nth-child(3) > section > div > div > div > div > div > div.fc-tab-3.resp-tab-content.hor_1.resp-tab-content-active > ul > li:nth-child(3) > a
#ctl00_ContentPlaceHolder1_CtlMyLoans1_grdLoans > tbody > tr:nth-child(3) > td:nth-child(5)
#ctl00_ContentPlaceHolder1_CtlMyLoans1_grdLoans > tbody > tr:nth-child(2) > td:nth-child(5)
##ctl00_ContentPlaceHolder1_CtlMyLoans1_grdLoans_ctl02_lblFine
#//*[@id="ctl00_ContentPlaceHolder1_CtlMyLoans1_grdLoans"]/tbody/tr[2]/td[5]
#ctl00_ContentPlaceHolder1_CtlMyLoans1_grdLoans_ctl02_lblFine
#ctl00_ContentPlaceHolder1_CtlMyLoans1_grdLoans_ctl03_lblFine
#ctl00_ContentPlaceHolder1_CtlMyLoans1_grdLoans_ctl04_lblFine
#abhinayS1!
#chauhan.abhinay.singh@gmail.com
