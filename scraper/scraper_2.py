import os

from bs4 import BeautifulSoup
import re
import string
import json

import sys
#path = os.getcwd()
#


def color_parser(string: str) -> str:

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

def scraper():

    path = os.getcwd()
    x = os.path.abspath(os.path.join(path, os.pardir))
    sys.path.insert(1, x+"\\SQLite_Db")
    #print(x)

    #pa = os.chdir(x)
    print(os.getcwd())
    # sys.path.insert(1,'..\\SQLite_Db')
    from SQLite_Db.ChessGameDB import getChessDb
    #ChessGameDB

    with open("page.html", "r", encoding="UTF-8") as f:
        contents = f.read()
        soup = BeautifulSoup(contents, 'html.parser')

        #Finding HTML code with GameNr
        GameNr = soup.find("span",{"class": "chat-content-f infomsg"})
        #Analysing and finding the GameNr with Regex
        regex1 = re.search(r'Game #(\d+)',str(GameNr))

        #Getting only the Number
        regex2 = regex1.group(1)
        #print(regex2)

        #dictionary
        jsonString ={}
        jsonString[regex2] = []

        try:
            for i in soup.find_all("div", {"class": "tableRow"}):

                    roundNr = i.div.text
                    color = i.find_all("div", {"class": "pointer"})
                    usernames = soup.find_all("div", {"class": "truncate120"})
                    player_name = [i.text.split('\n')[2].translate({ord(c): None for c in string.whitespace}) for i in usernames]

                    #print(f"\nRound Number: {roundNr.strip()}\n")

                    for j in color:

                            if color_parser(j.span['style']) == "Red":

                                # Easier to read every information
                                jsonString[regex2].append({
                                    'username' : player_name[0],
                                    'round_nr': roundNr.split()[0],
                                    'moves-time': j['title'],
                                    'color': 'Red'
                                })
                                #print(f"Player: {player_name[0]}|{color_parser(j.span['style'])}|\n\t Moves:\n\t{j['title']}")

                            elif color_parser(j.span['style']) == "Blue":

                                # Easier to read every information
                                jsonString[regex2].append({
                                    'username': player_name[1],
                                    'round_nr': roundNr.split()[0],
                                    'moves-time': j['title'],
                                    'color': 'Blue'
                                })

                                #pr}|{color_paint(f"Player: {player_name[1]rser(j.span['style'])}|\n\t Moves:\n\t{j['title']}")

                            elif color_parser(j.span['style']) == "Yellow":

                                # Easier to read every information
                                jsonString[regex2].append({
                                    'username': player_name[2],
                                    'round_nr': roundNr.split()[0],
                                    'moves-time': j['title'],
                                    'color': 'Yellow'
                                })
                                #print(f"Player: {player_name[2]}|{color_parser(j.span['style'])}|\n\t Moves:\n\t{j['title']}")

                            else:
                                # Easier to read every information
                                jsonString[regex2].append({
                                    'username': player_name[3],
                                    'round_nr': roundNr.split()[0],
                                    'moves-time': j['title'],
                                    'color': 'Green'
                                })
                            #print(f"Player: {player_name[3]}|{color_parser(j.span['style'])}|\n\t Moves:\n\t{j['title']}")
        finally:
            getChessDb(jsonString)
        return jsonString

#if __name__ == '__main__':
scraper()


            # s = i.find('span')
        # if s:
        # for j in i.select("span[style]"):
        # print(i.text, j['style'])
        # print(i.text, b)

        # cont = soup.select_one("div.move")
        # ram = cont.select_one("span")
        # print(ram["style"], ram.text)
        # for span in soup.select("div.movesList span"):
        # print(span["style"], span.text)
        # s in soup.select("div.tableRow span[style]"):
        # print(s['style'], s.text)

        # for j in b:
        #     print(j.text)
        # with open("data/pages/page.html", "w", encoding="UTF-8") as f2:
        # f2.write(soup.prettify())

        # style1 = soup.select_one('span[style]')['style']
        # style2 = soup.select_one('span[style]')['style']
        # #for i in style:
        # print(style1)
        # print(style2)
        # v = soup.select_one('span[style]')['style']
        # for span1 in soup.find_all('span'):
        #     print(soup.select('span[style]')['style'])
