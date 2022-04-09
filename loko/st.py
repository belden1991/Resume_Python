from selenium import webdriver
import time
opts = webdriver.ChromeOptions()
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options


global soup
global df
global ex
global url_list
global b
global hrefSector
global l
ex = 0

s = requests.Session()
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    'Connection': 'keep-alive',
    'X-Requested-With': 'XMLHttpRequest'
}
#user_agent = ('Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) '
              #'Gecko/20100101 Firefox/50.0')
data = {"LoginForm[username]":"a****@mail.ru", "LoginForm[password]":"******"}
#data = {"LoginForm[username]":"d****@mail.ru", "LoginForm[password]":"*****"}
url = "https://www.fclm.ru/ru/user/login"
#r = s.post(url, headers={'User-Agent':user_agent}, data=data)
r = s.post(url, headers=headers, data=data)
cookies = s.cookies
cookies_old = s.cookies
#urlTicket='https://tickets.fclm.ru/ru/sector/seat/6518/2765'
page = s.get('https://www.fclm.ru/ru/user/login', headers=headers, cookies=cookies, data=data)
soup = BeautifulSoup(page.text, 'html.parser')
ss = soup.select('.header-button-text')

print(s.cookies)
print(ss)


def getTicket(urlTicket):
    global b
    global soup
    page = s.get(urlTicket, headers=headers, cookies=cookies, data=data)
    soup = BeautifulSoup(page.text, 'html.parser')

    seat = soup.select('.\_empty[data-num]')
    seatNone = soup.select('.\_none[data-num]')
    #print(seat)
    #print(seatNone)

    row = []
    num = []
    datanum = []
    for i in range(len(seat)):
        row.append(int(seat[i]['data-realrow']))
        newrow = row[::-1]
        num.append((seat[i]['data-realnum']))
        newnum = num[::-1]
        datanum.append((seat[i]['data-num']))
        newdatanum = datanum[::-1]
        row = newrow
        num = newnum
        datanum = newdatanum

    #print(len(row))
    #print(num)
    
    a = []
    for i in range(len(row)):
        #if int(row[i]) > 9:
        #print(i)
        a.append([row[i], num[i], datanum[i]])
        #else:
           # a.append([0,0])
    #print(a)
    #print('_'*20)
    
    rowNone = []
    numNone = []
    datanumNone = []
    for i in range(len(seatNone)):
        rowNone.append(int(seatNone[i]['data-realrow']))
        newrowNone = rowNone[::-1]
        numNone.append((seatNone[i]['data-realnum']))
        newnumNone = numNone[::-1]
        datanumNone.append((seatNone[i]['data-num']))
        newdatanumNone = datanumNone[::-1]
        rowNone = newrowNone
        numNone = newnumNone
        datanumNone = newdatanumNone

        #print(rowNone)
        #print(numNone)
        
    aNone = []
    for i in range(len(rowNone)):
    #if int(row[i]) > 9:
        aNone.append([rowNone[i], numNone[i], datanumNone[i]])
        #else:
           # a.append([0,0])
    #print(aNone)
    

    aSort = sorted(a, key=lambda x: (x[0], x[1]), reverse=True)
    #print(aSort)
    print('_'*30)
    aSortNone = sorted(aNone, key=lambda x: (x[0], x[1]), reverse=True)
    #print(aSortNone)
    
    b = []
    for i in range(len(aSort)-1):
        #print(aSort[i+1][0],aSort[i][0])
        if aSort[i+1][0] == aSort[i][0]: # один ли ряд [17, '69', '31'], [17, '59', '19']
            if int(aSort[i][1]) - int(aSort[i+1][1]) == 1:
                #print(aSort[i],aSort[i+1])
                u = []
                #print(aSort[i][2],aSort[i+1][2])
                u.append(aSort[i][2])
                u.append(aSort[i+1][2])
                for j in aSortNone:
                    if j[0] == aSort[i+1][0]:
                        #print(j[2])
                        u.append(j[2])
                #print(u)
                #print(sorted(u))
                listU = sorted(u)
                listUTrue = False
                for k in range(len(listU)-1):
                    if int(listU[k]) + 1 ==  int(listU[k]) + 1:
                        listUTrue = True
                    else:
                        listUTrue = False
                
                #print(listUTrue)
                if listUTrue == False:
                    b.append([aSort[i][0],int(aSort[i][1]),int(aSort[i+1][1])])
            else:
                if int(aSort[i][1]) - int(aSort[i+1][1]) == 3:
                    #print(aSort[i],aSort[i+1])
                    
                    #print(aSort[i],aSort[i+1])
                    u = []
                    #print(aSort[i][2],aSort[i+1][2])
                    u.append(aSort[i][2])
                    u.append(aSort[i+1][2])
                    for j in aSortNone:
                        if j[0] == aSort[i+1][0]:
                            #print(j[2])
                            u.append(j[2])
                    #print(u)
                    #print(sorted(u))
                    listU = sorted(u)
                    listUTrue = False
                    for k in range(len(listU)-1):
                        if int(listU[k]) + 1 ==  int(listU[k]) + 1:
                            listUTrue = True
                        else:
                            listUTrue = False
                
                    #print(listUTrue)
                    if listUTrue == True:
                        #print(aSort[i])
                        #print([aSort[i][0],int(aSort[i][1]),int(aSort[i+1][1])])
                        b.append([aSort[i][0],int(aSort[i][1]),int(aSort[i+1][1])])

         
    newB = []
    for i in b:
        if (i[0] > 6):
        #if (i[0] > 6) and (i[0] != 19):
            newB.append(i)
    #print(newB)
    b = newB               
    
    
    
    #print(b)
    #print('_'*30)
    bSort = sorted(b, key=lambda x: (x[0]), reverse=False)
    b = bSort
    #print(b)
    return (b)
