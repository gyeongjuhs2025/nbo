# 1) 카드번호 입력 (띄어쓰기로 구분)
parts = input().split()

# (1) 입력 형식 검사 : 4개 부분, 각 부분은 숫자 4자리
if len(parts) != 4:
    print(-1)
    exit()

for p in parts:
    if len(p) != 4 or not p.isdigit():
        print(-1)
        exit()

# 카드번호 합치기
card_num = "".join(parts)

# 2) 카드 브랜드 판별
brand = ""
first_two = int(card_num[0:2])
first_one = int(card_num[0])

if first_two == 35:
    brand = "JCB"
elif first_two == 37:
    brand = "American Express"
elif first_one == 4:
    brand = "VISA"
elif 51 <= first_two <= 55:
    brand = "MasterCard"
elif first_two == 65:
    brand = "BC Global"
elif first_one == 9:
    brand = "Local"
else:
    print(-2)
    exit()

# 3) Luhn 알고리즘으로 검증값 계산
total_sum = 0
position = 1  # 오른쪽에서부터 위치

for digit in card_num[::-1]:  # 뒤에서부터 하나씩
    num = int(digit)
    if position % 2 == 0:  # 짝수 번째 자리를 두배 한값= num
        num *= 2
        if num > 9:  # 18
            num = num // 10 + num % 10
    total_sum += num
    position += 1

# 4) 유효성 판정
valid_flag = "O" if total_sum % 10 == 0 else "X"

# 5) 출력 : 브랜드, 검증값, 유효여부
print(brand, total_sum, valid_flag)
