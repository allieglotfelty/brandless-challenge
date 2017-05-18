# Markov Chain Tweeter


# Description
The Markov Chain Tweeter takes in a Twitter handle from the user and then generates a random tweet based on the Twitter users prior tweets. All tweets are cached on the server. 

![alt text](https://github.com/allieglotfelty/brandless-challenge/blob/master/README/b_challenge.gif?raw=true "Markov gif")


# Technologies
 - Python 2.7.12
 - JavaScript
 - Flask
 - Tweepy
 - HTML5


# Installation

Open your favorite terminal.

Clone or fork this repo:

```
https://github.com/allieglotfelty/brandless-challenge.git
```

Create and activate a virtual environment inside your Markov Chain Tweeter directory:

```sh
virtualenv env
source env/bin/activate
```

Install the dependencies:

```sh
pip install -r requirements.txt
```

Login or create a Twitter account at https://twitter.com/

Create a new Twitter app at https://apps.twitter.com

Create your access token

Add your API Key, API Secret, Access Token, and Access Token Secret to a secrets.sh file using this format:

```
export TWITTER_CONSUMER_KEY="Your_Consumer_Key_Goes_Here"
export TWITTER_CONSUMER_SECRET="Your_Consumer_Secret_Goes_Here"
export TWITTER_ACCESS_TOKEN="Your_Twitter_Access_Token_Goes_Here"
export TWITTER_TOKEN_SECRET="Your_Twitter_Token_Secret_Goes_Here"
```

Source your keys from your secrets.sh file into your virtual environment

```sh
source secrets.sh
```

Run the app:
```sh
python server.py
```

Finally, navigate to "localhost:5000/" in your favorite browser to access Markov Chain Tweeter.
