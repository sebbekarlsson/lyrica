from lyrica.GeniusSession import GeniusSession


class Lyrica(object):

    def __init__(self):
        self.sessions = [GeniusSession()]

    def get_lyrics(self, artist, song):
        for session in self.sessions:
            lyrics = session.get_lyrics(artist, song)

            if lyrics:
                return lyrics
