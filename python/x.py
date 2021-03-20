import requests

headers = {
'Content-Type': 'application/json'
}

job_params = {
'scraper': 'google_search',
'domain': 'com',
'q': 'Mutual Fund',
'parse': 'true'
}

response = requests.post(
'https://rt.serpmaster.com/',
headers = headers,
json = job_params,
auth=('SM400822', 'fZQWWwwj37')
)

rq = response.json()["results"][0]["content"]["results"]["related_questions"]

for r in rq:
    print(r["search"]["title"])
