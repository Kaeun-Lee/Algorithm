# 연습문제 | https://school.programmers.co.kr/learn/courses/30/lessons/12935

# Solution_1
def solution(arr):
    del arr[arr.index(min(arr))]
    return arr or [-1]


# Solution_2 -> Solution_1 보다 살짝 더 빠름
def solution(arr):
    arr.remove(min(arr))
    return arr or [-1]
    

# test case
print(solution([4, 3, 2, 1]))  # [4, 3, 2]
print(solution([10]))          # [-1]