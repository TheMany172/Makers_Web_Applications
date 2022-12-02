from lib.album_repository import *

#get all method
def test_all(db_connection):
    db_connection.seed("seeds/music_web_app.sql")
    repository = AlbumRepository(db_connection)
    assert repository.all() == [
            Album(1, 'Death Magnetic', 2008, 1),
            Album(2, 'Rocket Ride', 2006, 2),
            Album(3, 'King of Fools', 2004, 2)
        ]
    

    
# call create - uses INSERT to add to the database
def test_create(db_connection):
    db_connection.seed("seeds/music_web_app.sql")
    repository = AlbumRepository(db_connection)
    album = Album(None, 'Test title', 1000, 2)
    repository.create(album)
    assert repository.all() == [
        Album(1, 'Death Magnetic', 2008, 1),
        Album(2, 'Rocket Ride', 2006, 2),
        Album(3, 'King of Fools', 2004, 2),
        Album(4, 'Test title', 1000, 2)
    ]
