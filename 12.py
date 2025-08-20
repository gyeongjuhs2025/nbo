# 제12회 전국상업경진대회 비즈니스 프로그래밍 문제 풀이

# 문제 1: 하노이 탑 (최소 이동 횟수)
def problem1():
    n = int(input())
    
    # 하노이 탑 공식: 2^n - 1
    result = (2 ** n) - 1
    print(result)

# 문제 2: 읽고 말하기 수열 (개미 수열)
def problem2():
    # 한 줄에 여러 숫자를 입력받고, 마지막 0 제거
    line = input().split()
    sequence = []
    
    for num_str in line:
        num = int(num_str)
        if num == 0:
            break
        sequence.append(num)
    
    # 다음 단계 수열 만들기
    result = []
    i = 0
    
    while i < len(sequence):
        current_num = sequence[i]
        count = 1
        
        # 같은 숫자가 몇 개 연속으로 나오는지 세기
        while i + count < len(sequence) and sequence[i + count] == current_num:
            count += 1
        
        # 개수와 숫자를 결과에 추가
        result.append(count)
        result.append(current_num)
        
        # 다음 위치로 이동
        i += count
    
    # 결과 출력
    for j in range(len(result)):
        if j == len(result) - 1:
            print(result[j])
        else:
            print(result[j], end=' ')

