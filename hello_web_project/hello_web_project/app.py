import os
from flask import Flask, request

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==


#dfsg;jnsdgjfkskldfjns;dlfgjknsdfkgjnsdfdfg
@app.route('/submit', methods=['POST'])
def post_submit():
    name = request.form["name"]
    message = request.form["message"]
    return f"Thanks {name}, you sent this message: {message}"

@app.route('/wave', methods=['GET'])
def post_wave():
    name = request.args['name']
    return f"I am waving at {name}"

@app.route('/count_vowels', methods=['POST'])
def post_count_vowels():
    text = request.form['text']
    vowel_number = 0
    for letter in text:
        if letter in 'aeiou':
            vowel_number += 1
    return f'There are {vowel_number} vowels in "{text}"'

@app.route('/sort-names', methods=['POST'])
def post_sort_names():
    if 'names' not in request.form:
        return 'You didn\'t submit any names!', 400
    names = request.form['names']
    split_names = names.split(',')
    sorted_split_names = sorted(split_names)
    return ','.join(sorted_split_names)

#------------------------HTML--------------------------------

@app.route('/goodbye')
def get_goodbye():
    return render_template("goodbye.html")





# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://localhost:5000/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"

@app.route('/goodbye', methods=['POST'])
def goodbye():
    name = request.form['name'] # The value is 'Alice'

    # Send back a fond farewell with the name
    return f"Goodbye {name}!"

@app.route('/hello', methods=['GET'])
def hello():
    name = request.args['name'] # The value is 'David'

    # Send back a friendly greeting with the name
    return f"Hello {name}!"

# To make a request, run:
# curl "http://localhost:5000/hello?name=David"





# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))





