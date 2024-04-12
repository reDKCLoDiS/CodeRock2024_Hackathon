import json
from dijkstra import Graph, Graph2
if __name__ == "__main__":
    V = 2**18
    dist = Graph(V)
    cost = Graph2(V)
    data = open('data.json')
    graph = json.load(data)
    data.close()
    for i in graph["distance"]:
        dist.addEdge(i['Graph_from'], i['Graph_to'], i['Length'], i['cost'])
    for i in graph["distance"]:
        cost.addEdge(i['Graph_from'], i['Graph_to'], i['cost'], i['Length'])
    print(f"lowest time: {dist.shortestPath(31, 15)},\nlowest price: {cost.shortestPath(31, 15)}")