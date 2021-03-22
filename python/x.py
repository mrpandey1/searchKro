import requests

headers = {
'Content-Type': 'application/json'
}

job_params = {
'scraper': 'google_search',
'domain': 'com',
'q': '<query>',
'parse': 'true'
}

response = requests.post(
'https://rt.serpmaster.com/',
headers = headers,
json = job_params,
auth=('<username>', '<password>')
)

rq = response.json()["results"][0]["content"]["results"]["related_questions"]

for r in rq:
    print(r["search"]["title"])
