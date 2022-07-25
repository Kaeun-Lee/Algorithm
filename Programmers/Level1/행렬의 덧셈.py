# 연습문제 | https://school.programmers.co.kr/learn/courses/30/lessons/12950

# Solution_1
def solution(arr1, arr2):
    for i in range(len(arr1)): 
        for j in range(len(arr1[0])): 
            arr1[i][j] += arr2[i][j]  
    return arr1


# Solution_2 -> zip 이용, 시간 소요가 1/2로 줄어듦
def solution(arr1, arr2):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(arr1, arr2)] 
    return answer


# Solution_3 -> 여러 행렬을 동시에 더할 수 있음
def solution(arr1, arr2):
    result = [list(map(sum, zip(*x))) for x in zip(arr1, arr2)]  # zip 함수에 *args 인수를 넣으면 col끼리 엮어줌
    return result


# Solution_4
def solution(arr1, arr2):
    return [[arr1[i][j] + arr2[i][j] for j in range(len(arr1[0]))] for i in range(len(arr1))]


# test case
print(solution([[1,2],[2,3]], [[3,4],[5,6]]))  # [[4, 6], [7, 9]]
print(solution([[1],[2]], [[3],[4]]))          # [[4], [6]]