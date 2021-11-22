from bs4 import BeautifulSoup
import requests

game_nr = 626377

url = f"https://www.chess.com/4-player-chess?g={game_nr}-0"

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')
print(soup.prettify())