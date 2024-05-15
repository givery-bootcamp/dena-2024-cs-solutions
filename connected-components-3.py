# 動作するコード（計算量は全部 O(n+m+q)）
# Pattern 2 の work の位置を stack に追加したときではなく stack から取り出したときに変更したバージョン
# https://ideone.com/i8dU8X
# https://docs.google.com/presentation/d/1q9AAobjASs8Ot4NJ2d8XWbQhrXZT_eI8l81KE3EnvYI/edit#slide=id.g27138cca32f_0_238

import queue
import sys

sys.setrecursionlimit(100000)

def DFS(graph, color, current_node, initial_node):
    color[current_node] = initial_node
    for next_node in graph[current_node]:
        if color[next_node] == -1:
            DFS(graph, color, next_node, initial_node)

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
        graph[u].append(v)
        graph[v].append(u)

    color = [-1] * n
    for node_id in range(0, n):
        if color[node_id] == -1: # まだ塗られていなければ
            visited = DFS(graph, color, node_id, node_id)

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
