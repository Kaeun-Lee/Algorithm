# 스택/큐 | https://school.programmers.co.kr/learn/courses/30/lessons/12906

# Solution_1
# 리스트끼리 비교 or 리스트 슬라이싱 후 리스트끼리 비교하는 풀이보다 '값'끼리만 비교하는 코드가 훨씬 효율적
def solution(arr):
    result = []
    for i in range(len(arr) - 1):
        if arr[i] != arr[i + 1]:
            result.append(arr[i])
    result.append(arr[-1])
    return result


# Solution_2 -> 가장 빠름
def solution(arr):
    target = -1
    result = []
    for i in arr:
        if i != target:
            result.append(i)
            target = i
    return result


# Solution_3 -> array[-1:]로 마지막 값을 비교, Solution_1, 2 보다 조금 느림
# 리스트를 슬라이싱하면 리스트를 리턴함
def solution(arr):
    a = []
    for i in arr:
        if a[-1:] == [i]: continue  # array[-1]을 하면 empty array일 때 인덱싱 오류 발생
        a.append(i)
    return a


# Solution_4 -> 오른쪽에 인접한 원소 값과 비교해서 값이 다르면 리스트에 포함, 가장 느림
# (cf) 리스트 슬라이싱은 index 값이 범위를 초과해도 오류가 발생하지 않고 []로 반환됨
def solution(arr):
    return [arr[i] for i in range(len(arr)) if [arr[i]] != arr[i + 1 : i + 2]] 


# Solution_5 -> Solution_3 보다 좀 더 느림
def solution(arr):
    return [v for i, v in enumerate(arr) if arr[i - 1 : i] != [arr[i]]]


# Solutino_6 -> Solution_1과 시간 소요 비슷
def solution(arr):
    result = []
    for c in arr:
        if (len(result) == 0) or (result[-1] != c):
            result.append(c)
    return result


# test case
print(solution([1, 1, 3, 3, 0, 1, 1]))  # [1, 3, 0, 1]
print(solution([4, 4, 4, 3, 3]))        # [4, 3]