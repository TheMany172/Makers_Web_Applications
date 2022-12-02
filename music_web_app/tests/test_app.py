# Tests for your routes go here
import pytest

def test_post_albums(db_connection, web_client):
    db_connection.seed("seeds/music_web_app.sql")
    response = web_client.post("/albums", data={'title': 'Master of Puppets', 'release_year': '1986', 'artist_id': '1'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == ""


def test_post_and_get_albums(db_connection, web_client):
    db_connection.seed("seeds/music_web_app.sql")
    response = web_client.post("/albums", data={'title': 'Master of Puppets', 'release_year': '1986', 'artist_id': '1'})

    assert response.status_code == 200
    assert response.data.decode('utf-8') == ""

    
    get_response = web_client.get("/albums")
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "" \
            "Album(1, Death Magnetic, 2008, 1)\n" \
            "Album(2, Rocket Ride, 2006, 2)\n" \
            "Album(3, King of Fools, 2004, 2)\n" \
            "Album(4, Master of Puppets, 1986, 1)"
    ""

def test_post_with_nothing(db_connection, web_client):
    db_connection.seed("seeds/music_web_app.sql")
    response = web_client.post("/albums")

    assert response.status_code == 400
    assert response.data.decode('utf-8') == "You need to actually submit stuff..."

    
    get_response = web_client.get("/albums")
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "" \
            "Album(1, Death Magnetic, 2008, 1)\n" \
            "Album(2, Rocket Ride, 2006, 2)\n" \
            "Album(3, King of Fools, 2004, 2)"
    ""


# CHALLENGE-----------------------------------------------


"""
GET/ artists

before running POST route

return complete list of albums, response == 200
"""
def test_get_artists(db_connection, web_client):
    db_connection.seed("seeds/music_web_app.sql")
    get_response = web_client.get("/artists")
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "Pixies, ABBA, Taylor Swift, Nina Simone"

"""
POST /artists

No return, expected response == 200

adds new artist with name: Wild Nothing and genre: Indie
"""
def test_post_artist(db_connection, web_client):
    db_connection.seed("seeds/music_web_app.sql")
    response = web_client.post("/artists", data={'name': 'Wild Nothing', 'genre': 'Indie'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == ""

"""
GET/ artists

after running POST route

return complete list of artists including new artist Wild Nothing

response == 200
"""
def test_post_and_get_artists(db_connection, web_client):
    db_connection.seed("seeds/music_web_app.sql")
    response = web_client.post("/artists", data={'name': 'Wild Nothing', 'genre': 'Indie'})

    assert response.status_code == 200
    assert response.data.decode('utf-8') == ""


    get_response = web_client.get("/artists")
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "Pixies, ABBA, Taylor Swift, Nina Simone, Wild Nothing"


"""
POST /artists

Return "Bad Request", expected response == 400

When POST request is made without the necessary body parameters, name/genre
"""

def test_bad_post(db_connection, web_client):
    db_connection.seed("seeds/music_web_app.sql")
    response = web_client.post("/artists")
    assert response.status_code == 400
    assert response.data.decode('utf-8') == "You need to actually submit stuff..."
