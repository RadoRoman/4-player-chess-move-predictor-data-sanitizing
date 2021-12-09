from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import re
import string
import sys
from SQLite_Db.ChessGameDB import Chess_db


def color_parser(string: str) -> str:
    """
    converting rgb values to respective colors for given string.
    """

    # predfined colors with rgb values
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


def scraper() -> dict:
    """
    function to scrape data from given gameNr's html source page using beautifulsoup
    and storing them in Database
    """
    path = os.getcwd()
    x = os.path.abspath(os.path.join(path, os.pardir))
    sys.path.insert(1, x + "\\SQLite_Db")

    # storing html source page as a variable for further scrapping
    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser')
    # Finding HTML code for game_nr using class attribute
    game_nr = soup.find("span", {"class": "chat-content-f infomsg"})
    # Analysing and finding the game_nr with Regex
    regex1 = re.search(r'Game #(\d+)', str(game_nr))
    # Getting only the Number
    regex2 = regex1.group(1)

    # dictionary
    sql_query_dict = {}
    sql_query_dict[regex2] = []

    try:
        # searching through div section with class attribute "tableRow" which contains information such as roundNr,
        # colors and moves are located
        for element in soup.find_all("div", {"class": "tableRow"}):

            # parsing elements below for to their respective format
            roundNr = int(element.div.text.split(".")[0].translate({ord(c): None for c in string.whitespace}))
            color = element.find_all("div", {"class": "pointer"})
            usernames = soup.find_all("div", {"class": "truncate120"})
            player_name = [username.text.split('\n')[1].translate({ord(c): None for c in string.whitespace})
                           for username in usernames]

            # searching through section with class "pointer" where color and move can be found
            for element in color:

                # matching the correct color using color_parser fucntion
                if color_parser(element.span['style']) == "Red":

                    # append the data to query dictionry
                    sql_query_dict[regex2].append({
                        'username': player_name[0],
                        'round_nr': roundNr,
                        'moves': element['title'].split(" • ")[0],
                        'time': element['title'].split(" • ")[1],
                        'color': 'Red'
                    })

                # matching the correct color using color_parser fucntion
                elif color_parser(element.span['style']) == "Blue":
                    # append the data to query dictionry
                    sql_query_dict[regex2].append({
                        'username': player_name[1],
                        'round_nr': roundNr,
                        'moves': element['title'].split(" • ")[0],
                        'time': element['title'].split(" • ")[1],
                        'color': 'Blue'
                    })

                # matching the correct color using color_parser fucntion
                elif color_parser(element.span['style']) == "Yellow":
                    # append the data to query dictionry
                    sql_query_dict[regex2].append({
                        'username': player_name[2],
                        'round_nr': roundNr,
                        'moves': element['title'].split(" • ")[0],
                        'time': element['title'].split(" • ")[1],
                        'color': 'Yellow'
                    })

                else:
                    # append the data to query dictionry
                    sql_query_dict[regex2].append({
                        'username': player_name[3],
                        'round_nr': roundNr,
                        'moves': element['title'].split(" • ")[0],
                        'time': element['title'].split(" • ")[1],
                        'color': 'Green'
                    })

    finally:
        # uploading the dictionary to the database
        Chess_db(sql_query_dict)
    # return the dictionary
    return sql_query_dict


if __name__ == '__main__':
    # test username and password for login
    USER_NAME = r'TestUserForProject'
    PASSWORD = r'4playerchess'

    # getting game numbers from txt file an storing in list
    with open("data/merge_game_nr.txt", "r") as f:
        lines = f.readlines()
        game_nr_list = [line.rstrip() for line in lines]

    # scrapping each game html file using list of game numbers
    for game_nr in game_nr_list[351:400]:
        driver = webdriver.Chrome(executable_path=r"chromedriver.exe")
        # common game url with game_nr pasted using loop
        url = "https://www.chess.com/4-player-chess?g={}".format(game_nr)
        driver.get(url)

        # waiting for element to be appeared on screen to be clicked
        try:
            element = WebDriverWait(driver, 5).until(
                EC.presence_of_all_elements_located((By.XPATH, '//*[@id="sb"]/div[3]/a[8]'))
            )
            element[0].click()
            time.sleep(3)

        except:
            driver.quit()

        # passing test login credentials to the browser
        driver.find_elements(By.XPATH, '//*[@id="username"]')[0].send_keys(USER_NAME)
        driver.find_elements(By.XPATH, '//*[@id="password"]')[0].send_keys(PASSWORD)
        driver.find_elements(By.XPATH, '//*[@id="login"]')[0].click()
        time.sleep(4)
        # call the scrapper fuction after sucessfully logged in
        scraper()
