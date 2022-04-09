from sys import argv

link = argv
f = open("u.txt",'a')
f.write(str(link))
f.close()
#link = '[8, 126, 123]https://tickets.fclm.ru/ru/sector/seat/6518/2765'
urlTicket = link[1].split(']')[1]
b = link[1].split(']')[0].replace('[','').replace(']','').replace(' ','').split(',')

from selenium import webdriver
import time
opts = webdriver.ChromeOptions()
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
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
data = {"LoginForm[username]":"d******@mail.ru", "LoginForm[password]":"******"}
url = "https://www.fclm.ru/ru/user/login"
#r = s.post(url, headers={'User-Agent':user_agent}, data=data)
r = s.post(url, headers=headers, data=data)
cookies = s.cookies
cookies_old = s.cookies
#urlTicket='https://tickets.fclm.ru/ru/sector/seat/6518/2765'
page = s.get('https://tickets.fclm.ru/ru/sector/6518', headers=headers, cookies=cookies, data=data)
soup = BeautifulSoup(page.text, 'html.parser')
ss = soup.select('.header-button-text')

print(s.cookies)
print(ss)


# In[17]:


def getTicket(urlTicket):
    global b
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
        if i[0] > 6:
            newB.append(i)
    #print(newB)
    b = newB               
    
    
    
    #print(b)
    #print('_'*30)
    bSort = sorted(b, key=lambda x: (x[0]), reverse=False)
    b = bSort
    print(b)
    return (b)
line = ''
l = []


print('Покупаем')

# In[18]:


opts.add_argument('--no-sandbox')
opts.add_argument('--headless')
opts.add_argument('window-size=1200x600')
driver = webdriver.Chrome(options=opts)
driver.get('https://www.fclm.ru/ru/user/login')

email = driver.find_element_by_css_selector('#LoginForm_username')
password = driver.find_element_by_css_selector('#LoginForm_password')


email.send_keys('d******@mail.ru')
password.send_keys('******')

ticket = driver.find_element_by_css_selector('.btn')
print(driver.find_element_by_css_selector('.btn').text)


#driver.get_screenshot_as_file('login.png')
ticket.click()

#LoginForm_username
#getTicket(urlTicket)
#driver.get_screenshot_as_file('login.png')
#print(driver.find_element_by_css_selector('.header-button-text').text)


# In[19]:


#driver.get_screenshot_as_file('login.png')

#urlTicket='https://tickets.fclm.ru/ru/sector/seat/6518/2765'
print('open')
time.sleep(1)
driver.get(urlTicket)
print('get')
#getTicket(urlTicket)
print(b)
ticketStr = '.\_empty'+'[data-realrow=\"'+str(b[0])+'\"][data-realnum=\"'+str(b[2])+'\"]'
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

#print(driver.find_element_by_css_selector('.header-button-text').text)


f = open('Den.txt','a')
f.write('ok\n')
f.close()


print('ok')
driver.close()