import json
from dijkstra import Graph
if __name__ == "__main__":
    V = 2**18
    dist = Graph(V)
    cost = Graph(V)
    data = open('data.json')
    graph = json.load(data)
    data.close()
    print("time")
    for i in graph["distance"]:
        print(f"{i['Graph_from']}, {i['Graph_to']}, {i['Length']}\n")
        dist.addEdge(i['Graph_from'], i['Graph_to'], i['Length'])
    #print(graph)
    print("cost")
    for i in graph["cost"]:
        print(f"{i['Graph_from']}, {i['Graph_to']}, {i['cost']}\n")
        cost.addEdge(i['Graph_from'], i['Graph_to'], i['cost'])
    print("info")
    for i in graph["information"]:
        print(graph["information"][i])