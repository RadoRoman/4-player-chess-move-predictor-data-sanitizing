from bs4 import BeautifulSoup
import requests

game_nr = 626377

url = f"https://www.chess.com/4-player-chess?g=9434531-1"

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

print(soup.prettify())

# print(soup.findall(class_='tableCell move'))