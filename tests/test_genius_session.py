from lyrica.GeniusSession import GeniusSession


session = GeniusSession()


def test_no_lyrics():
    lyrics = session.get_lyrics('Artist Does not Exist', 'No such Song')

    assert lyrics is None


def test_lyrics():
    lyrics = session.get_lyrics('pink floyd', 'shine on you crazy diamond')

    assert type(lyrics) is unicode or type(lyrics) is str
    assert 'piper' in lyrics
