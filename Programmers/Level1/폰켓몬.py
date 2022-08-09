# 해시 | https://school.programmers.co.kr/learn/courses/30/lessons/1845

# Solution_1
def solution(nums):
    return min(len(nums) // 2, len(set(nums)))


# test case
print(solution([3,1,2,3]))      # 2
print(solution([3,3,3,2,2,4]))  # 3
print(solution([3,3,3,2,2,2]))  # 2