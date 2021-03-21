import requests
import json
import praw
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import MiniBatchKMeans, KMeans
import numpy as np
import pandas as pd


def clusterz(response_array,query):
    arr = np.asarray(response_array)
    df = pd.DataFrame(arr)
    df = df.T
    df.columns = ['questions']
    df = df.iloc[1:]
    vector = TfidfVectorizer(stop_words='english', ngram_range=(1, 3))
    vector.fit(df.questions.values)
    features = vector.transform(df.questions.values)

    cluster = KMeans(init='k-means++', n_clusters=5, n_init=10)
    cluster.fit(features)
    df['Cluster Labels'] = cluster.labels_

    def give_me_clusters(df, num_of_clusters):
        dict = {}
        for i in range(0, num_of_clusters):
            dict[i+1] = list(df.loc[df['Cluster Labels'] == i]['questions'].values)
        return dict

    cls = give_me_clusters(df, 5)
    cls = changeFormat(cls,query)
    return cls


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


def changeFormat(data,query):
    output = dict()
    # print(data)
    output["label"] = query
    children = []
    for i in range(1, 6):
        name = f"Cluster {i}"
        o = [{"label": _} for _ in data[i]]
        # print(o)
        children.append({"label": name, "children": o})

    output["children"] = children
    # print(output)
    return output


# x = {
#     "query": "Apple",
#     "1": [
#         "What is the origin of the English word apple?"
#     ],
#     "2": [
#         "Why do people buy Apple products?",
#         "Why Apple products are getting so expensive?",
#         "Are Apple products worth the money?",
#         "Are Apple products overpriced?"
#     ],
#     "3": [
#         "What does apples mean in slang?"
#     ],
#     "4": [
#         "Whats does Apple mean?",
#         "What does Apple mean in a relationship?",
#         "What does the Apple mean sexually?"
#     ],
#     "5": [
#         "Why is Apple stuff so expensive?",
#         "Is Apple a waste of money?",
#         "Why is Apple so famous?",
#         "What is so special about Apple phones?",
#         "What makes Apple unique?",
#         "What Apple will release in 2020?",
#         "What is Apple best known for?"
#     ]
# }

# changeFormat(x)

# response_array = [[
#     "What is Elon Musk's IQ?", 
#     "How did Elon get rich?", 
#     "Why is Elon so rich?", 
#     "How is Elon Musk the richest person in the world?", 
#     "What makes Elon Musk a good leader?", 
#     "How Elon Musk changed the world?", 
#     "Why Elon Musk is famous?", 
#     "What is interesting about Elon Musk?", 
#     "Is Elon Musk a millionaire or billionaire?"
#   ]]

# clusterz(response_array,"Elon")
