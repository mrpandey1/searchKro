import praw

reddit_client_id = "wyciBnH1ZUiTww"
reddit_client_secret = "pR-MXV3mH9JFRDHAGG7nfttbQBsTrQ"
reddit_username = "0captainlevi"
reddit_password = "qwerty1234"

reddit = praw.Reddit(user_agent="Mozilla",
                     client_id=reddit_client_id, client_secret=reddit_client_secret,
                     username=reddit_username, password=reddit_password)

for submission in reddit.subreddit("AskReddit").search("Elon"):
    print(submission.title)