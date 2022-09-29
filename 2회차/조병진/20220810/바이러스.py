# 바이러스 🐳
# 문제 : 바이러스에 걸린 컴퓨터와 인접한 컴퓨터의 개수 구하기

N = int(input())
M = int(input())

JOIN = [[] for _ in range(N + 1)]  # 인접 리스트 생성

for _ in range(M):
    v1, v2 = map(int, input().split())
    JOIN[v1].append(v2)  # 해당 인덱스 값에 추가
    JOIN[v2].append(v1)

visited = [0] * (N + 1)  # 방문 여부 확인


def DFS(v):
    stack = [v]  # 돌아갈 곳을 기록하는 리스트
    visited[v] = 1  # 방문 처리

    while stack:  # 스택이 비어있을 때까지 반복
        cur = stack.pop()  # 정점을 빼면서 변수에 저장

        for d in JOIN[cur]:  # 뺀 정점과 인접한 모든 정점 확인
            if not visited[d]:  # 방문을 하지 않은 정점이라면
                visited[d] = 1  # 방문 처리
                stack.append(d)  # 스택에 추가


DFS(1)  # 1번 컴퓨터가 바이러스에 걸림

# visited = [0, 1, 1, 1, 0, 1, 1, 0] -> 0번 인덱스는 제외하고 1번 컴퓨터와 연결된 하나의 요소
total = 0
for i in visited:
    if i == 1:
        total += 1

print(total - 1)  # 1번은 제외하고 출력
