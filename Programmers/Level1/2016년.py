# 연습문제 | https://school.programmers.co.kr/learn/courses/30/lessons/12901

# Solution_1
def solution(a, b):
    day = {0:'THU', 1:'FRI', 2:'SAT', 3:'SUN', 4:'MON', 5:'TUE', 6:'WED'}
    mon = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    cnt = b
    for i in range(a - 1): # 0,1,2,3
        cnt += mon[i]
    return day[cnt % 7]


# Solution_2
def solution(a, b):
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    return days[(sum(months[:a - 1]) + b - 1) % 7]


# Solution_3 -> datetime 함수 활용 ('월요일'부터 시작)
from datetime import datetime
def solution(a, b):
    day = 'MON TUE WED THU FRI SAT SUN'.split()
    return day[datetime(2016, a, b).weekday()]  # datetime(2016, a, b) : 2016-05-24 00:00:00


# test case
print(solution(5, 24))  # TUE