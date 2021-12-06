from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re

USER_NAME = r'TestUserForProject'
PASSWORD = r'4playerchess'

# code by dharmik
with open("C:/Users/dharm/OneDrive - IMC/FH Krems/3rd sem/Software Engineering and Project Management/project/4-player-chess-move-predictor-data-sanitizing/data/mergedGameNr2.txt", "r") as f:
    lines = f.readlines()
    gameNr = [line.rstrip() for line in lines]
# print(gameNr)
# print(gameNr[0])


# game_nr = 626377
driver = webdriver.Chrome(
    executable_path=r"C:\Users\dharm\OneDrive - IMC\FH Krems\3rd sem\Software Engineering and Project Management\project\4-player-chess-move-predictor-data-sanitizing\chromedriver.exe")
url = "https://www.chess.com/4-player-chess?g={}".format(gameNr[0])
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

#i suggest doing scrapping in test.py at the moment because scrapper is all in one script and every time you run it will open chrome fro chess.com login

with open("data/pages/page.html", "a", encoding="UTF-8") as f:
    html = driver.page_source
    #in loop we can accsess directly html in soup
    # html is messy so i preffered to write it after prettifying it.
    #f.write(html)
    soup = BeautifulSoup(html)
    f.write(soup.prettify())

    for s in soup.select("div.tableRow span[style]"):
        print(s['style'], s.text)

    #a = soup.find_all("div", {"class": ["fullmoveNr", "pointer"]})
    #for i in a:
        #print(i.text)
    #delete content of page
    #f.truncate(0)


# r = requests.get('http://www.chess.com/members/view/MagnusCarlsen')
# soup = BeautifulSoup(r.content)
# for i in soup.find_all('a', href=re.compile("^/livechess/game\?id=")):
#     print(re.split(r'id=', i['href'])[1])

# page = requests.get(url)

# soup = BeautifulSoup(page.text, 'html.parser')

# print(soup.prettify())

# print(soup.findall(class_='tableCell move'))