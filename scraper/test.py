

from bs4 import BeautifulSoup
import re
with open("data/pages/page.html", "r", encoding="UTF-8") as f:
    contents = f.read()
    soup = BeautifulSoup(contents, 'html.parser')
    #a = soup.findAll("div.movesList span")
    #b= soup.find_all("div", {"class": "fullmoveNr"})
    #print(a)
    #for span in a.select_one('span', recursive=False):
        #print(span.attrs['style'])
    #for i in a:
        #b= soup.select_one("span")
        #for span in soup.select("div.pointer span"):
        #print(i.text)
    for i in soup.find_all("div", {"class": ["tableRow"]}):
        roundNr = i.div.text
        color =  i.find_all("div", {"class": ["pointer"]})
        print(roundNr)
        for j in color:
            print(j.text)
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
