# O(V^2+E) 解法 - 毎回全入次数をチェック
# https://ideone.com/kltmtJ
# https://docs.google.com/presentation/d/1q9AAobjASs8Ot4NJ2d8XWbQhrXZT_eI8l81KE3EnvYI/edit#slide=id.g27138cca32f_0_596
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
    graph = [[] for _ in range(v)]
    for s, t in edge_list:
        graph[s].append(t)

    degree = [0] * v
    for s, t in edge_list:
        degree[t] += 1

    for _ in range(v):
        for i in range(v):
            if degree[i] == 0:
                degree[i] = -1
                for t in graph[i]:
                    degree[t] -= 1
                print(i)
                break

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
