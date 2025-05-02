from flask import Flask, render_template
import networkx as nx

app = Flask(__name__)

@app.route("/")
def index():
    G = nx.DiGraph()

    # Define your city roads (directed edges)
    roads = {
        'A': ['B', 'D'],
        'B': ['C'],
        'C': ['A'],
        'D': ['C']
    }

    # Build the graph
    for src, destinations in roads.items():
        for dst in destinations:
            G.add_edge(src, dst)

    # Apply PageRank
    ranks = nx.pagerank(G, alpha=0.85)

    return render_template("index.html", pagerank=ranks)

if __name__ == "__main__":
    app.run(debug=True)
