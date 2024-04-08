import json
from dijkstra import Graph
if __name__ == "__main__":
    V = 2**18
    g = Graph(V)
    data = open('data.json')
    graph = json.load(data)
    data.close()
    for i in graph["Graph_details"]:
        print(f"{i['Graph_from']}, {i['Graph_to']}, {i['Length']}\n")
    #print(graph)