from lib.artists_repository import *

"""
When we call ArtistRepository.all()

We get a list of all Artist objects reflecting the seed data
"""
def test_artists_all(db_connection):
    db_connection.seed("seeds/music_web_app.sql")
    repository = ArtistRepository(db_connection)
    assert repository.all() == [
            Artist(1, 'Pixies', 'Rock'),
            Artist(2, 'ABBA', 'Pop'),
            Artist(3, 'Taylor Swift', 'Pop'),
            Artist(4, 'Nina Simone', 'Jazz')
        ]



"""
Given a new artist record

when using create() to add these records to the artist table in the database

the new records are also listed when the all() method is used
"""

def test_artist_create(db_connection):
    db_connection.seed("seeds/music_web_app.sql")
    repository = ArtistRepository(db_connection)
    repository.create(Artist(None, 'Celeste', 'GameOST'))
    assert repository.all() == [
            Artist(1, 'Pixies', 'Rock'),
            Artist(2, 'ABBA', 'Pop'),
            Artist(3, 'Taylor Swift', 'Pop'),
            Artist(4, 'Nina Simone', 'Jazz'),
            Artist(5, 'Celeste', 'GameOST')
        ]
        
