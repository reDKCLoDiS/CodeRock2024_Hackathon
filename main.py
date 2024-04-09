import json
from dijkstra import Graph
if __name__ == "__main__":
    V = 2**18
    g = Graph(V)
    data = open('data.json')
    graph = json.load(data)
    data.close()
    for i in graph["distance"]:
        print(f"{i['Graph_from']}, {i['Graph_to']}, {i['Length']}\n")
        g.addEdge(i['Graph_from'], i['Graph_to'], i['Length'])
    #print(graph)
    print('\n')
    for i in graph["information"]:
        print(graph["information"][i])