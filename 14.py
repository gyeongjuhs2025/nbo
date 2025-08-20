# 제14회 전국상업경진대회 비즈니스 프로그래밍 문제 풀이

# 문제 1: 진수 변환
def problem1():
    n = int(input())  # 10진수 숫자
    k = int(input())  # 변환할 진수
    
    # k진수로 변환
    result = ""
    temp = n
    
    if temp == 0:
        result = "0"
    else:
        while temp > 0:
            remainder = temp % k
            result = str(remainder) + result
            temp = temp // k
    
    print(result)

# 문제 2: 비밀스러운 숫자
def problem2():
    # 키보드로 입력 받기 (안내 메시지 없이)
    word = input().strip()
    
    # 1단계: 각 문자를 ASCII 코드로 변환 후 8진수로 변환
    octal_string = ""
    for char in word:
        ascii_code = ord(char)
        octal_code = oct(ascii_code)[2:]  # oct()는 '0o'를 앞에 붙이므로 [2:]로 제거
        octal_string += octal_code
    
    # 2단계: 런 렝스 부호화 (Run-length encoding)
    if not octal_string:
        print("")
        return
    
    result = ""
    current_char = octal_string[0]
    count = 1
    
    for i in range(1, len(octal_string)):
        if octal_string[i] == current_char:
            count += 1
        else:
            result += current_char + str(count)
            current_char = octal_string[i]
            count = 1
    
    # 마지막 문자 처리
    result += current_char + str(count)
    
    # 비밀스러운 숫자 출력
    print(result)

# 문제 3: SNS 비밀번호
def problem3():
    password = input().strip()
    
    # 각 조건 체크
    has_upper = False
    has_lower = False
    has_special = False
    has_number = False
    
    special_chars = "!@#$%^&*()_+"
    
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_number = True
        elif char in special_chars:
            has_special = True
    
    # 부족한 조건들 세기
    missing_count = 0
    missing_type = ""
    
    if not has_upper:
        missing_count += 1
        missing_type = "need uppercase"
    if not has_lower:
        missing_count += 1
        missing_type = "need lowercase"
    if not has_special:
        missing_count += 1
        missing_type = "need special symbols"
    if not has_number:
        missing_count += 1
        missing_type = "need number"
    
    # 결과 출력
    if missing_count == 0:
        print("accept")
    elif missing_count == 1:
        print(missing_type)
    else:
        print("check your password")

# 문제 4: 공약수의 합
def problem4():
    a, b = map(int, input().split())
    
    # 최대공약수 구하기 (유클리드 호제법)
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    
    gcd_value = gcd(a, b)
    
    # 최대공약수의 약수들을 구해서 합산
    divisor_sum = 0
    for i in range(1, gcd_value + 1):
        if gcd_value % i == 0:
            divisor_sum += i
    
    print(divisor_sum)

# 문제 5: 삼다도 제주도
def problem5():
    n = int(input())
    grid = []
    
    for _ in range(n):
        row = input().strip()
        grid.append(row)
    
    target_words = ["wind", "stone", "woman"]
    total_count = 0
    
    # 각 단어를 찾기
    for word in target_words:
        word_len = len(word)
        
        # 가로 방향 (왼쪽에서 오른쪽)
        for i in range(n):
            for j in range(n - word_len + 1):
                found_word = ""
                for k in range(word_len):
                    found_word += grid[i][j + k]
                if found_word == word:
                    total_count += 1
        
        # 세로 방향 (위에서 아래)
        for i in range(n - word_len + 1):
            for j in range(n):
                found_word = ""
                for k in range(word_len):
                    found_word += grid[i + k][j]
                if found_word == word:
                    total_count += 1
        
        # 대각선 방향 (왼쪽 위에서 오른쪽 아래)
        for i in range(n - word_len + 1):
            for j in range(n - word_len + 1):
                found_word = ""
                for k in range(word_len):
                    found_word += grid[i + k][j + k]
                if found_word == word:
                    total_count += 1
    
    print(total_count)

# 문제 6: 가장 큰 정사각형
def problem6():
    n, m = map(int, input().split())
    grid = []
    
    for _ in range(n):
        row = input().strip()
        grid.append(row)
    
    # 동적 프로그래밍으로 최대 정사각형 찾기
    dp = [[0] * m for _ in range(n)]
    max_size = 0
    
    # 첫 번째 행과 열 초기화
    for i in range(n):
        if grid[i][0] == '1':
            dp[i][0] = 1
            max_size = 1
    
    for j in range(m):
        if grid[0][j] == '1':
            dp[0][j] = 1
            max_size = 1
    
    # 나머지 칸들 계산
    for i in range(1, n):
        for j in range(1, m):
            if grid[i][j] == '1':
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                max_size = max(max_size, dp[i][j])
    
    # 넓이 = 한 변의 길이의 제곱
    print(max_size * max_size)

# 문제 7: 달 탐사 전초기지 (플로이드-워셜)
def problem7():
    n, m = map(int, input().split())
    
    # 무한대를 표현하는 큰 수
    INF = float('inf')
    
    # 거리 배열 초기화
    dist = [[INF] * (n + 1) for _ in range(n + 1)]
    
    # 자기 자신으로의 거리는 0
    for i in range(1, n + 1):
        dist[i][i] = 0
    
    # 간선 정보 입력
    for _ in range(m):
        a, b, c = map(int, input().split())
        dist[a][b] = c
    
    # 플로이드-워셜 알고리즘
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if dist[i][k] != INF and dist[k][j] != INF:
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    # 쿼리 처리
    z = int(input())
    for _ in range(z):
        x, y = map(int, input().split())
        if dist[x][y] == INF:
            print("INF")
        else:
            print(dist[x][y])

# 문제 8: 새로운 사격 종목
def problem8():
    n, t = map(int, input().split())
    scores = []
    
    for _ in range(n):
        score = int(input())
        scores.append(score)
    
    # 동적 프로그래밍으로 해결 (같은 점수를 여러 번 사용 가능)
    # dp[i] = i점을 만들 수 있는지 여부
    dp = [False] * (t + 1)
    dp[0] = True  # 0점은 항상 가능 (아무것도 맞히지 않음)
    
    # 각 점수에 대해 DP 업데이트 (같은 점수 여러 번 사용 가능)
    for i in range(1, t + 1):
        for score in scores:
            if i >= score and dp[i - score]:
                dp[i] = True
                break
    
    # 목표점수 이하에서 만들 수 있는 최대점수 찾기
    max_score = 0
    for i in range(t + 1):
        if dp[i]:
            max_score = i
    
    print(max_score)

# 실행 부분 (각 문제별로 주석 해제하여 실행)
if __name__ == "__main__":
    # problem1()  # 문제 1: 진수 변환
    problem2()  # 문제 2: 비밀스러운 숫자
    # problem3()  # 문제 3: SNS 비밀번호
    # problem4()  # 문제 4: 공약수의 합
    # problem5()  # 문제 5: 삼다도 제주도
    # problem6()  # 문제 6: 가장 큰 정사각형
    # problem7()  # 문제 7: 달 탐사 전초기지
    # problem8()  # 문제 8: 새로운 사격 종목
    pass