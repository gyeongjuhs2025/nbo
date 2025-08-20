from collections import deque

# 입력 받기
N = int(input())
paper = []
for i in range(N):
    paper.append(list(map(int, input().split())))

# CODE를 만들기 위한 큐 준비
code = ""
queue = deque()
queue.append((0, 0, N))  # 시작 x, y, 크기

# 큐가 빌 때까지 반복
while queue:
    x, y, size = queue.popleft()

    # 종이의 값이 모두 같은지 확인
    first = paper[x][y]
    same = True
    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != first:
                same = False
                break
        if not same:
            break

    if same:
        # 모두 같으면 N 추가
        code += "N"
    else:
        # 다르면 D 추가하고 1x1 사각형으로 나누기 (2x2라면 바로 1x1로)
        code += "D"
        half = size // 2
        queue.append((x, y, half))           # 왼쪽위
        queue.append((x, y + half, half))    # 오른쪽위
        queue.append((x + half, y, half))    # 왼쪽아래
        queue.append((x + half, y + half, half)) # 오른쪽아래

# CODE 압축
best_length = len(code)
n = len(code)

for unit in range(1, n + 1):
    result = ""
    prev = code[0:unit]
    count = 1
    i = unit
    while i < n:
        now = code[i:i+unit]
        if now == prev:
            count += 1
        else:
            if count > 1:
                result += str(count) + prev
            else:
                result += prev
            prev = now
            count = 1
        i += unit
    if count > 1:
        result += str(count) + prev
    else:
        result += prev

    if len(result) < best_length:
        best_length = len(result)

# 출력
print(code, best_length)
