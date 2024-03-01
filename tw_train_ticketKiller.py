from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.support import expected_conditions as EC
import time


targetUrl = 'https://www.railway.gov.tw/tra-tip-web/tip/tip001/tip121/query'

browser = webdriver.Chrome()
browser.get(targetUrl)

# 設定訂票資訊

print('請輸入身分證')
userID = input()

print('請輸入起點')
startStation = input()

print('請輸入終點')
endStation = input()

print('要訂幾張')
numberOfTickets = int(input())

print('搭車日期 e.g 格式 : 20240228')

date = ''
trainNo = []

date = str(input())

print('輸入車次')

for i in range(3):
    trainNo.append(input())

browser.execute_script('window.scrollTo(0, 50)')
time.sleep(3)

# 在browser上輸入訂票人資訊
idTextArea = browser.find_element(By.ID, 'pid')
idTextArea.send_keys(userID)

time.sleep(1.5)
browser.execute_script('window.scrollTo(0, 100)')

startStationTextArea = browser.find_element(By.ID, 'startStation')
startStationTextArea.send_keys(startStation)

time.sleep(3)
browser.execute_script('window.scrollTo(0, 200)')

endStationTextArea = browser.find_element(By.ID, 'endStation')
endStationTextArea.send_keys(endStation)

time.sleep(3)
browser.execute_script('window.scrollTo(0, 300)')

numberOfTicketsTextArea = browser.find_element(By.ID, 'normalQty')
numberOfTicketsTextArea.clear()
numberOfTicketsTextArea.send_keys(numberOfTickets)

time.sleep(3)
browser.execute_script('window.scrollTo(0, 400)')

dateTextArea = browser.find_element(By.ID, 'rideDate1')
dateTextArea.clear()
dateTextArea.send_keys(date)

time.sleep(3)
browser.execute_script('window.scrollTo(0, 500)')

for i in range(3):
    trainNoTextArea = browser.find_element(By.ID, 'trainNoList' + str(i + 1))
    if trainNo[i] :
        time.sleep(1.5)
        trainNoTextArea.send_keys(trainNo[i])
    else :
        break


# Google recaptcha-anchor
time.sleep(3)
recaptchaWait = WebDriverWait(browser, timeout=2)
WebDriverWait(browser, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//*[@id="recaptcha"]/div/div/div/iframe')))
WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#recaptcha-anchor > div.recaptcha-checkbox-border'))).click()

print('')