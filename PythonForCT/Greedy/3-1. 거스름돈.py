# Greedy

# Solution_1
price = 1260
cnt = 0

coin = [500, 100, 50, 10]

for i in coin:
    if price % i != 0:
        cnt += price//i
        price = price % i 
    else:
        cnt += price//i
        
print(cnt)  # 6


# Solution_2 -> 더 간단한 풀이
n = 1260
count = 0

# 큰 단위의 화폐부터 차례대로 확인
coin_types = [500, 100, 50, 10]  # 시간 복잡도 O(4)

for coin in coin_types:
    count += n // coin           # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin
    
print(count)