import math
import matplotlib.pyplot as plt

# 1. 입력 받기
time_str = input("시간 입력 (H:M:S): ")
H, M, S = map(int, time_str.split(":"))
H = H % 12  # 12시는 0시로 변환

# 2. 바늘 각도 계산
theta_sec = 6 * S
theta_min = 6 * M
theta_hour = 30 * H + 0.5 * M

# 라디안으로 변환
rad_sec = math.radians(theta_sec)
rad_min = math.radians(theta_min)
rad_hour = math.radians(theta_hour)

# 3. 바늘 길이
L_sec = 180
L_min = 200
L_hour = 120

# 4. 좌표 계산
x_sec = L_sec * math.sin(rad_sec)
y_sec = -L_sec * math.cos(rad_sec)

x_min = L_min * math.sin(rad_min)
y_min = -L_min * math.cos(rad_min)

x_hour = L_hour * math.sin(rad_hour)
y_hour = -L_hour * math.cos(rad_hour)

# 5. 좌표 출력 (반올림)
print(f"시침: ({round(x_hour)}, {round(y_hour)})")
print(f"분침: ({round(x_min)}, {round(y_min)})")
print(f"초침: ({round(x_sec)}, {round(y_sec)})")

# 6. 시계 그림 시각화
plt.figure(figsize=(6,6))
plt.plot([0, x_hour], [0, y_hour], color='blue', linewidth=6, label='시침')
plt.plot([0, x_min], [0, y_min], color='green', linewidth=4, label='분침')
plt.plot([0, x_sec], [0, y_sec], color='red', linewidth=2, label='초침')

# 시계판 원 그리기
circle = plt.Circle((0, 0), 220, color='black', fill=False, linewidth=2)
plt.gca().add_artist(circle)

# 축 설정
plt.xlim(-240, 240)
plt.ylim(-240, 240)
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.title(f"시각: {H}:{M}:{S}")
plt.legend()
plt.show()
