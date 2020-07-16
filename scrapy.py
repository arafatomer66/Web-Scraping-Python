import requests
from bs4 import BeautifulSoup

URL = 'https://www.alteryx.com/live-training?level=3436&region[0]=26&langcode=All&event_timezone=All'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

level = soup.findAll('span', {"class": "field-content"})

levelInfi = soup.findAll('h4', {"class": "event-title"})
for i in range(len(level) - 1):
    title = level[i].get_text()
    print(title.strip())
    print(i)

for link in levelInfi:
    print(link.find('a').get("href"))
