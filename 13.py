# 제13회 전국상업경진대회 비즈니스 프로그래밍 문제 풀이

# 문제 1: 총점과 평균점수 구하기
def problem1():
    n = int(input())  # 과목 수
    
    scores = []  # 모든 점수를 저장할 리스트
    
    # 점수를 입력받기 (한 줄에 최대 5개씩)
    while len(scores) < n:
        line_scores = list(map(float, input().split()))
        scores.extend(line_scores)
    
    # 정확히 n개만 사용 (혹시 더 많이 입력된 경우 대비)
    scores = scores[:n]
    
    # 총점 계산
    total = sum(scores)
    
    # 평균 계산
    average = total / n
    
    # 출력 (총점은 소수점 첫째자리, 평균은 반올림하여 첫째자리)
    print(f"{total:.1f}")
    print(f"{average:.1f}")

# 문제 2: 토끼의 번식 (피보나치 수열)
def problem2():
    n = int(input())
    
    # 피보나치 수열: F(0)=1, F(1)=1, F(n)=F(n-1)+F(n-2)
    if n == 0:
        print(1)
    elif n == 1:
        print(1)
    else:
        # 처음 두 값
        prev2 = 1  # F(0)
        prev1 = 1  # F(1)
        
        # n번째까지 계산
        for i in range(2, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
        
        print(current)

# 문제 3: 진수 변환기
def problem3():
    n = int(input())
    
    # 2진수 변환
    binary = ""
    temp = n
    if temp == 0:
        binary = "0"
    else:
        while temp > 0:
            binary = str(temp % 2) + binary
            temp = temp // 2
    
    # 3진수 변환
    ternary = ""
    temp = n
    if temp == 0:
        ternary = "0"
    else:
        while temp > 0:
            ternary = str(temp % 3) + ternary
            temp = temp // 3
    
    # 4진수 변환
    quaternary = ""
    temp = n
    if temp == 0:
        quaternary = "0"
    else:
        while temp > 0:
            quaternary = str(temp % 4) + quaternary
            temp = temp // 4
    
    print(binary)
    print(ternary)
    print(quaternary)

# 문제 4: 문장 암호화
def problem4():
    cipher_key = input().strip()  # 암호화 키
    text = input().strip()  # 암호화할 문장
    
    # 알파벳 순서 (a~z)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    # 암호화된 결과
    result = ""
    
    for char in text:
        if char == ' ':
            result += ' '  # 공백은 그대로
        else:
            # 해당 알파벳의 위치 찾기
            pos = alphabet.find(char)
            # 암호화 키의 해당 위치 문자로 변환
            result += cipher_key[pos]
    
    print(result)

# 문제 5: 증가하는 난이도 (최장 증가 부분 수열)
def problem5():
    n = int(input())
    difficulties = list(map(int, input().split()))
    
    # 동적 프로그래밍으로 최장 증가 부분 수열 길이 구하기
    dp = [1] * n  # 각 위치에서 끝나는 최장 증가 부분 수열의 길이
    
    for i in range(1, n):
        for j in range(i):
            if difficulties[j] < difficulties[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    # 최대값 출력
    print(max(dp))

# 문제 6: 바이러스 전파 (그래프 탐색)
def problem6():
    n = int(input())  # 컴퓨터 수
    p = int(input())  # 연결 쌍 수
    
    # 인접 리스트로 그래프 표현
    graph = [[] for _ in range(n + 1)]
    
    # 연결 정보 입력
    for _ in range(p):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    t = int(input())  # 최초 감염 컴퓨터
    
    # BFS로 연결된 모든 컴퓨터 찾기
    visited = [False] * (n + 1)
    queue = [t]
    visited[t] = True
    infected_count = 0
    
    while queue:
        current = queue.pop(0)
        
        # 현재 컴퓨터와 연결된 모든 컴퓨터 확인
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                infected_count += 1
    
    print(infected_count)

# 문제 7: NBO로봇 (최단 경로 - 다이나믹 프로그래밍)
def problem7():
    n = int(input())
    
    # 에너지 소모량 격자 입력
    grid = []
    for _ in range(n):
        row = list(map(int, input().split()))
        grid.append(row)
    
    # 최소 비용 계산을 위한 DP 테이블
    dp = [[float('inf')] * n for _ in range(n)]
    dp[0][0] = grid[0][0]  # 시작점
    
    # 첫 번째 행 (오른쪽으로만 이동)
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + grid[0][j]
    
    # 첫 번째 열 (아래로만 이동)
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    
    # 나머지 칸들 (위에서 오거나 왼쪽에서 오거나)
    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    
    # 목표지점까지의 최소 비용
    print(dp[n-1][n-1])

# 문제 8: 블록의 최소면적
def problem8():
    n, k = map(int, input().split())
    
    blocks = []
    for _ in range(n):
        w, h = map(int, input().split())
        blocks.append((w, h))
    
    min_area = float('inf')
    
    # k개 블록을 선택하는 모든 조합 확인
    # 비트마스크를 사용하여 조합 생성
    for mask in range(1, 1 << n):
        # 선택된 블록 개수 확인
        selected_count = 0
        selected_blocks = []
        
        for i in range(n):
            if mask & (1 << i):
                selected_count += 1
                selected_blocks.append(blocks[i])
        
        # k개가 아니면 건너뛰기
        if selected_count != k:
            continue
        
        # 선택된 블록들로 만들 수 있는 면적 계산
        total_width = sum(block[0] for block in selected_blocks)
        max_height = max(block[1] for block in selected_blocks)
        area = total_width * max_height
        
        min_area = min(min_area, area)
    
    print(min_area)

# 효율적인 문제 8 버전 (조합이 너무 많을 경우를 위한 대안)
def problem8_efficient():
    n, k = map(int, input().split())
    
    blocks = []
    for _ in range(n):
        w, h = map(int, input().split())
        blocks.append((w, h))
    
    min_area = float('inf')
    
    # 재귀적으로 k개 선택하는 모든 조합 확인
    def find_min_area(start, selected, remaining):
        nonlocal min_area
        
        if remaining == 0:
            # k개를 모두 선택했을 때 면적 계산
            total_width = sum(blocks[i][0] for i in selected)
            max_height = max(blocks[i][1] for i in selected)
            area = total_width * max_height
            min_area = min(min_area, area)
            return
        
        if start >= n:
            return
        
        # 현재 블록을 선택하는 경우
        selected.append(start)
        find_min_area(start + 1, selected, remaining - 1)
        selected.pop()
        
        # 현재 블록을 선택하지 않는 경우
        find_min_area(start + 1, selected, remaining)
    
    find_min_area(0, [], k)
    print(min_area)

# 실행 부분 (각 문제별로 주석 해제하여 실행)
if __name__ == "__main__":
    # problem1()  # 문제 1: 총점과 평균점수
    # problem2()  # 문제 2: 토끼의 번식
    # problem3()  # 문제 3: 진수 변환기
    # problem4()  # 문제 4: 문장 암호화
    # problem5()  # 문제 5: 증가하는 난이도
    # problem6()  # 문제 6: 바이러스 전파
    # problem7()  # 문제 7: NBO로봇
    problem8()  # 문제 8: 블록의 최소면적
    pass
