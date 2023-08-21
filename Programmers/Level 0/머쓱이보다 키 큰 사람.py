# 코딩테스트 입문


# My Solution
def solution(array, height):
    return sum(1 if i > height else 0 for i in array)


# My Solution Refactoring
def solution(array, height):
    # return sum(i for i in array if i > height)
    return sum(i > height for i in array)


# Another Solution -> sort() 사용. sort: O(nlogn), for문 : O(n)이므로 시간 복잡도는 더 안 좋음
def solution(array, height):
    array.append(height)
    array.sort(reverse=True)
    return array.index(height)
