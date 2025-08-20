# 문제 1: 소득세 계산
def problem1():
    # 입력 받기
    income, deduction, tax_reduction = map(int, input().split())
    
    # 과세표준 계산
    taxable = income - deduction
    if taxable <= 0:
        print(0)
        return
    
    # 소득세 계산
    tax = 0
    if taxable <= 12000000:
        tax = taxable * 0.06
    elif taxable <= 46000000:
        tax = 12000000 * 0.06 + (taxable - 12000000) * 0.15
    elif taxable <= 88000000:
        tax = 12000000 * 0.06 + 34000000 * 0.15 + (taxable - 46000000) * 0.24
    elif taxable <= 150000000:
        tax = 12000000 * 0.06 + 34000000 * 0.15 + 42000000 * 0.24 + (taxable - 88000000) * 0.35
    elif taxable <= 300000000:
        tax = 12000000 * 0.06 + 34000000 * 0.15 + 42000000 * 0.24 + 62000000 * 0.35 + (taxable - 150000000) * 0.38
    elif taxable <= 500000000:
        tax = 12000000 * 0.06 + 34000000 * 0.15 + 42000000 * 0.24 + 62000000 * 0.35 + 150000000 * 0.38 + (taxable - 300000000) * 0.40
    else:
        tax = 12000000 * 0.06 + 34000000 * 0.15 + 42000000 * 0.24 + 62000000 * 0.35 + 150000000 * 0.38 + 200000000 * 0.40 + (taxable - 500000000) * 0.42
    
    # 세액감면 적용
    final_tax = max(0, tax - tax_reduction)
    
    # 10원 미만 절사
    final_tax = int(final_tax // 10) * 10
    
    print(int(final_tax))

# 문제 2: 신용카드 유효성 검증
def problem2():
    parts = input().split()
    
    # 입력 검증
    if len(parts) != 4:
        print(-1)
        return
    
    # 각 부분이 4자리 숫자인지 확인
    card_number = ""
    for part in parts:
        if len(part) != 4 or not part.isdigit():
            print(-1)
            return
        card_number += part
    
    # 브랜드 확인
    first_two = card_number[:2]
    first_four = card_number[:4]
    
    brand = ""
    if first_two == "35":
        brand = "JCB"
    elif first_two == "37":
        brand = "American Express"
    elif card_number[0] == "4":
        brand = "VISA"
    elif "51" <= first_two <= "55":
        brand = "MasterCard"
    elif first_two == "65":
        brand = "BC Global"
    elif card_number[0] == "9":
        brand = "Local"
    else:
        print(-2)
        return
    
    # 유효성 검증 (Luhn 알고리즘)
    total = 0
    for i in range(16):
        digit = int(card_number[i])
        # 오른쪽부터 1번째(인덱스 15)가 홀수 번째, 2번째(인덱스 14)가 짝수 번째
        if (15 - i) % 2 == 1:  # 짝수 번째 (오른쪽부터)
            digit *= 2
            if digit >= 10:
                digit = digit // 10 + digit % 10
        total += digit
    
    valid = "O" if total % 10 == 0 else "X"
    print(f"{brand} {total} {valid}")

# 문제 3: 슈팅 게임 적기 이동
def problem3():
    W, H, N = map(int, input().split())
    
    for _ in range(N):
        parts = input().split()
        start_pos = parts[0]
        moves = parts[1]
        
        # 시작 위치 파싱
        x, y = map(int, start_pos.split(','))
        
        # 이동 처리
        for move in moves:
            new_x, new_y = x, y
            if move == 'L':
                new_x = x - 1
            elif move == 'R':
                new_x = x + 1
            elif move == 'U':
                new_y = y - 1
            elif move == 'D':
                new_y = y + 1
            
            # 경계 검사
            if 1 <= new_x <= W and 1 <= new_y <= H:
                x, y = new_x, new_y
        
        print(f"{x},{y}")

# 문제 4: 완전순열 (Derangement)
def problem4():
    n = int(input())
    
    if n < 1 or n > 15:
        print("오류")
        return
    
    # 완전순열 개수 계산 (점화식 사용)
    if n == 1:
        print(0)
    elif n == 2:
        print(1)
    else:
        # D(n) = (n-1) * (D(n-1) + D(n-2))
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 0
        dp[2] = 1
        
        for i in range(3, n + 1):
            dp[i] = (i - 1) * (dp[i - 1] + dp[i - 2])
        
        print(dp[n])

# 문제 5: 아날로그 시계
def problem5():
    import math
    
    time_str = input()
    h, m, s = map(int, time_str.split(':'))
    
    # 각도 계산 (12시 방향을 0도로 하여 시계방향)
    # 초침: 1초당 6도
    second_angle = s * 6
    
    # 분침: 1분당 6도
    minute_angle = m * 6
    
    # 시침: 1분당 0.5도
    hour_angle = (h * 60 + m) * 0.5
    
    # 좌표 계산 (수학적 각도로 변환: 시계방향 -> 반시계방향, 12시 -> 3시 기준)
    def get_coordinates(angle, length):
        # 시계 각도를 수학 각도로 변환
        math_angle = math.radians(90 - angle)
        x = length * math.cos(math_angle)
        y = length * math.sin(math_angle)
        return round(x), round(y)
    
    # 각 바늘의 좌표 계산
    hour_x, hour_y = get_coordinates(hour_angle, 120)
    minute_x, minute_y = get_coordinates(minute_angle, 200)
    second_x, second_y = get_coordinates(second_angle, 180)
    
    print(f"({hour_x}, {hour_y})")
    print(f"({minute_x}, {minute_y})")
    print(f"({second_x}, {second_y})")

# 문제 6: 퀘스트 진행 시간
def problem6():
    N, M = map(int, input().split())
    
    # 퀘스트 정보 저장
    quest_time = [0] * (N + 1)
    prerequisites = [[] for _ in range(N + 1)]
    
    for i in range(1, N + 1):
        line = list(map(int, input().split()))
        quest_time[i] = line[0]
        for j in range(1, len(line)):
            if line[j] == -1:
                break
            prerequisites[i].append(line[j])
    
    # 각 퀘스트의 최소 완료 시간 계산
    completion_time = [0] * (N + 1)
    
    def calculate_time(quest):
        if completion_time[quest] != 0:
            return completion_time[quest]
        
        max_prereq_time = 0
        for prereq in prerequisites[quest]:
            max_prereq_time = max(max_prereq_time, calculate_time(prereq))
        
        completion_time[quest] = max_prereq_time + quest_time[quest]
        return completion_time[quest]
    
    print(calculate_time(M))

# 문제 7: 쿼드트리 압축
def problem7():
    N = int(input())
    grid = []
    for i in range(N):
        row = list(map(int, input().split()))
        grid.append(row)
    
    def is_uniform(x, y, size):
        """영역의 모든 값이 같은지 확인"""
        first_value = grid[x][y]
        for i in range(x, x + size):
            for j in range(y, y + size):
                if grid[i][j] != first_value:
                    return False
        return True
    
    def make_quadtree(x, y, size):
        """쿼드트리 생성"""
        if size == 1:
            # 1x1 크기일 때
            value = grid[x][y]
            if value == 0:
                return "N"
            else:
                # 1이면 D + 4개의 N (가상 하위 노드)
                return "DNNNN"
        
        if is_uniform(x, y, size):
            # 모든 값이 같으면 분할하지 않음
            value = grid[x][y]
            if value == 0:
                return "N"
            else:
                return "D"
        else:
            # 값이 다르면 분할
            half = size // 2
            result = "D"
            
            # 4개 영역을 순서대로 처리 (좌상, 우상, 좌하, 우하)
            result += make_quadtree(x, y, half)  # 좌상
            result += make_quadtree(x, y + half, half)  # 우상
            result += make_quadtree(x + half, y, half)  # 좌하
            result += make_quadtree(x + half, y + half, half)  # 우하
            
            return result
    
    # 쿼드트리 코드 생성
    code = make_quadtree(0, 0, N)
    
    # 압축 최적화
    def find_best_compression(text):
        best_length = len(text)
        
        for unit in range(1, len(text) + 1):
            if len(text) % unit == 0:
                compressed = ""
                i = 0
                
                while i < len(text):
                    pattern = text[i:i + unit]
                    count = 1
                    
                    j = i + unit
                    while j <= len(text) - unit and text[j:j + unit] == pattern:
                        count += 1
                        j += unit
                    
                    if count == 1:
                        compressed += pattern
                    else:
                        compressed += str(count) + pattern
                    
                    i = j
                
                best_length = min(best_length, len(compressed))
        
        return best_length
    
    best_compressed_length = find_best_compression(code)
    print(f"{code} {best_compressed_length}")

# 문제 8: 다각형과 직사각형 교집합
def problem8():
    line = list(map(int, input().split()))
    x1, y1, x2, y2, N = line
    
    polygon = []
    for _ in range(N):
        x, y = map(int, input().split())
        polygon.append((x, y))
    
    # Sutherland-Hodgman 클리핑 알고리즘을 사용하여 교집합 구하기
    def clip_polygon_with_rectangle(polygon, x1, y1, x2, y2):
        def is_inside(point, edge):
            x, y = point
            if edge == 'left':
                return x >= x1
            elif edge == 'right':
                return x <= x2
            elif edge == 'bottom':
                return y >= y1
            elif edge == 'top':
                return y <= y2
        
        def get_intersection(p1, p2, edge):
            x1_p, y1_p = p1
            x2_p, y2_p = p2
            
            if edge == 'left':
                if x2_p == x1_p:
                    return None
                t = (x1 - x1_p) / (x2_p - x1_p)
                return (x1, y1_p + t * (y2_p - y1_p))
            elif edge == 'right':
                if x2_p == x1_p:
                    return None
                t = (x2 - x1_p) / (x2_p - x1_p)
                return (x2, y1_p + t * (y2_p - y1_p))
            elif edge == 'bottom':
                if y2_p == y1_p:
                    return None
                t = (y1 - y1_p) / (y2_p - y1_p)
                return (x1_p + t * (x2_p - x1_p), y1)
            elif edge == 'top':
                if y2_p == y1_p:
                    return None
                t = (y2 - y1_p) / (y2_p - y1_p)
                return (x1_p + t * (x2_p - x1_p), y2)
        
        clipped = polygon[:]
        
        for edge in ['left', 'right', 'bottom', 'top']:
            if not clipped:
                break
                
            new_clipped = []
            if len(clipped) > 0:
                prev_point = clipped[-1]
                
                for curr_point in clipped:
                    if is_inside(curr_point, edge):
                        if not is_inside(prev_point, edge):
                            intersection = get_intersection(prev_point, curr_point, edge)
                            if intersection:
                                new_clipped.append(intersection)
                        new_clipped.append(curr_point)
                    elif is_inside(prev_point, edge):
                        intersection = get_intersection(prev_point, curr_point, edge)
                        if intersection:
                            new_clipped.append(intersection)
                    prev_point = curr_point
            
            clipped = new_clipped
        
        return clipped
    
    # 교집합 다각형 구하기
    clipped_polygon = clip_polygon_with_rectangle(polygon, x1, y1, x2, y2)
    
    # 다각형 넓이 계산 (Shoelace formula)
    def polygon_area(vertices):
        if len(vertices) < 3:
            return 0.0
        
        area = 0.0
        n = len(vertices)
        for i in range(n):
            j = (i + 1) % n
            area += vertices[i][0] * vertices[j][1]
            area -= vertices[j][0] * vertices[i][1]
        
        return abs(area) / 2.0
    
    area = polygon_area(clipped_polygon)
    print(f"{area:.5f}")

# 실행 부분 (각 문제별로 주석 해제하여 실행)
if __name__ == "__main__":
    # problem1()  # 문제 1
    # problem2()  # 문제 2
    # problem3()  # 문제 3
    # problem4()  # 문제 4
    # problem5()  # 문제 5
    # problem6()  # 문제 6
    problem7()  # 문제 7 ### 미결
    # problem8()  # 문제 8
    pass