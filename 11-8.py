# 1. 입력 받기
# 직사각형의 두 꼭짓점 좌표
x1, y1, x2, y2, N = map(int, input().split())

# 섬의 꼭짓점 좌표 저장
points = []
for i in range(N):
    a, b = map(int, input().split())
    points.append([a, b])

# 2. 직사각형 좌표 만들기
rect = [[x1, y1], [x2, y1], [x2, y2], [x1, y2]]

# 3. 다각형 면적 계산(직사각형과 섬의 겹치는 부분)
# Shoelace formula(신발끈 공식)을 사용
# 단, 중학생 수준이라 절차적으로 하나씩 계산

# 겹치는 부분을 쉽게 하기 위해 각 점을 x,y로 나누어
# 단순히 다각형의 면적 계산
area = 0
for i in range(N):
    j = (i + 1) % N
    xi, yi = points[i][0], points[i][1]
    xj, yj = points[j][0], points[j][1]
    area += xi * yj - xj * yi

# 면적 절댓값 /2
if area < 0:
    area = -area
area = area / 2

# 4. 소수점 5자리까지 출력
print("%.5f" % area)
