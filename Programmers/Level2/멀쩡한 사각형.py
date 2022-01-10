# Summer/Winter Coding(2019) | https://programmers.co.kr/learn/courses/30/lessons/62048

# Solution_1
from math import gcd
def solution(w,h):
    return w * h - (w + h - gcd(w,h)) # 최소 공배수 이용


# Solution_2 
from math import gcd
def gcd(a,b): return b if (a==0) else gcd(b%a, a)
def solution(w,h): return w*h-w-h+gcd(w,h)


# Solution_3
from math import gcd
def solution(w,h):
    return w * h - (w/gcd(w,h) + h/gcd(w,h) - 1) * gcd(w, h)



test_case1 = solution(8,12)
print(test_case1) # 80
