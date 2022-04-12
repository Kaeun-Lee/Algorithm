# Stack | https://codeup.kr/problem.php?id=3117

# Solution_1
total = int(input())
lst = []
for i in range(total):
    number = int(input())
    if number != 0:
        lst.append(number)
    else:
        lst.pop()  # pop은 복잡도가 올라감
print(sum(lst))


# Solution_2 -> del 사용, 조금 빠름
total = int(input())
lst = []
for i in range(total):
    number = int(input())
    if number != 0:
        lst.append(number)
    else:
        if lst:
            del lst[-1]
print(sum(lst))



# test_case1
# < 입력 >
# 10
# 1
# 3
# 5    
# 4  
# 0  
# 0  
# 7  
# 0  
# 0  
# 6

# 출력 : 7  