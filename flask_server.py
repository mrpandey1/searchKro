from flask import Flask, jsonify, request
import people_also_ask , praw

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello"

@app.route('/google/')
def google():
    query = request.args.get('query','',type=str)
    op = people_also_ask.get_related_questions(query)

    return jsonify(op)


@app.route('/reddit/')
def rebbit():
    query = request.args.get('query','',type=str)
    reddit_client_id = "wyciBnH1ZUiTww"
    reddit_client_secret = "pR-MXV3mH9JFRDHAGG7nfttbQBsTrQ"
    reddit_username = "0captainlevi"
    reddit_password = "qwerty1234"
    reddit = praw.Reddit(user_agent="Mozilla",
                     client_id=reddit_client_id, client_secret=reddit_client_secret,
                     username=reddit_username, password=reddit_password)

    return '\n'.join([s.title for s in reddit.subreddit("AskReddit").search(query)])