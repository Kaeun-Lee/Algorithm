# Greedy | https://codeup.kr/problem.php?id=2001

# Solution_1
price = []
for i in range(5):
    price.append(int(input()))

pasta = price[:3]
juice = price[3:]
min_price = [((i+j) + (i+j)*0.1) for i in pasta for j in juice]

print(round(min(min_price),1))  # 987.8


# Solution_2
price = []
for i in range(5):
    price.append(int(input()))
    
pasta = price[:3]
juice = price[3:]
min_price = (min(pasta) + min(juice)) * 1.1  # 메뉴 중 최솟값으로 대금 계산

print(round(min_price,1))



# 입력
# 800
# 700
# 900
# 198
# 330
