# Greedy | https://codeup.kr/problemsetsol.php

# Solution_1
money = int(input())
cnt = 0
change_money = [50000, 10000, 5000, 1000,  500, 100, 50, 10]

for i in change_money:
    if money == 0:
        break
    cnt += (money // i)
    money %= i

print(cnt)



# test_case1
# 입력 : 54520
# 출력 : 8