global b
line = ''
l = []



import requests
from bs4 import BeautifulSoup
import pandas as pd

dataDen = {"LoginForm[username]":"d****@mail.ru", "LoginForm[password]":"******"}
dataDash = {"LoginForm[username]":"a*****@mail.ru", "LoginForm[password]":"******"}


def auth(data):
    global soup
    s = requests.Session()
    headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    'Connection': 'keep-alive',
    'X-Requested-With': 'XMLHttpRequest'
}
    #user_agent = ('Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) '
              #'Gecko/20100101 Firefox/50.0')

    url = "https://www.fclm.ru/ru/user/login"
    r = s.post(url, headers=headers, data=data)
    cookies = s.cookies
    #print(cookies)
    #print(r.cookies)

    #page = s.get('https://tickets.fclm.ru/ru/sector/6518', headers=headers, cookies=cookies, data=data)
    page = s.get('https://tickets.fclm.ru/ru/sector/6647', headers=headers, cookies=cookies, data=data)
    soup = BeautifulSoup(page.text, 'html.parser')
    ss = soup.select('.header-button-text')

    #print(s.cookies)
    print(ss)
    return(soup,page)

def findSectors(soup):
    global df
    numSectors = soup.select('g.j-sector')
    #for i in numSectors:
        #print(i['data-price'].replace(' ', ''))


    sectorsPrice = []
    sectorsHref = []
    sectorsName = []
    sectors = []
    sectorColor = []
    sectorRange = []
    for i in range(len(numSectors)):
        #print(numSectors[i]['data-price'])
        #print(numSectors[i].get_attribute('data-href'))
        if int(numSectors[i]['data-price'].replace(' ', '')) < 5000:
            sectorsPrice.append(numSectors[i]['data-price'].replace(' ', ''))
            sectorsHref.append(numSectors[i]['data-href'])
            sectorsName.append(numSectors[i].text.replace('\n', '').replace(' ',''))
            sectorColor.append(soup.select('g.j-sector > path')[i]['fill'])
    #t = soup.select('g.j-sector > path')[0]['fill']
    for i in range(len(sectorsName)):
        if sectorColor[i] == '#971515':
            sectors.append([int(sectorsName[i]), 'v', sectorsPrice[i], sectorsHref[i]])
        else:
            sectors.append([int(sectorsName[i]), 'n', sectorsPrice[i], sectorsHref[i]])
        
        
    for i in range(len(sectorsName)):
        if sectorColor[i] == '#971515':
            sectorRange.append('v')
        else:
            sectorRange.append('n')
    #print(sectorColor)
    #print(sectorsPrice, sectorsHref, sectorsName)
    #print(sectors)
    #print(sorted(sectors, key=lambda x: (x[0],x[1]), reverse=False))


    d = {'sector': sectorsName, 'range': sectorRange, 'price': sectorsPrice, 'href': sectorsHref}
    df = pd.DataFrame(data=d)
    #df.head()
    return(df)


