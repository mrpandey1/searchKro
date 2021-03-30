import requests
import json
import praw
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import MiniBatchKMeans, KMeans
import numpy as np
import pandas as pd
from requests_html import HTMLSession
session = HTMLSession()

def clusterz(response_array,query):
    try:
        arr = np.asarray(response_array)
        df = pd.DataFrame(arr)
        df = df.T
        df.columns = ['questions']
        df = df.iloc[1:]
        vector = TfidfVectorizer(stop_words='english', ngram_range=(1, 3))
        vector.fit(df.questions.values)
        features = vector.transform(df.questions.values)
        if len(response_array[0])>=10:
            num_of_clusters=5
        elif len(response_array[0])>5:
            num_of_clusters=3
        elif len(response_array[0])==1:
            num_of_clusters=1
        else:
            num_of_clusters=2
        cluster = KMeans(init='k-means++', n_clusters=num_of_clusters, n_init=10)
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
    except:
        return {}



def rapid_rewrite(query):
    url = "https://rewriter-paraphraser-text-changer-multi-language.p.rapidapi.com/rewrite"

    payload = json.dumps({
        "language": "en",
        "strength": 3,
        "text": query
    })
    headers = {
        'useQueryString': 'true',
        'x-rapidapi-key': '<api-key>',
        'x-rapidapi-host': 'rewriter-paraphraser-text-changer-multi-language.p.rapidapi.com',
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, data=payload)
    return json.loads(response.text)["rewrite"]


def rebbit(query):
    # query = request.args.get('query','',type=str)
    try:
        reddit_client_id = "wyciBnH1ZUiTww"
        reddit_client_secret = "pR-MXV3mH9JFRDHAGG7nfttbQBsTrQ"
        reddit_username = "0captainlevi"
        reddit_password = "qwerty1234"
        reddit = praw.Reddit(user_agent="Mozilla",
                            client_id=reddit_client_id, client_secret=reddit_client_secret,
                            username=reddit_username, password=reddit_password)
        op = [s.title for s in reddit.subreddit("AskReddit").search(query)]
        if len(op)>10:
            return op[:10]
        else:
            return op
    except:
        return []

def ginger_rewrite(query):
    try:
        url = f"https://rephrasesrv.gingersoftware.com/Rephrase/secured/rephrase?apiKey=GingerWebsite&clientVersion=2.0&lang=en&s={query}&size=5"
        response = requests.get(url)
        res = json.loads(response.text)["Sentences"]
        return [r["Sentence"] for r in res]
    except:
        return ['YOU have exhausted your rephrasing limit']

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

