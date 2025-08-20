# 1. 게임판 크기와 적기 수 입력
W, H, N = map(int, input().split())

# 2. 적기 정보 입력받기
enemies = []
for _ in range(N):
    pos_str, moves = input().split()
    x, y = map(int, pos_str.split(','))
    enemies.append([x, y, moves])

# 3. 이동 처리
for enemy in enemies:
    x, y, moves = enemy
    for move in moves:
        if move == 'L' and x > 1:  # 왼쪽 이동
            x -= 1
        elif move == 'R' and x < W:  # 오른쪽 이동
            x += 1
        elif move == 'U' and y > 1:  # 위로 이동
            y -= 1
        elif move == 'D' and y < H:  # 아래로 이동
            y += 1
    # 최종 좌표 출력
    print(f"{x},{y}")
