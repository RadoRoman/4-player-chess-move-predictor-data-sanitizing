

from bs4 import BeautifulSoup

with open("data/pages/page.html", "r", encoding="UTF-8") as f:
    contents = f.read()
    soup = BeautifulSoup(contents)
    a = soup.find_all("div", {"class": ["fullmoveNr", "pointer"]})
    #b= soup.find_all("div", {"class": "fullmoveNr"})
    for i in a:
        print(i.text)
    # for j in b:
    #     print(j.text)
    #with open("data/pages/page2.html", "w", encoding="UTF-8") as f2:
        #f2.write(soup.prettify())
