import argparse
from lyrica.GeniusSession import GeniusSession


parser = argparse.ArgumentParser()
parser.add_argument("artist")
parser.add_argument("song")
args = parser.parse_args()


def run():
    artist = args.artist
    song = args.song

    sess = GeniusSession()

    print(sess.get_lyrics(artist, song))
