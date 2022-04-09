#!/usr/bin/env python
# coding: utf-8

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

def search_tickets(name_doctor):  

    opts = webdriver.ChromeOptions()
    opts.add_argument('--no-sandbox')
    opts.add_argument('--headless')
    opts.add_argument('window-size=1200x600')
    driver = webdriver.Chrome(options=opts)

    url = 'https://gorzdrav.spb.ru/service-free-schedule#%5B%7B%22district%22:%2217%22%7D,%7B%22lpu%22:%22508%22%7D%5D'
    driver.get(url)

    time.sleep(5)
    print('страница загружена')
    
    mid = driver.find_elements_by_class_name("service-speciality")
    time.sleep(5)

    doc_i = 0
    #name_doctor = 'ОТОЛАРИНГОЛОГ'
    #name_doctor = 'ЭНДОКРИНОЛОГ'
    #name_doctor = 'ХИРУРГ'
    for i in mid:
        #print(i.text.split('\n'))
        doc = i.text.split('\n')[0]
        #print(doc)
        #print('_'*20)
        if doc == name_doctor:
            #print(doc)
            doc_res = doc_i
            #print(i.get_attribute('outerHTML'))
            try:
                tickets = i.find_element_by_class_name("service-speciality__tickets")
                #print(name_doctor,tickets.text)
                log(tickets.text)
                return(tickets.text)
            except:
                #print('нет доступных')
                log('нет доступных')
                return('нет доступных')
                
            #print(tickets.text)
        doc_i += 1
    #print(name_doctor,doc_res,tickets.text)
    
    try:
        driver.quit()
    except:
        pass
    
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from datetime import *
import time


def send_sms(res):
    # create message object instance
    msg = MIMEMultipart()

    message = "Thank you"
    message = res

    # setup the parameters of the message
    password = "******"
    msg['From'] = "b***t@gmail.com"
    msg['To'] = "d***v@mail.ru"
    msg['Subject'] = "Subscription"

    # add in the message body
    msg.attach(MIMEText(message, 'plain'))

    #create server
    server = smtplib.SMTP('smtp.gmail.com: 587')

    server.starttls()

    # Login Credentials for sending the mail
    server.login(msg['From'], password)

    # send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())

    server.quit()

    print ("successfully sent email to %s:" % (msg['To']))


def log(result):    
    f = open('log.txt', 'a')
    current_datetime = datetime.now()
    f.write(str(current_datetime)+' '+result+'\n')
    f.close()


j = 0
otv = 0
while j == 0:
    
    name_doctor = 'ЭНДОКРИНОЛОГ'
    #name_doctor = 'ХИРУРГ'

    res = search_tickets(name_doctor)
    print('res =', res)

    if res != 'нет доступных':
        if res is not None:
            if otv < 2:
                send_sms(res)
                otv += 1
                print('отправлено')
            #print('res = ', res)
        
    time.sleep(60*10)





