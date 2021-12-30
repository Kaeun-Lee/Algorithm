# 해시 | https://programmers.co.kr/learn/courses/30/lessons/42577

# Solution_1
import re
from collections import Counter
def solution(phone_book):
    lst = []
    
    for i in phone_book:
        lst.append(len(i))
    
    min_ = min(lst)   
    
    num = []
    for i in range(len(phone_book)):
        num.append(phone_book[i][:min_])
    

    dic_ = {}
    for i in num:
        if i not in dic_:
            dic_[i] = 1
        else:
            dic_[i] += 1
    
    for k, v in dic_.items():
        if v >=2 :
            return False
        else:
            return True