# 문제 3: 포켓몬 카드 케이스
def problem3():
    n = int(input())  # 카드 개수
    price1, capacity1 = map(int, input().split())  # 첫 번째 케이스
    price2, capacity2 = map(int, input().split())  # 두 번째 케이스
    
    min_cost = float('inf')
    best_case1 = 0
    best_case2 = 0
    found = False
    
    # 첫 번째 케이스를 0개부터 최대 필요한 개수까지 시도
    max_case1 = (n // capacity1) + 1
    
    for case1_count in range(max_case1 + 1):
        remaining_cards = n - (case1_count * capacity1)
        
        if remaining_cards < 0:
            continue
        
        # 남은 카드가 두 번째 케이스로 정확히 나누어떨어지는지 확인
        if remaining_cards % capacity2 == 0:
            case2_count = remaining_cards // capacity2
            total_cost = case1_count * price1 + case2_count * price2
            
            if total_cost < min_cost:
                min_cost = total_cost
                best_case1 = case1_count
                best_case2 = case2_count
                found = True
    
    if found:
        print(best_case1, best_case2)
    else:
        print("Not Full")

# 문제 4: 회문(팰린드롬) 찾기
def problem4():
    text = input().strip()
    
    # 단어들을 공백으로 분리
    words = text.split()
    palindromes = []
    
    # 알파벳과 숫자만 남기는 함수 (대소문자 구분 없이)
    def clean_text(s):
        result = ""
        for char in s:
            if char.isalnum():
                result += char.lower()
        return result
    
    # 회문인지 확인하는 함수
    def is_palindrome(s):
        cleaned = clean_text(s)
        if len(cleaned) <= 1:
            return False
        return cleaned == cleaned[::-1]
    
    # 단일 단어 회문 찾기
    for word in words:
        if is_palindrome(word):
            palindromes.append(word)
    
    # 연속된 단어들로 이루어진 회문 찾기
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            combined = ""
            original_combined = ""
            for k in range(i, j + 1):
                combined += clean_text(words[k])
                if k == i:
                    original_combined = words[k]
                else:
                    original_combined += " " + words[k]
            
            if len(combined) > 1 and combined == combined[::-1]:
                # 이미 찾은 회문의 부분이 아닌지 확인
                is_subset = False
                for existing in palindromes:
                    if original_combined in existing and original_combined != existing:
                        is_subset = True
                        break
                
                if not is_subset:
                    palindromes.append(original_combined)
    
    # 결과 출력
    for palindrome in palindromes:
        print(palindrome)

# 문제 5: 채권 투자 수익률 계산
def problem5():
    issue_price = int(input())  # 발행가격
    interest_rate = float(input())  # 이자율
    payment_period = int(input())  # 이자지급주기 (개월)
    remaining_months = int(input())  # 잔존만기 (개월)
    target_return = float(input())  # 목표수익률
    
    # 연간 이자 계산
    annual_interest = issue_price * interest_rate / 100
    
    # 각 지급 시기별 이자
    period_interest = annual_interest * payment_period / 12
    
    # 이자 지급 횟수 계산
    payment_count = remaining_months // payment_period
    
    # 총 이자 수익 (세전)
    total_interest_before_tax = period_interest * payment_count
    
    # 세금 계산 (15.4%)
    tax = int(total_interest_before_tax * 0.154)
    
    # 실제 이자 수익 (세후)
    net_interest = int(total_interest_before_tax) - tax
    
    # 보유기간 (년)
    holding_years = remaining_months / 12
    
    # 목표 수익률로부터 최대 매수가격 계산
    # 목표수익률 = (실제이자수익 + 매매차익) / 매수가격 / 보유기간
    # 매매차익 = 발행가격 - 매수가격
    # 목표수익률 = (실제이자수익 + 발행가격 - 매수가격) / 매수가격 / 보유기간
    
    # 이를 매수가격에 대해 정리하면:
    # 매수가격 = (실제이자수익 + 발행가격) / (1 + 목표수익률 * 보유기간)
    
    max_purchase_price = int((net_interest + issue_price) / (1 + target_return / 100 * holding_years))
    
    print(max_purchase_price)

# 문제 6: 고속도로 광고판 수익 최대화
def problem6():
    L = int(input())  # 고속도로 거리
    N = int(input())  # 광고판 개수
    positions = list(map(int, input().split()))  # 광고판 위치
    profits = list(map(int, input().split()))  # 각 광고판 수익
    K = int(input())  # 최소 거리
    
    # 동적 프로그래밍으로 해결
    # dp[i] = i번째 광고판까지 고려했을 때 최대 수익
    dp = [0] * N
    
    for i in range(N):
        # i번째 광고판을 선택하는 경우
        dp[i] = profits[i]
        
        # 이전 광고판들 중에서 거리 조건을 만족하는 것들과 합치기
        for j in range(i):
            if positions[i] - positions[j] > K:
                dp[i] = max(dp[i], dp[j] + profits[i])
    
    # 전체 최대값 찾기
    max_profit = max(dp)
    print(max_profit)

# 문제 7: 약통 서랍 약 분류
def problem7():
    M, N = map(int, input().split())  # 약통 개수, 약 개수
    capacities = list(map(int, input().split()))  # 각 약통 용량
    
    # 약 정보 저장
    medicines = []
    for i in range(N):
        line = list(map(int, input().split()))
        symptom_count = line[0]
        symptoms = line[1:symptom_count + 1]
        medicines.append((i + 1, symptoms))  # (약 번호, 증상 리스트)
    
    # 각 약통에 들어간 약들
    boxes = [[] for _ in range(M)]
    
    # 탐욕적으로 약 배정
    used = [False] * N
    
    # 각 약통별로 용량을 채우기
    for box_idx in range(M):
        target_symptom = box_idx + 1  # 약통 번호 = 증상 번호
        
        # 해당 증상에 효과가 있는 약들 중 번호가 작은 것부터 선택
        for medicine_num, symptoms in medicines:
            if not used[medicine_num - 1] and target_symptom in symptoms:
                if len(boxes[box_idx]) < capacities[box_idx]:
                    boxes[box_idx].append(medicine_num)
                    used[medicine_num - 1] = True
    
    # 모든 약통이 가득 찼는지 확인
    all_full = True
    for i in range(M):
        if len(boxes[i]) < capacities[i]:
            all_full = False
            break
    
    if not all_full:
        print("less pill")
    else:
        # 사용된 약 중 가장 큰 번호
        max_used = 0
        for i in range(N):
            if used[i]:
                max_used = max(max_used, i + 1)
        print(max_used)

# 문제 8: 3차원 틱택토
def problem8():
    # 3x3x3 게임판 입력받기
    board = []
    
    # 27개의 숫자를 입력받아 3차원 배열로 구성
    for z in range(3):
        layer = []
        for y in range(3):
            row = list(map(int, input().split()))
            layer.append(row)
        board.append(layer)
    
    winner = 0
    winning_positions = []
    
    # 모든 가능한 승리 조건 확인
    # 1. 같은 층에서의 가로/세로/대각선
    for z in range(3):
        # 가로
        for y in range(3):
            if board[z][y][0] == board[z][y][1] == board[z][y][2] != 0:
                winner = board[z][y][0]
                winning_positions = [(0, y, z), (1, y, z), (2, y, z)]
                break
        
        if winner != 0:
            break
            
        # 세로
        for x in range(3):
            if board[z][0][x] == board[z][1][x] == board[z][2][x] != 0:
                winner = board[z][0][x]
                winning_positions = [(x, 0, z), (x, 1, z), (x, 2, z)]
                break
        
        if winner != 0:
            break
            
        # 대각선
        if board[z][0][0] == board[z][1][1] == board[z][2][2] != 0:
            winner = board[z][0][0]
            winning_positions = [(0, 0, z), (1, 1, z), (2, 2, z)]
            break
        
        if board[z][0][2] == board[z][1][1] == board[z][2][0] != 0:
            winner = board[z][0][2]
            winning_positions = [(2, 0, z), (1, 1, z), (0, 2, z)]
            break
    
    # 2. 수직 (z축 방향)
    if winner == 0:
        for x in range(3):
            for y in range(3):
                if board[0][y][x] == board[1][y][x] == board[2][y][x] != 0:
                    winner = board[0][y][x]
                    winning_positions = [(x, y, 0), (x, y, 1), (x, y, 2)]
                    break
            if winner != 0:
                break
    
    # 3. 공간 대각선 (4개)
    if winner == 0:
        # (0,0,0) -> (1,1,1) -> (2,2,2)
        if board[0][0][0] == board[1][1][1] == board[2][2][2] != 0:
            winner = board[0][0][0]
            winning_positions = [(0, 0, 0), (1, 1, 1), (2, 2, 2)]
        # (0,0,2) -> (1,1,1) -> (2,2,0)
        elif board[2][0][0] == board[1][1][1] == board[0][2][2] != 0:
            winner = board[2][0][0]
            winning_positions = [(0, 0, 2), (1, 1, 1), (2, 2, 0)]
        # (0,2,0) -> (1,1,1) -> (2,0,2)
        elif board[0][2][0] == board[1][1][1] == board[2][0][2] != 0:
            winner = board[0][2][0]
            winning_positions = [(0, 2, 0), (1, 1, 1), (2, 0, 2)]
        # (2,0,0) -> (1,1,1) -> (0,2,2)
        elif board[0][0][2] == board[1][1][1] == board[2][2][0] != 0:
            winner = board[0][0][2]
            winning_positions = [(2, 0, 0), (1, 1, 1), (0, 2, 2)]
    
    # 4. 면 대각선들 (추가로 확인)
    if winner == 0:
        # x=0 면에서의 대각선
        if board[0][0][0] == board[1][1][0] == board[2][2][0] != 0:
            winner = board[0][0][0]
            winning_positions = [(0, 0, 0), (0, 1, 1), (0, 2, 2)]
        elif board[0][2][0] == board[1][1][0] == board[2][0][0] != 0:
            winner = board[0][2][0]
            winning_positions = [(0, 2, 0), (0, 1, 1), (0, 0, 2)]
        
        # x=1 면에서의 대각선
        elif board[0][0][1] == board[1][1][1] == board[2][2][1] != 0:
            winner = board[0][0][1]
            winning_positions = [(1, 0, 0), (1, 1, 1), (1, 2, 2)]
        elif board[0][2][1] == board[1][1][1] == board[2][0][1] != 0:
            winner = board[0][2][1]
            winning_positions = [(1, 2, 0), (1, 1, 1), (1, 0, 2)]
        
        # x=2 면에서의 대각선
        elif board[0][0][2] == board[1][1][2] == board[2][2][2] != 0:
            winner = board[0][0][2]
            winning_positions = [(2, 0, 0), (2, 1, 1), (2, 2, 2)]
        elif board[0][2][2] == board[1][1][2] == board[2][0][2] != 0:
            winner = board[0][2][2]
            winning_positions = [(2, 2, 0), (2, 1, 1), (2, 0, 2)]
    
    print(winner)
    
    if winner != 0:
        # 좌표 정렬 (x, y, z 순서로)
        winning_positions.sort()
        for pos in winning_positions:
            print(f"({pos[0]},{pos[1]},{pos[2]})")

# 실행 부분 (각 문제별로 주석 해제하여 실행)
if __name__ == "__main__":
    # problem1()  # 문제 1: 하노이 탑
    # problem2()  # 문제 2: 읽고 말하기 수열  
    # problem3()  # 문제 3: 포켓몬 카드 케이스
    # problem4()  # 문제 4: 회문 찾기
    # problem5()  # 문제 5: 채권 투자
    # problem6()  # 문제 6: 광고판 수익 최대화
    # problem7()  # 문제 7: 약통 서랍  # 미결 오답 1
    # problem8()  # 문제 8: 3차원 틱택토
    pass