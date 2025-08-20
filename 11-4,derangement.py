# 사람 수 입력
n = int(input("사람 수 입력: "))

# 입력 범위 체크
if n < 1 or n > 20:
    print("오류")
else:
    # D[n] : 아무도 자기 가방을 받지 않는 경우의 수
    D = [0]*(n+1)  # D[0], D[1], D[2] → [0,0,0] #D 배열은 사람 수 i일 때 아무도 자기 가방을 받지 않는 경우의 수 저장
    
    # 초기값
    if n >= 1:
        D[1] = 0 # i명이 있을 때 아무도 자기 가방을 받지 않는 경우의 수, 1명만 있을 때, 가방을 섞으면? 한명은 자신 가방을 안 받는것은  불가능-> 경우의 수:0
    if n >= 2:
        D[2] = 1
    
    # 재귀 공식으로 계산
    for i in range(3, n+1):
        D[i] = (i-1)*(D[i-1] + D[i-2])
    
    # 결과 출력
    print(D[n])

# [완전순열](https://www.google.com/search?q=%EC%95%84%EB%AC%B4%EB%8F%84+%EC%9E%90%EA%B8%B0+%EA%B2%83%EC%9D%84+%EB%B0%9B%EC%A7%80+%EC%95%8A%EB%8A%94+%EC%88%9C%EC%97%B4%EC%9D%84+%EA%B3%A0%EC%A0%95%EC%A0%90+%EC%97%86%EB%8A%94+%EC%88%9C%EC%97%B4&oq=%EC%95%84%EB%AC%B4%EB%8F%84+%EC%9E%90%EA%B8%B0+%EA%B2%83%EC%9D%84+%EB%B0%9B%EC%A7%80+%EC%95%8A%EB%8A%94+%EC%88%9C%EC%97%B4%EC%9D%84+%EA%B3%A0%EC%A0%95%EC%A0%90+%EC%97%86%EB%8A%94+%EC%88%9C%EC%97%B4&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIKCAEQABiABBiiBDIKCAIQABiABBiiBDIHCAMQABjvBTIHCAQQABjvBTIKCAUQABiABBiiBNIBCDMxNjVqMGo3qAIIsAIB8QXHtB8veWBRKg&sourceid=chrome&ie=UTF-8#fpstate=ive&vld=cid:93e75dc4,vid:i-kD9dQDNOY,st:0)