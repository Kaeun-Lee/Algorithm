# Recursion_Function | https://codeup.kr/problem.php?id=1902

# Solution_1
n = int(input())

def recursion(n):
    if n < 1:
        return 
    
    print(n)
    n -= 1
    recursion(n)
    
recursion(n)


# Solution_2
n = int(input())

def recursive(num):
    print(num)
    if num > 1:
        recursive(num - 1)
    
recursive(n)



# test_case
# 입력 : 10
# 출력
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
