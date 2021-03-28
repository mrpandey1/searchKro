from flask import Flask, jsonify, request, send_file, make_response
import people_also_ask
from flask_cors import CORS
import pandas as pd
from helper import rebbit, rapid_rewrite, ginger_rewrite, clusterz , scrape_from_quora

app = Flask(__name__)
CORS(app)


@app.route('/')
def data():
    query = request.args.get('query', '', type=str)
    frmt = request.args.get('format', 'json', type=str)
    output = []
    op = people_also_ask.get_related_questions(query)
    for o in op:
        output.append(o)
        for p in people_also_ask.get_related_questions(o):
            output.append(p)
    # if len(output)<10:
    #     output=scrape_from_quora(query)
    if len(output)<10:
        output = rebbit(query)
    output = list(set(output))
    if frmt == "csv":
        path = "<path to temp.csv file>"
        df = pd.DataFrame(output)
        df.to_csv('temp.csv',header=False)
        return send_file(path, mimetype='text/csv',
                         attachment_filename='Response.csv',
                         as_attachment=True)
    # print(len(output))
    return jsonify({"response": output, "graph": clusterz([output], query)})


@app.route('/rewrite/')
def rewrite():
    query = request.args.get('query', '', type=str)
    output = []

    # Rapid API
    # x = rapid_rewrite(query)
    # if x != query:
    #     output.append(x)

    # Ginger Software
    output += ginger_rewrite(query)

    return jsonify({"response": list(set(output))})


if __name__ == '__main__':
    app.run(debug=True)
