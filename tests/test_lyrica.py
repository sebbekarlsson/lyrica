from lyrica.Lyrica import Lyrica


lyrica = Lyrica()


def test_no_lyrics():
    lyrics = lyrica.get_lyrics('Artist Does not Exist', 'No such Song')

    assert lyrics is None


def test_lyrics():
    lyrics = lyrica.get_lyrics('tom waits', 'hold on')

    assert type(lyrics) is unicode or type(lyrics) is str
    assert 'sign' in lyrics

    lyrics = lyrica.get_lyrics('pink floyd', 'shine on you crazy diamond')

    assert type(lyrics) is unicode or type(lyrics) is str
    assert 'piper' in lyrics