def findUrlList(df):
    global url_list
    my_sectors=[[14,'n'],[13,'n'],[15,'n'],[12,'n'],[16,'n'],[14,'v'],[13,'v'],[15,'v'],[12,'v'],[16,'v'],[2,'n'],[4,'n'],[1,'n'],[5,'n'],[3,'v'],[2,'v'],[4,'v'],[1,'v'],[5,'v'],[11,'n'],[17,'n'],[6,'n'],[22,'n'],[11,'v'],[17,'v'],[6,'v'],[22,'v']]
    
    
    my_sectors=[[10,'v'],[21,'v'],[18,'v'],[7,'v'],[11,'n'],[22,'n'],[17,'n'],[6,'n'],[11,'v'],[22,'v'],[17,'v'],[6,'v'],[14,'n'],[15,'n'],[13,'n'],[16,'n'],[12,'n'],[14,'v'],[15,'v'],[13,'v'],[16,'v'],[12,'v'],[1,'n'],[5,'n'],[4,'n'],[2,'n'],[3,'v'],[1,'v'],[2,'v'],[4,'v']]
    
    
    url_list = []
    for i in my_sectors:
        #print(i)
        #print(df.loc[(df['sector'] == str(i[0])) & (df['range'] == i[1])]['href'])
        if len(list(df.loc[(df['sector'] == str(i[0])) & (df['range'] == i[1])]['href'])) != 0:
            #print(i)
            #print(list(df.loc[(df['sector'] == str(i[0])) & (df['range'] == i[1])]['href'])[0])
            url_list.append(list(df.loc[(df['sector'] == str(i[0])) & (df['range'] == i[1])]['href'])[0])
    #print(url_list)
    return(url_list)
        

def findSeats(url_list):
    global ex
    global b
    global hrefSector
    line = ''
    global l
    l = []
    for i in range(len(url_list)-10):
        page = s.get(url_list[i], headers=headers, cookies=cookies, data=data)
        soup = BeautifulSoup(page.text, 'html.parser')
        #print(url_list[i], str(sectorsName[i]) + '|' + str(sectors[i][1]))
        getTicket(url_list[i])
        #print(b)
        sectorItem = df.loc[df['href'] == url_list[i]]
        #print(sectorItem)
        #print(str(list(sectorItem['sector'])))
        #print(str(list(sectorItem['range'])))
        #print(str(list(sectorItem['price'])))
        #print(str(list(sectorItem['href'])))
        nameSector = (str(list(sectorItem['sector'])))
        rangeSector = (str(list(sectorItem['range'])))
        priceSector = (str(list(sectorItem['price'])))
        hrefSector = (str(list(sectorItem['href'])))
        if len(b) != 0:
            print('buy', nameSector, rangeSector, b[0], hrefSector)
            #print(b,str(hrefSector)[2:-2:])
            
            import  subprocess
            link = str(b[0])+str(hrefSector)[2:-2:]
            subprocess.Popen(['python3', 'Dash.py', link])
            #subprocess.Popen(['python3', 'Den.py', link])
            #buyFunction(b,str(hrefSector)[2:-2:])
            
            import smtplib
            from email.mime.text import MIMEText
            from email.header import Header
#df.loc[df['href'] == str(hrefSector)[2:-2:]][['sector','range','price']]
            sector = str(df.loc[df['href'] == str(hrefSector)[2:-2:]]['sector'])
            rangeS = str(df.loc[df['href'] == str(hrefSector)[2:-2:]]['range'])
            price = str(df.loc[df['href'] == str(hrefSector)[2:-2:]]['price'])
# Настройки
            mail_sender = 'b*****t@gmail.com'
            mail_receiver = 'd*****@mail.ru'
            username = 'b*****@gmail.com'
            password = '*******'
            server = smtplib.SMTP('smtp.gmail.com:587')
# Формируем тело письма
            subject = u'email от ' + mail_sender
            body = u'Куплено+'+sector+'|'+rangeS+'|'+price+'|'+str(b[0])
            msg = MIMEText(body, 'plain', 'utf-8')
            msg['Subject'] = Header(subject, 'utf-8')
