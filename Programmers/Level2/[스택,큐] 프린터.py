# 스택/큐 | https://programmers.co.kr/learn/courses/30/lessons/42587

# Solution_1
def solution(priorities, location):
    progress = []
    max_num = 1
    start = priorities[0] # 2
    temp = []

    for i in range(len(priorities)):
        if (priorities[i] > start) and (priorities[i] > max_num):
            max_num = priorities[i]
            progress.append(max_num)
            temp.append(max_num)
            priorities.pop(start)
    return priorities