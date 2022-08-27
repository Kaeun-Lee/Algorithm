# 탐욕법(Greedy) | https://school.programmers.co.kr/learn/courses/30/lessons/42862#qna

# Solution_1
def solution(n, lost, reserve):
    inter = set(lost) & set(reserve)
    lost = set(lost) - inter
    reserve = set(reserve) - inter
    student = [True] * (n + 2) 

    for i in lost:
        student[i] = False

    for i in reserve:
        if student[i - 1] == False:
            student[i - 1] = True
        elif student[i + 1] == False:
            student[i + 1] = True
    return sum(student[1:n + 1])
    

# Solution_2 -> 좀 더 빠름
def solution(n, lost, reserve):
    # 운동복을 잃어버렸지만 여분의 운동복이 있는 학생 제외
    lost2 = set(lost) - set(reserve)
    reserve2 = set(reserve) - set(lost)

    for i in lost2:
        if i - 1 in reserve2:
            reserve2.remove(i - 1)
        elif i + 1 in reserve2:
            reserve2.remove(i + 1)
        else:
            n -= 1  # 운동복을 못 빌려서 수업 참가 못하는 학생 제외
    return n


# Solution_3
def solution(n, lost, reserve):
    _reserve = set(reserve) - set(lost)
    _lost = set(lost) - set(reserve)

    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)


# test case
print(solution(5, [2, 4], [1, 3, 5]))     # 5
print(solution(5, [2, 4], [3]))           # 4
print(solution(3, [3], [1]))              # 2
print(solution(4, [2, 3], [3, 4]))        # 3
print(solution(3, [1, 2], [2, 3]))        # 2
print(solution(6, [1, 3, 5], [2, 4, 6]))  # 6
print(solution(5, [4, 2], [3, 5]))        # 5