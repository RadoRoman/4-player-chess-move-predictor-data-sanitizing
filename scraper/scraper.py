from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import re
import string
import json
import sys
from SQLite_Db.ChessGameDB import getChessDb

def color_parser(string:str) -> str:
    yellow = "color: rgb(192, 149, 38)"
    blue = "color: rgb(65, 133, 191)"
    red = "color: rgb(191, 59, 67)"
    green = "color: rgb(78, 145, 97)"

    if yellow in string:
        return "Yellow"
    elif blue in string:
        return "Blue"
    elif green in string:
        return "Green"
    elif red in string:
        return "Red"
    else:
        return "No color specified"

#i suggest doing scrapping in test.py at the moment because scrapper is all in one script and every time you run it will open chrome fro chess.com login
def scraper():
    path = os.getcwd()
    x = os.path.abspath(os.path.join(path, os.pardir))
    sys.path.insert(1, x + "\\SQLite_Db")
    # print(x)
    print(os.getcwd())

    #with open("data/pages/page.html", "a", encoding="UTF-8") as f:
    html = driver.page_source
    #in loop we can accsess directly html in soup
    #f.write(html)
    soup = BeautifulSoup(html, 'html.parser')
    #f.write(soup.prettify())
    # Finding HTML code with GameNr
    GameNr = soup.find("span", {"class": "chat-content-f infomsg"})
    # Analysing and finding the GameNr with Regex
    regex1 = re.search(r'Game #(\d+)', str(GameNr))
    # Getting only the Number
    regex2 = regex1.group(1)
    # print(regex2)

    # dictionary
    jsonString = {}
    jsonString[regex2] = []

    try:
        for i in soup.find_all("div", {"class": "tableRow"}):
            roundNr = i.div.text
            color = i.find_all("div", {"class": "pointer"})
            usernames = soup.find_all("div", {"class": "truncate120"})
            player_name = [i.text.split('\n')[1].translate({ord(c): None for c in string.whitespace}) for i in usernames]
            #print(player_name)
            # print(f"\nRound Number: {roundNr.strip()}\n")

            for j in color:

                if color_parser(j.span['style']) == "Red":

                    # Easier to read every information
                    jsonString[regex2].append({
                        'username': player_name[0],
                        'round_nr': roundNr.split()[0],
                        'moves-time': j['title'],
                        'color': 'Red'
                    })
                    # print(f"Player: {player_name[0]}|{color_parser(j.span['style'])}|\n\t Moves:\n\t{j['title']}")

                elif color_parser(j.span['style']) == "Blue":

                    # Easier to read every information
                    jsonString[regex2].append({
                        'username': player_name[1],
                        'round_nr': roundNr.split()[0],
                        'moves-time': j['title'],
                        'color': 'Blue'
                    })

                    # pr}|{color_paint(f"Player: {player_name[1]rser(j.span['style'])}|\n\t Moves:\n\t{j['title']}")

                elif color_parser(j.span['style']) == "Yellow":

                    # Easier to read every information
                    jsonString[regex2].append({
                        'username': player_name[2],
                        'round_nr': roundNr.split()[0],
                        'moves-time': j['title'],
                        'color': 'Yellow'
                    })
                    # print(f"Player: {player_name[2]}|{color_parser(j.span['style'])}|\n\t Moves:\n\t{j['title']}")

                else:
                    # Easier to read every information
                    jsonString[regex2].append({
                        'username': player_name[3],
                        'round_nr': roundNr.split()[0],
                        'moves-time': j['title'],
                        'color': 'Green'
                    })
                # print(f"Player: {player_name[3]}|{color_parser(j.span['style'])}|\n\t Moves:\n\t{j['title']}")
    finally:
        getChessDb(jsonString)
    return jsonString


USER_NAME = r'TestUserForProject'
PASSWORD = r'4playerchess'

# code by dharmik
with open("C:/Users/dharm/OneDrive - IMC/FH Krems/3rd sem/Software Engineering and Project Management/project/4-player-chess-move-predictor-data-sanitizing/data/mergedGameNr2.txt", "r") as f:
    lines = f.readlines()
    gameNrlist = [line.rstrip() for line in lines]
# print(gameNr)
# print(gameNr[0])


# game_nr = 626377
for gameNr in gameNrlist:
    driver = webdriver.Chrome(
        executable_path=r"C:\Users\dharm\OneDrive - IMC\FH Krems\3rd sem\Software Engineering and Project Management\project\4-player-chess-move-predictor-data-sanitizing\chromedriver.exe")
    url = "https://www.chess.com/4-player-chess?g={}".format(gameNr)
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
    scraper()

