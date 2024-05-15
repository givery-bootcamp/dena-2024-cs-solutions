# 動作するコード（計算量は全部 O(n+m+q)）
# 全くスライドの DFS をいじっていないパターン（+ work をきちんと使ったパターン）
# https://ideone.com/Mssy6n
# https://docs.google.com/presentation/d/1q9AAobjASs8Ot4NJ2d8XWbQhrXZT_eI8l81KE3EnvYI/edit#slide=id.g27138cca32f_0_238

import queue
import sys

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

def main(lines):
    # 1 行目は SNS のユーザ数 n、友達関係の数 m
    n, m = map(int, lines[0].split(" "))
    
    # (s, t) が友達であることを示す配列 friends_list
    friends_list = []
    for i in range(1, m + 1):
        s, t = map(int, lines[i].split(" "))
        friends_list.append((s, t))
    
    q = int(lines[m + 1])
    # s から t へたどり着けますか？というクエリのリスト queries_list
    queries_list = []
    for i in range(m + 2, m + q + 2):
        s, t = map(int, lines[i].split(" "))
        queries_list.append((s, t))

    # 下記に queries_list のクエリに対し、標準出力で答えるプログラムを作成してください。
    graph = [[] for _ in range(n)]
    for u, v in friends_list:
#        print(u, v)
        graph[u].append(v)
        graph[v].append(u)
#    print(graph)

    color = [-1] * n
    for node_id in range(0, n):
        if color[node_id] == -1: # まだ塗られていなければ
            def work(x):
                color[x] = node_id
            visited = DFS(graph, node_id, work)

    for u, v in queries_list:
        if color[u] == color[v]:
            print("yes")
        else:
            print("no")

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
