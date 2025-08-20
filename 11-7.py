# 1) 입력 받기
N = int(input())  # 정사각형 한 변 길이
matrix = []       # 2차원 배열 초기화

for _ in range(N):
    line = list(map(int, input().split()))
    matrix.append(line)

# 2) CODE 만들기
code = ""  # 최종 CODE 문자열

# 재귀를 반복문과 리스트로 처리 (스택 사용)
stack = []  
stack.append((0, 0, N))  # 시작 좌표와 크기

while stack:
    x, y, size = stack.pop()
    same = True
    first = matrix[x][y]
    
    # 해당 영역이 모두 같은지 확인
    for i in range(x, x+size):
        for j in range(y, y+size):
            if matrix[i][j] != first:
                same = False
                break
        if not same:
            break
    
    if same:
        if first == 0:
            code += "N"
        else:
            code += "D"
    else:
        code += "D"
        half = size // 2
        # 오른쪽 아래부터 스택에 넣으면 왼쪽 위부터 처리 가능
        stack.append((x+half, y+half, half))  # 오른쪽 아래
        stack.append((x+half, y, half))       # 왼쪽 아래
        stack.append((x, y+half, half))       # 오른쪽 위
        stack.append((x, y, half))            # 왼쪽 위

# 3) CODE 압축
min_len = len(code)
L = len(code)

for step in range(1, L+1):
    compressed = ""
    i = 0
    while i < L:
        unit = code[i:i+step]
        count = 1
        while i+step < L and code[i+step:i+2*step] == unit:
            count += 1
            i += step
        if count > 1:
            compressed += str(count) + unit
        else:
            compressed += unit
        i += step
    if len(compressed) < min_len:
        min_len = len(compressed)

# 4) 출력
print(code, min_len)
