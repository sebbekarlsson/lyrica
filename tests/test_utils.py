from lyrica.utils import clean_lyrics


def test_clean_lyrics():
    lyrics = '\n\nhello world\n\n\n'

    assert clean_lyrics(lyrics) == 'hello world'

    lyrics = '       hello world       '

    assert clean_lyrics(lyrics) == 'hello world'

    lyrics = 'hello world'

    assert clean_lyrics(lyrics) == 'hello world'
