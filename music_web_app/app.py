import os
from flask import Flask, request
from lib.database_connection import *
from lib.album_repository import *
from lib.artists_repository import *

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==
@app.route('/albums', methods=['POST'])
def post_submit():
    if 'title' not in request.form or 'release_year' not in request.form or 'artist_id' not in request.form:
        return "You need to actually submit stuff...", 400
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album = Album(None, request.form['title'],request.form['release_year'],request.form['artist_id'])
    repository.create(album)
    return '', 200

@app.route('/albums')
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    repository.all()
    return "\n".join(
        f"{album}" for album in repository.all()
    )

@app.route('/artists')
def get_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    repository.all()
    s = [artist.name for artist in repository.all()]
    return ", ".join(s)

@app.route('/artists', methods=['POST'])
def post_new_artist():
    if 'name' not in request.form or 'genre' not in request.form:
        return "You need to actually submit stuff...", 400
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artist = Artist(None, request.form['name'],request.form['genre'])
    repository.create(artist)
    return '', 200

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))

