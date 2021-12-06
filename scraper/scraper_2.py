

from bs4 import BeautifulSoup
import re
import string

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

with open("data/pages/page.html", "r", encoding="UTF-8") as f:
    contents = f.read()
    soup = BeautifulSoup(contents, 'html.parser')

    for i in soup.find_all("div", {"class": "tableRow"}):
        roundNr = i.div.text
        color =  i.find_all("div", {"class": "pointer"})
        usernames = soup.find_all("div", {"class": "truncate120"})
        player_name = [i.text.split('\n')[2].translate({ord(c): None for c in string.whitespace}) for i in usernames]


        print(roundNr.strip())

        for j in color:
            if color_parser(j.span['style']) == "Red":
                print(player_name[0],color_parser(j.span['style']), j['title'])

            elif color_parser(j.span['style']) == "Blue":
                print(player_name[1],color_parser(j.span['style']), j['title'])

            elif color_parser(j.span['style']) == "Yellow":
                print(player_name[2],color_parser(j.span['style']), j['title'])
            
            else:
                print(player_name[3],color_parser(j.span['style']), j['title'])
            

        #s = i.find('span')
       # if s:
        #for j in i.select("span[style]"):
            #print(i.text, j['style'])
        #print(i.text, b)

    #cont = soup.select_one("div.move")
    #ram = cont.select_one("span")
    #print(ram["style"], ram.text)
    #for span in soup.select("div.movesList span"):
        #print(span["style"], span.text)
    #s in soup.select("div.tableRow span[style]"):
            #print(s['style'], s.text)


    # for j in b:
    #     print(j.text)
    #with open("data/pages/page.html", "w", encoding="UTF-8") as f2:
        #f2.write(soup.prettify())

    # style1 = soup.select_one('span[style]')['style']
    # style2 = soup.select_one('span[style]')['style']
    # #for i in style:
    # print(style1)
    # print(style2)
    #v = soup.select_one('span[style]')['style']
    # for span1 in soup.find_all('span'):
    #     print(soup.select('span[style]')['style'])
