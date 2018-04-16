# lyrica
> Library and Command Line Tool to get song lyrics


## Usage
### Command Line (CLI)
> To use the command line tool:

    $ lyrica <artist> <song-name>


> For example:

    $ lyrica "tom waits" "green grass"

    > Lay your head where
    > My heart used to be
    > Hold the earth above me
    > Lay down in the green grass
    > Remember when you loved me

    ...

### Using it in your application
> Here is an example:

    from lyrica.Lyrica import Lyrica

    
    lyrica = Lyrica()
    lyrics = lyrica.get_lyrics('tom waits', 'hold on')

    print(lyrics)

## Install
> To install lyrica, simply run the `setup.py`

    $ python setup.py install

> or:

    $ pip install lyrica

## Unit tests
> To run unit tests, first install `pytest`:

    $ pip install pytest

> Then to run the tests:

    $ py.test

## notes
> Lyrics are cached in `~/.lyrics` .
