from collections import deque

# 입력 받기
N, M = map(int, input().split())   # 퀘스트 개수 N, 목표 퀘스트 M
time = [0] * (N + 1)               # 각 퀘스트 수행 시간
graph = [[] for _ in range(N + 1)] # 그래프 (선행 → 후행)
indegree = [0] * (N + 1)           # 진입 차수 (선행퀘스트 수)

# 각 퀘스트 정보 입력
for quest in range(1, N + 1):
    data = list(map(int, input().split()))
    time[quest] = data[0]  # 수행 시간
    for pre in data[1:]:
        if pre == -1:
            break
        graph[pre].append(quest)   # pre → quest
        indegree[quest] += 1       # quest의 선행퀘 증가

# 위상 정렬 (BFS)
queue = deque()
dp = [0] * (N + 1)  # dp[i] = i번 퀘스트를 끝내는 데 걸리는 최소 시간

# 선행퀘 없는 애들(바로 시작 가능) 큐에 넣기
for i in range(1, N + 1):
    if indegree[i] == 0:
        queue.append(i)
        dp[i] = time[i]

while queue:
    now = queue.popleft()
    for nxt in graph[now]:
        # 다음 퀘스트(nxt)는 현재 퀘스트(now)를 반드시 끝내야 가능
        dp[nxt] = max(dp[nxt], dp[now] + time[nxt])
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            queue.append(nxt)

# 결과 출력
print(dp[M])
