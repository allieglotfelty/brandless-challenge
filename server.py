from flask import Flask, render_template, jsonify, session, request
from jinja2 import StrictUndefined
from markov import Markov

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

    twitter_handle = request.args.get('twitter-handle')

    try:
        twitter_handle_markov = Markov(twitter_handle, 2)
    except Exception:
        return jsonify("Sorry, this user does not exist. Try again.")

    new_tweet = twitter_handle_markov.make_markov_tweet()
    session[twitter_handle] = session.get(twitter_handle, []) + [new_tweet]

    results = {"new_tweet": new_tweet, "twitter_handle": twitter_handle}

    return jsonify(results)

if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')
