# 해시 | https://programmers.co.kr/learn/courses/30/lessons/42577

# Solution_1
def solution(phone_book):
    phone_book.sort()
    
    for i in range(len(phone_book)-1):
        s_num = phone_book[i]
        len_ = len(s_num)
        for j in phone_book[i+1:]:
            if s_num in j[:len_+1]:
                return False
            return True
                


test_case1 = solution(["119", "97674223", "1195524421"])
test_case2 = solution(["123","456","789"])
test_case3 = solution(["12","123","1235","567","88"])
print(test_case1)
print(test_case2)
print(test_case3)
