from requests import get
import pandas as pd 
from bs4 import BeautifulSoup
import re

headers = {
    'User-Agent': "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1b3pre) Gecko/20090109 Shiretoko/3.1b3pre"}

index = range(0,257)
columns = ['Artist', 'Text']
df = pd.DataFrame(columns=columns)

for x in range(1,10):
    subpage_url = """
        https://www.tekstowo.pl/piosenki_artysty,peja,alfabetycznie,strona,{x}.html
        """.format(x=x)
    response = get(subpage_url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    songsList = soup.find('div', {'class': 'ranking-lista'})
    sub_songs = []
    for link in songsList.findAll('a', {'class': 'title'}, href=True):
        # print(link)
        if link['href'][0] == '/':
            sub_songs.append('https://www.tekstowo.pl' + link['href'])
        else:
            sub_songs.append('https://www.tekstowo.pl/' + link['href'])
    for song in sub_songs:
        print("Opening " + song)
        song_response = get(song, headers=headers)
        song_soup = BeautifulSoup(song_response.content, 'html.parser')
        song_text = song_soup.find('div', {'class': 'song-text'})
        try: 
            df.loc[len(df)] = ['Peja', song_text.text]
        except AttributeError:
            continue

try:
    df.to_csv('pejaBezGeorgea.csv')
except IndexError:
    pass
