# 코딩테스트 입문


# My Solution 1
def solution(my_string, n):
    return "".join(char * n for char in my_string)


# My Solution 2
def solution(my_string, n):
    return "".join(map(lambda x: x * n, my_string))
