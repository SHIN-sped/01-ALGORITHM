# 그래프 입력이 주어질 때 무방향 그래프를 인접 행렬과 인접 리스트로 표현하세요.
# 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다.  
# 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 
# 인접 행렬을 출력하고, 인접 리스트를 출력하세요.

from pprint import pprint

n, m = map(int,input().split())

graph = [[0]* (n+1) for i in range(n+1)]

for i in range(m):
    u, v = map(int,input().split())
    graph[u][v] = 1
    graph[v][u] = 1

pprint(graph)


list_adj = [[] * (n+1) for i in range(n+1)]

for i in range(n+1):
    for j in range(n+1):
        if graph[i][j] == 1:
            list_adj[i].append(j)
print(list_adj)