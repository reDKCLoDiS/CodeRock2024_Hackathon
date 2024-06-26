import heapq

iPair = tuple

class Graph:
	def __init__(self, V: int):
		self.V = V
		self.adj = [[] for _ in range(V)]

	def addEdge(self, u: int, v: int, w: int, c: int = 150):
		self.adj[u].append((v, w, c))
		self.adj[v].append((u, w, c))

	def shortestPath(self, src: int, goal: int):

		pq = []
		heapq.heappush(pq, (0, src))
		costs = [float('inf')] * self.V
		dist = [float('inf')] * self.V
		dist[src] = 0
		costs[src] = 0
		us = []

		while pq:

			d, u = heapq.heappop(pq)

			for v, weight, cost in self.adj[u]:

				if dist[v] > dist[u] + weight:
					costs[v] = costs[u] + cost
					dist[v] = dist[u] + weight
					us.append(u)
					heapq.heappush(pq, (dist[v], v))
		res = [i for n, i in enumerate(us) if i not in us[:n]]
		return dist[goal], costs[goal], res

class Graph2:
	def __init__(self, V: int):
		self.V = V
		self.adj = [[] for _ in range(V)]

	def addEdge(self, u: int, v: int, w: int, c: int = 150):
		self.adj[u].append((v, w, c))
		self.adj[v].append((u, w, c))

	def shortestPath(self, src: int, goal: int):

		pq = []
		heapq.heappush(pq, (0, src))
		costs = [float('inf')] * self.V
		dist = [float('inf')] * self.V
		dist[src] = 0
		costs[src] = 0
		us = []

		while pq:

			d, u = heapq.heappop(pq)

			for v, weight, cost in self.adj[u]:

				if dist[v] > dist[u] + weight:
					costs[v] = costs[u] + cost
					dist[v] = dist[u] + weight
					us.append(u)
					heapq.heappush(pq, (dist[v], v))
		res = [i for n, i in enumerate(us) if i not in us[:n]]
		return costs[goal], dist[goal], res

if __name__ == "__main__":

	V = 2**18
	g = Graph(V)

	g.addEdge(0, 1, 4)
	g.addEdge(0, 7, 8)
	g.addEdge(1, 2, 8)
	g.addEdge(1, 7, 11)
	g.addEdge(2, 3, 7)
	g.addEdge(2, 8, 2)
	g.addEdge(2, 5, 4)
	g.addEdge(3, 4, 9)
	g.addEdge(3, 5, 14)
	g.addEdge(4, 5, 10)
	g.addEdge(5, 6, 2)
	g.addEdge(6, 7, 1)
	g.addEdge(6, 8, 6)
	g.addEdge(7, 8, 7)

	g.shortestPath(0, 5)