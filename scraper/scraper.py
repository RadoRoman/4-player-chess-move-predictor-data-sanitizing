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

RED = r'rgb(191, 59, 67);'
BLUE = r'rgb(65, 133, 191);'
YELLOW = r'rgb(192, 149, 38);'
GREEN = r'rgb(78, 145, 97);'

# code by dharmik
# with open("./data/mergedGameNr2","r") as f:
#     lines = f.readlines()
#     gameNr = [line.rstrip() for line in lines]
# print(gameNr)
# print(gameNr[0])


# game_nr = 626377
driver = webdriver.Chrome() # leave this here, since Chromedriver is in the filesystem
# url = "https://www.chess.com/4-player-chess?g={}".format(gameNr[0])
url = "https://www.chess.com/4-player-chess?g=9434531"

driver.get(url)

# driver.find_elements(By.XPATH, '//*[@id="sb"]/div[3]/a[8]')[0].click()

# time.sleep(5)
try:
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.XPATH, '//*[@id="sb"]/div[3]/a[8]'))
    )
    element[0].click()

    time.sleep(3)

except:
    driver.quit()

driver.find_elements(By.XPATH, '//*[@id="username"]')[0].send_keys(USER_NAME)
driver.find_elements(By.XPATH, '//*[@id="password"]')[0].send_keys(PASSWORD)
driver.find_elements(By.XPATH, '//*[@id="login"]')[0].click()
time.sleep(5)

page_source_code = driver.page_source
soup = BeautifulSoup(page_source_code, "html.parser")
print(soup.find("div", {"id": "fullMoveNr_1"}))

# with open("./data/pages/page.html", "w", encoding="UTF-8") as f:
#     f.write(driver.page_source)

# page = requests.get(url)

# soup = BeautifulSoup(page.text, 'html.parser')

# print(soup.prettify())

# print(soup.findall(class_='tableCell move'))