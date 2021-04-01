from fastapi import FastAPI
from requests_html import AsyncHTMLSession
import people_also_ask
from helper import rebbit, rapid_rewrite, ginger_rewrite, clusterz 
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = [
	"*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/quora")
async def read_user_item(query: str):
	try:
		url = "https://www.quora.com/search?q="+query
		session = AsyncHTMLSession()
		r = await session.get(url)
		await r.html.arender(sleep=1, keep_page=True, scrolldown=1, timeout=60)
		a_tags = r.html.find('div.puppeteer_test_question_title')
		output = [a.text for a in a_tags]
		if len(a_tags)<12:
			op = people_also_ask.get_related_questions(query)
			for o in op:
				output.append(o)
				for p in people_also_ask.get_related_questions(o):
					output.append(p)
		# if len(output)<12:
		# 	op=rebbit(query)
		# 	output.append(op)
	except Exception as e:
		print("Error", e)
		return {"resonse":[],"graph":[]}
	return {"response":output, "graph": clusterz([output], query)}

@app.get("/")
async def root():
    return {"message": "Hello"}

@app.get('/rewrite')
async def rewrite(query:str):
	output = []
	output += ginger_rewrite(query)
	return {"response": list(set(output))}


if __name__ == '__main__':
    app.run(debug=True)
