# https://ideone.com/ssId8n
# https://docs.google.com/presentation/d/1q9AAobjASs8Ot4NJ2d8XWbQhrXZT_eI8l81KE3EnvYI/edit#slide=id.g270b1618c9f_0_4230

import queue


# graph: adjacency list of directed/undirected graph
# start: starting node
# work: function called with each node in order

# Return whether each node is reachable from start.

def DFS(graph, start, work):
	stack = queue.LifoQueue()
	visited = [False for _ in graph]
	
	def visit(node):
		if not visited[node]:
			work(node)
			visited[node] = True
			stack.put(node)
	
	visit(start)
	
	while not stack.empty():
		node = stack.get()
		for neighbor in graph[node]:
			visit(neighbor)

	return visited


# graph: adjacency list of directed/undirected graph
# start: starting node
# work: function called with each node in order

# Return distances from start to each node (or None if unreachable)

def BFS(graph, start, work):
	stack = queue.Queue()
	dist = [None for _ in graph]
	
	def visit(node, d):
		if dist[node] is None:
			work(node)
			dist[node] = d
			stack.put(node)
	
	visit(start, 0)
	
	while not stack.empty():
		node = stack.get()
		for neighbor in graph[node]:
			visit(neighbor, dist[node] + 1)
			
	return dist


if __name__ == "__main__":
	graph = [[1,2], [3,4], [5,6], [], [], [], []]  # A perfect binary tree  
	
	def dump(node):
		print("Visiting: " + str(node))
	
	print("Gonna DFS!")
	res = DFS(graph, 0, dump)
	print("Result: " + str(res))
	
	print("Gonna BFS!")
	res = BFS(graph, 0, dump)
	print("Result: " + str(res))

