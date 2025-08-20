import math

# 입력 받기
time_str = input("시간 입력 (H:M:S): ")
H, M, S = map(int, time_str.split(":"))

# 시각 처리
H = H % 12  # 12시를 0시로 변환

# 각도 계산 (시계 방향, 0°가 위쪽)
theta_sec = 6 * S
theta_min = 6 * M
theta_hour = 30 * H + 0.5 * M

# 라디안으로 변환
rad_sec = math.radians(theta_sec)
rad_min = math.radians(theta_min)
rad_hour = math.radians(theta_hour)

# 바늘 길이
L_sec = 180
L_min = 200
L_hour = 120

# 좌표 계산 (x, y)
x_sec = round(L_sec * math.sin(rad_sec))
y_sec = round(-L_sec * math.cos(rad_sec))

x_min = round(L_min * math.sin(rad_min))
y_min = round(-L_min * math.cos(rad_min))

x_hour = round(L_hour * math.sin(rad_hour))
y_hour = round(-L_hour * math.cos(rad_hour))

print(f"({x_hour}, {y_hour})")  # 시침
print(f"({x_min}, {y_min})")    # 분침
print(f"({x_sec}, {y_sec})")    # 초침
