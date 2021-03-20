import requests
import json
import praw


def rapid_rewrite(query):
    url = "https://rewriter-paraphraser-text-changer-multi-language.p.rapidapi.com/rewrite"

    payload = json.dumps({
        "language": "en",
        "strength": 3,
        "text": query
    })
    headers = {
        'useQueryString': 'true',
        'x-rapidapi-key': 'f545c18230msh642a4a120a7330ep199ac8jsn3254cf995ae4',
        'x-rapidapi-host': 'rewriter-paraphraser-text-changer-multi-language.p.rapidapi.com',
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, data=payload)
    return json.loads(response.text)["rewrite"]

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

def ginger_rewrite(query):
    url = f"https://rephrasesrv.gingersoftware.com/Rephrase/secured/rephrase?apiKey=GingerWebsite&clientVersion=2.0&lang=en&s={query}&size=5"
    response = requests.get(url)
    res = json.loads(response.text)["Sentences"]
    return [r["Sentence"] for r in res]
