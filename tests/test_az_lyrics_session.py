from lyrica.AZLyricsSession import AZLyricsSession


session = AZLyricsSession()


def test_no_lyrics():
    lyrics = session.get_lyrics('Artist Does not Exist', 'No such Song')

    assert lyrics is None


def test_lyrics():
    lyrics = session.get_lyrics('tom waits', 'hold on')

    assert type(lyrics) is unicode
    assert 'sign' in lyrics
