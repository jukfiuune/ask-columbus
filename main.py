from flask import Flask, render_template, request, jsonify, redirect
from duckduckgo_search import DDGS as duckduckgo

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/search", methods=["GET"])
def search():

    query = request.args.get("q") if request.args.get("q") is not None else "christopher columbus"
    number_results = int(request.args.get("n") if request.args.get("n") is not None else "50")

    results = duckduckgo().text(query, max_results=number_results)
    return render_template("search.html", query=query, results=results, number_results=number_results)

@app.route("/lucky", methods=["GET"])
def lucky():
    query = request.args.get("q") if request.args.get("q") is not None else "christopher columbus"

    results = duckduckgo().text(query, max_results=1)
    return render_template("lucky.html", query=query, results=results)

"""@app.route("/ship", methods=["GET"])
def game():

    query = request.args.get("q")

    results = duckduckgo().text(query, max_results=50)
    return render_template("ship_mode.html", results=results)"""

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
