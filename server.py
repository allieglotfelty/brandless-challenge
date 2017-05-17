from flask import Flask, render_template, jsonify, session, request
from jinja2 import StrictUndefined
import server_utilities


app = Flask(__name__)

app.secret_key = 'asldfjajeiownasldknvauwaeadsfanadnvaoqpndcsdf'

app.jinja_env.undefined = StrictUndefined


@app.route('/')
def display_homepage():
    """Displays homepage."""

    return render_template('homepage.html')


@app.route('/markovify', methods=["GET"])
def create_markov_tweet():
    """Creates Markov tweet based on tweets from the given Twitter handle."""

    print "I'm here"
    twitter_handle = request.args.get('twitter-handle')
    print twitter_handle
    tweet_text = server_utilities.connect_to_twitter(twitter_handle)

    return jsonify(tweet_text)

if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')
