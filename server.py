from flask import Flask, render_template, jsonify, session, request
from jinja2 import StrictUndefined
import server_utilities
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
    # try:
    #     tweet_text = server_utilities.connect_to_twitter(twitter_handle)
    # except Exception:
    #     return jsonify("Sorry, this user does not exist. Try again.")

    try:
        twitter_handle_markov = Markov(twitter_handle, 2)
    except Exception:
        return jsonify("Sorry, this user does not exist. Try again.")

    new_tweet = twitter_handle_markov.make_markov_tweet()
    # tweet_chains = markov.make_n_gram_chains(tweet_text, 5)
    # new_tweet = markov.make_a_markov_phrase(tweet_chains)
    results = {"new_tweet": new_tweet, "twitter_handle": twitter_handle}
    session[twitter_handle] = session.get(twitter_handle, []) + [new_tweet]

    return jsonify(results)

if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')
