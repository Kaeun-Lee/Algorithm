# 정렬 | https://school.programmers.co.kr/learn/courses/30/lessons/42748

# Solution_1
def solution(array, commands):
    answer = []
    for i in commands:
        result = array[i[0]-1:i[1]]
        result.sort()
        answer.append(result[i[2]-1])

    return answer


# Solution_2 -> Lambda, map 활용
def solution(array, commands):
    return list(map(lambda x : sorted(array[x[0]-1:x[1]])[x[2]-1], commands))


# Solution_3 -> List Comprehension 활용
def solution(array, commands):
    return [sorted(array[a-1:b])[c-1] for a,b,c in commands] 


# test case
solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])  # [5, 6, 3]