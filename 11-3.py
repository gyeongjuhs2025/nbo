import time

# 게임판 크기와 적기 수 입력
W, H, N = map(int, input("게임판 W H N 입력: ").split())

# 적기 정보 입력
enemies = []
for i in range(N):
    pos_str, moves = input(f"적기 {i+1} 정보 입력 (x,y 계획): ").split()
    x, y = map(int, pos_str.split(','))
    enemies.append([x, y, moves])

# 방향별 좌표 변화
directions = {'L': (-1, 0), 'R': (1, 0), 'U': (0, -1), 'D': (0, 1)}

# 단계별 시각화
def print_board(enemies_positions):
    board = [['.' for _ in range(W)] for _ in range(H)]
    for idx, (x, y) in enumerate(enemies_positions):
        # 좌표 변환: (1,1) → (0,0)
        board[y-1][x-1] = chr(65 + idx)  # A, B, C...
    # 세로 방향 출력 (위쪽이 1)
    for row in board:
        print(' '.join(row))
    print('\n' + '-'*(2*W-1) + '\n')  # 구분선

# 최대 이동 횟수 확인
max_moves = max(len(enemy[2]) for enemy in enemies)

# 적기별 현재 좌표
current_positions = [(enemy[0], enemy[1]) for enemy in enemies]

# 단계별 이동 시뮬레이션
for step in range(max_moves):
    for idx, (x, y, moves) in enumerate(enemies):
        if step < len(moves):
            dx, dy = directions[moves[step]]
            new_x = x + dx
            new_y = y + dy
            # 게임판 안이면 이동
            if 1 <= new_x <= W:
                x = new_x
            if 1 <= new_y <= H:
                y = new_y
            current_positions[idx] = (x, y)
            enemies[idx][0], enemies[idx][1] = x, y
    print(f"Step {step+1}:")
    print_board(current_positions)
    time.sleep(0.5)  # 0.5초 딜레이, 필요 없으면 제거

# 최종 위치 출력
print("최종 위치:")
for pos in current_positions:
    print(f"{pos[0]},{pos[1]}")
