from flask import Flask, render_template, request, jsonify, redirect
from duckduckgo_search import DDGS as duckduckgo

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")
    
@app.route("/search", methods=["GET"])
def search():

    query = request.args.get("q")

    results = duckduckgo().text(query, max_results=50)
    return render_template("search.html", query=query, results=results)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)