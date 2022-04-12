# Recursion_Function | https://codeup.kr/problem.php?id=1915

# Solution_1
n = int(input())

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(n))



# test_case
# 입력 : 7
# 출력 : 13