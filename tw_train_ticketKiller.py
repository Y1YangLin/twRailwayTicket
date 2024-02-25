from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common import NoSuchElementException, ElementNotInteractableException


targetUrl = 'https://www.railway.gov.tw/tra-tip-web/tip/tip001/tip121/query'

browser = webdriver.Chrome()
browser.get(targetUrl)

# 設定訂票資訊

# print('請輸入身分證')
# userID = input()

# print('請輸入起點')
# startStation = input()

# print('請輸入終點')
# endStation = input()

# print('要訂幾張')
# numberOfTickets = int(input())

# print('搭車日期 e.g 格式 : 20240228')

# date = ''
# trainNo = []

# date = str(input())

# print('輸入車次')

# for i in range(3):
#     trainNo.append(input())

# # 在browser上輸入訂票人資訊
# idTextArea = browser.find_element(By.ID, 'pid')
# idTextArea.send_keys(userID)

# startStationTextArea = browser.find_element(By.ID, 'startStation')
# startStationTextArea.send_keys(startStation)

# endStationTextArea = browser.find_element(By.ID, 'endStation')
# endStationTextArea.send_keys(endStation)

# numberOfTicketsTextArea = browser.find_element(By.ID, 'normalQty').clear()
# numberOfTicketsTextArea.send_keys(numberOfTickets)

# dateTextArea = browser.find_element(By.ID, 'rideDate1').clear()
# dateTextArea.send_keys(date)

# for i in range(1, 4):
#     trainNoTextArea = browser.find_element(By.ID, 'trainNoList' + str(i))
#     if trainNo[i] :
#         trainNoTextArea.send_keys(trainNo[i])
#     else :
#         break


# Google recaptcha-anchor

recaptchaWait = WebDriverWait(browser, timeout=2)

recaptcha = browser.find_element(By.XPATH, '//*[@id="rc-anchor-container"]').click()

print('')