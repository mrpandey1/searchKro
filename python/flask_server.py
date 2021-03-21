from flask import Flask, jsonify, request
import people_also_ask
from flask_cors import CORS

from helper import rebbit, rapid_rewrite, ginger_rewrite, clusterz

app = Flask(__name__)
CORS(app)


@app.route('/')
def data():
    query = request.args.get('query', '', type=str)
    output = []
    op = people_also_ask.get_related_questions(query)
    for o in op:
        output.append(o)
        for p in people_also_ask.get_related_questions(o):
            output.append(p)
    if output == []:
        output = rebbit(query)
    output = list(set(output))

    return jsonify({"response": output, "graph": clusterz([output], query)})


@app.route('/rewrite/')
def rewrite():
    query = request.args.get('query', '', type=str)
    output = []

    # Rapid API
    x = rapid_rewrite(query)
    if x != query:
        output.append(x)

    # Ginger Software
    output += ginger_rewrite(query)

    return jsonify({"response": list(set(output))})


if __name__ == '__main__':
    app.run(debug=True)
