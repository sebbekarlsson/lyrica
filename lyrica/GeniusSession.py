from requests import Session
from bs4 import BeautifulSoup


class GeniusSession(object):

    def __init__(self):
        self.base_url = 'https://genius.com/'
        self.session = Session()

    def get_lyrics(self, artist, song):
        url = (self.base_url + artist + '-' + song + '-lyrics')\
            .replace(' ', '-')

        resp = self.session.get(url)

        soup = BeautifulSoup(resp.text, 'html.parser')
        lyrics_element = soup.find('div', {'class': 'lyrics'})

        return lyrics_element.text if lyrics_element else None
