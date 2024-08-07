import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9527")

driver=webdriver.Chrome(options=options)

#進入要搶的咖啡頁面
driver.get('https://shopee.tw/POP-MART-%E6%B3%A1%E6%B3%A1%E7%91%AA%E7%89%B9-THE-MONSTERS-%E5%9D%90%E5%9D%90%E6%B4%BE%E5%B0%8D%E6%90%AA%E8%86%A0%E6%AF%9B%E7%B5%A8%E7%9B%B2%E7%9B%92-i.458623340.26905100670?sp_atk=73c58354-7332-4b58-bc6c-39dfddc901f4&xptdk=73c58354-7332-4b58-bc6c-39dfddc901f4')

#最大等待時間設定為5分鐘(300秒)，等"直接購買"avaliable後點選
def do():
    WebDriverWait(driver, 300).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='btn btn-solid-primary btn--l rvHxix']"))).click()
    print('------do')

#等"去買單"avaliable後點選，需強制睡一秒最順
def do2():
    time.sleep(1)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='shopee-button-solid shopee-button-solid--primary']"))).click()
    print('-----do2')

#等"貨到付款"avaliable後點選
def do3():
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='貨到付款']"))).click()
    print('-----do3')

#等"下訂單"avaliable後點選
def do4():
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='stardust-button stardust-button--primary stardust-button--large _1qSlAe']"))).click()
    print('-----do4')

#測試先關掉最後"下訂單"
do()
do2()
do3()
# do4()
