from lib.album import *

#constructs an album with id, title, release, artist id
def test_constructs():
    album = Album(1, "test title", 1000, 2)
    assert album.id == 1
    assert album.title == "test title"
    assert album.release_year == 1000
    assert album.artist_id == 2


"""
We can format albums to strings nicely
"""
def test_albums_format_nicely():
    album1 = Album(1, "Ok Computer", 1997, 3)

    assert str(album1) == "Album(1, Ok Computer, 1997, 3)"
    # Try commenting out the `__repr__` method in lib/artist.py
    # And see what happens when you run this test again.

"""
We can compare two identical albums
And have them be equal
"""
def test_albums_are_equal():
    album1 = Album(1, "Ok Computer", 1997, 3)
    album2 = Album(1, "Ok Computer", 1997, 3)
    
    assert album1 == album2
    # Try commenting out the `__eq__` method in lib/artist.py
    # And see what happens when you run this test again.
