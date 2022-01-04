# 해시 | https://programmers.co.kr/learn/courses/30/lessons/42577

# Solution_1 -> hash 사용
def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:  # {'123':1, '456':1, '789':1}
        hash_map[phone_number] = 1
    for phone_number in phone_book:  # '123', '456', '789'
        temp = ""
        for number in phone_number:  # '1', '2', '3'
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer


# Solution_2
def solution(phone_book):
    phoneBook = sorted(phone_book)  # ["119", "1195524421", "97674223"]
    
    for p1, p2 in zip(phoneBook, phoneBook[1:]): # 119 1195524421, 1195524421 97674223
        if p2.startswith(p1):
            return False
    return True



test_case1 = solution(["119", "97674223", "1195524421"])
test_case2 = solution(["123","456","789"])
test_case3 = solution(["12","123","1235","567","88"])
print(test_case1)
print(test_case2)
print(test_case3)