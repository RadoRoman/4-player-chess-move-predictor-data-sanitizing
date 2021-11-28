from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

USER_NAME = r'TestUserForProject'
PASSWORD = r'4playerchess'
game_nr = 626377
driver = webdriver.Chrome()
url = r"https://www.chess.com/4-player-chess?g=9434531-1"
driver.get(url)

# driver.find_elements(By.XPATH, '//*[@id="sb"]/div[3]/a[8]')[0].click()

# time.sleep(5)
try:
    element = WebDriverWait(driver,5).until(
        EC.presence_of_all_elements_located((By.XPATH,'//*[@id="sb"]/div[3]/a[8]'))
    )
    element[0].click()
    
    time.sleep(3)

except:
    driver.quit()

driver.find_elements(By.XPATH, '//*[@id="username"]')[0].send_keys(USER_NAME)
driver.find_elements(By.XPATH, '//*[@id="password"]')[0].send_keys(PASSWORD)
driver.find_elements(By.XPATH, '//*[@id="login"]')[0].click()
time.sleep(5)

# page = requests.get(url)

# soup = BeautifulSoup(page.text, 'html.parser')

# print(soup.prettify())

# print(soup.findall(class_='tableCell move'))