# Отпавляем письмо
            server.starttls()
            server.ehlo()
            server.login(username, password)
            server.sendmail(mail_sender, mail_receiver, msg.as_string())
            server.quit()
            
            ex = 1
            break
        l.append([nameSector, rangeSector, b[0], hrefSector])
        #line = line + str(sectorsName[i]) + '|' + str(sectors[i][1])  + '|' + str(sectorsPrice[i]) + '|' + str(sectorsHref[i]) + '|' + str(b) + '\n'
    #print(line)
    
    #return(b)
    

#f = open("tickets.txt", 'a')
#f.write(line)
#f.close()



def buyFunction(b,url):
    print(b)
    auth(dataDash)
    print('open bowser')
    opts.add_argument('--no-sandbox')
    opts.add_argument('--headless')
    opts.add_argument('window-size=1200x600')
    driver = webdriver.Chrome(options=opts)
    driver.get('https://www.fclm.ru/ru/user/login')

    email = driver.find_element_by_css_selector('#LoginForm_username')
    password = driver.find_element_by_css_selector('#LoginForm_password')

    email.send_keys('a******@mail.ru')
    password.send_keys('******')

#email.send_keys('d******@mail.ru')
#password.send_keys('******')

    ticket = driver.find_element_by_css_selector('.btn')
#print(driver.find_element_by_css_selector('.btn').text)


    #driver.get_screenshot_as_file('login.png')
    ticket.click()

#LoginForm_username
#getTicket(urlTicket)
    #driver.get_screenshot_as_file('login.png')
#print(driver.find_element_by_css_selector('.header-button-text').text)


    #driver.get_screenshot_as_file('login.png')
    print(url)
    print('open url')
    driver.get(url)
    #getTicket(url)
    ticketStr = '.\_empty'+'[data-realrow=\"'+str(b[0][0])+'\"][data-realnum=\"'+str(b[0][1])+'\"]'
    print (ticketStr)
    ticket = driver.find_element_by_css_selector(ticketStr)
    ticket.click()

    #driver.get_screenshot_as_file('buy.png')
#покупка билетов
    print(driver.find_element_by_css_selector('.j-billets-btn').text)
    ticket = driver.find_element_by_css_selector('.j-billets-btn')
    ticket.click()
#оформление заказа
    import time
    time.sleep(1)
    print(driver.find_element_by_css_selector('.j-text').text)
    ticket = driver.find_element_by_css_selector('.j-text')
    #ticket.click()

    print(driver.find_element_by_css_selector('.header-button-text').text)

    
    
    auth(dataDen)
    print('open bowser')
    opts.add_argument('--no-sandbox')
    opts.add_argument('--headless')
    opts.add_argument('window-size=1200x600')
    driver = webdriver.Chrome(options=opts)
    driver.get('https://www.fclm.ru/ru/user/login')

    email = driver.find_element_by_css_selector('#LoginForm_username')
    password = driver.find_element_by_css_selector('#LoginForm_password')

    #email.send_keys('a******@mail.ru')
    #password.send_keys('******')

    email.send_keys('d******@mail.ru')
    password.send_keys('******')

    ticket = driver.find_element_by_css_selector('.btn')
#print(driver.find_element_by_css_selector('.btn').text)


    #driver.get_screenshot_as_file('login.png')
    ticket.click()

#LoginForm_username
#getTicket(urlTicket)
    #driver.get_screenshot_as_file('login.png')
#print(driver.find_element_by_css_selector('.header-button-text').text)


    #driver.get_screenshot_as_file('login.png')
    print('open url')
    driver.get(url)
    getTicket(url)
    print(b)
    ticketStr = '.\_empty'+'[data-realrow=\"'+str(b[0][0])+'\"][data-realnum=\"'+str(b[0][2])+'\"]'
    print (ticketStr)
    ticket = driver.find_element_by_css_selector(ticketStr)
    ticket.click()

    #driver.get_screenshot_as_file('buy.png')
#покупка билетов
    print(driver.find_element_by_css_selector('.j-billets-btn').text)
    ticket = driver.find_element_by_css_selector('.j-billets-btn')
    ticket.click()
#оформление заказа
    import time
    time.sleep(1)
    print(driver.find_element_by_css_selector('.j-text').text)
    ticket = driver.find_element_by_css_selector('.j-text')
    ticket.click()

    print(driver.find_element_by_css_selector('.header-button-text').text)


# In[ ]:


while ex == 0:
    auth(dataDash)
    findSectors(soup)
    df.head()
    findUrlList(df)
    findSeats(url_list)
    time.sleep(10)


# In[ ]:




