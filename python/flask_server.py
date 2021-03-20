from flask import Flask, jsonify, request
import people_also_ask , praw
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def data():
    query = request.args.get('query','',type=str)
    output = []
    op = people_also_ask.get_related_questions(query)
    for o in op:
        output.append(o)
        for p in people_also_ask.get_related_questions(o):
            output.append(p)
    if output==[]: output = rebbit(query)
    return jsonify({"response" :list(set(output))})

def rebbit(query):
    # query = request.args.get('query','',type=str)
    reddit_client_id = "wyciBnH1ZUiTww"
    reddit_client_secret = "pR-MXV3mH9JFRDHAGG7nfttbQBsTrQ"
    reddit_username = "0captainlevi"
    reddit_password = "qwerty1234"
    reddit = praw.Reddit(user_agent="Mozilla",
                     client_id=reddit_client_id, client_secret=reddit_client_secret,
                     username=reddit_username, password=reddit_password)
    op = [s.title for s in reddit.subreddit("AskReddit").search(query)][:10]
    return op