# 소득액, 소득공제액, 세액감면액 입력받기
income, deduction, tax_credit = map(int, input("소득액 소득공제액 세액감면액을 입력하세요: ").split())

# 1) 과세표준 계산
tax_base = income - deduction
# print("과세표준:", tax_base, "원")

# 세금 계산 변수 초기화
tax = 0

# 2) 과세표준이 0 이하이면 세금 없음
if tax_base <= 0:
    print("과세표준이 0 이하이므로 세금이 없습니다.")
else:
    # 세율과 누진공제 적용
    if tax_base <= 12000000:
        tax = tax_base * 0.06 - 0
    elif tax_base <= 46000000:
        tax = tax_base * 0.15 - 1080000
    elif tax_base <= 88000000:
        tax = tax_base * 0.24 - 5220000
    elif tax_base <= 150000000:
        tax = tax_base * 0.35 - 14900000
    elif tax_base <= 300000000:
        tax = tax_base * 0.38 - 19400000
    elif tax_base <= 500000000:
        tax = tax_base * 0.40 - 25400000
    else:
        tax = tax_base * 0.42 - 35400000

# 3) 세액감면 적용
final_tax = tax - tax_credit

# 최종 소득세액은 0원 이상이어야 함
if final_tax < 0:
    final_tax = 0

print("최종 소득세액:", int(final_tax), "원")
