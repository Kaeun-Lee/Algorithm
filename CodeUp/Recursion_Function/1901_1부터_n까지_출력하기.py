# Recursion_Function | https://codeup.kr/problem.php?id=1901

# Solution_1
n = int(input())

def recursion(n):
    if n > 1:
        recursion(n-1)
    print(n)
    
recursion(n)
    
    

# test_case
# 입력 : 10
# 출력
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10