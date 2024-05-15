# O(V+E) 解法 - アイディア: 入次数 0 の頂点だけを Queue で常に管理
# https://ideone.com/2dq2wd
# https://docs.google.com/presentation/d/1q9AAobjASs8Ot4NJ2d8XWbQhrXZT_eI8l81KE3EnvYI/edit#slide=id.g27138cca32f_0_613

from collections import deque
import sys

def main(lines):
    # 頂点数 v, 辺の数 e
    v, e = map(int, lines[0].split(" "))
    
    # 辺の一覧（グラフ化していません。有向グラフ）
    edge_list = []
    for i in range(e):
        s, t = map(int, lines[i + 1].split(" "))
        edge_list.append((s, t))
    
    # 下記にトポロジカルソートを行った頂点の並びを出力してください。
    G = [[] for _ in range(v)]

    in_num = [0]*v

    for tmp_from,tmp_to in edge_list:
        G[tmp_from].append(tmp_to)
        in_num[tmp_to] += 1

    Q = deque()
    for i in range(v):
        if in_num[i] == 0:
            Q.append(i)

    while len(Q) > 0:
        node_id = Q.popleft()
        print("%d"%(node_id))
        for adj in G[node_id]:
            in_num[adj] -= 1
            if in_num[adj] == 0:
                Q.append(adj)

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
