# Implementation

# Solution_1
hour = int(input())
three = [3, 13, 23, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 43, 53]
cnt = 0

for i in range(hour+1):
    for j in range(60):
        for k in range(60):
            if (i in three) or (j in three) or (k in three):
                cnt += 1
                
print(cnt)


# Soluton_2 -> 매 시각을 문자열로 바꾼 다음 문자열에 '3'이 포함됐는지 검사
# H를 입력받기
h = int(input())

count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                a = str(i)+str(j)+str(k)
                count += 1
        
print(count)



# test_case1
# 입력 : 5
# 출력 : 11475