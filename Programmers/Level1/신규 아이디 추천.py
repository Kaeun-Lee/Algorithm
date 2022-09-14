# 2021 KAKAO BLIND RECRUITMENT | https://programmers.co.kr/learn/courses/30/lessons/72410

# Solution_1
def solution(new_id):
    import re
    
    answer = new_id.lower()                             # step1. 소문자로 변경
    answer = "".join(re.findall('[a-z0-9-_.]',answer))  # step2. 소문자, 숫자, -, _, . 만 선택
    answer = re.sub('[.]{2,}', '.', answer)             # step3. '.'이 2개 이상인 것을 '.' 1개로 치환
    answer = re.sub('^[.]|[.]$', '', answer)            # step4. '.'이 맨 처음이나 맨 끝에 있는 경우 제거
    if len(answer) == 0:                                # step5. 빈 문자열인 경우 'a'대입 / append는 리스트에서 사용 가능
        answer = answer + 'a'
    elif len(answer) >= 16:                             # step6. 길이가 16 이상이면 15로 제한한 뒤, 맨 끝에 '.'이 있는 경우 제거
        answer = re.sub('[.]$', '', answer[:15])
    if len(answer) <= 2:                                # step7. 길이가 2 이하면, 길이가 3이 될 때까지 마지막 문자를 끝에 붙임
        len_ = len(answer)
        while len_ < 3:
            answer += answer[-1] 
            len_ += 1        
    return answer


# Solution_2
import re
def solution(new_id):
    new_id = new_id.lower()
    new_id = re.sub('[^a-z0-9\-_.]', '', new_id)
    new_id = re.sub('[.]+', '.', new_id)
    new_id = re.sub('^[.]', '', new_id)  # sub("(^\.|\.$)", "", new_id)도 가능
    new_id = re.sub('[.]$', '', new_id)
    if len(new_id) == 0:
        new_id += 'a'
    new_id = new_id[:15]
    new_id = re.sub('[.]$', '', new_id) 
    while len(new_id) < 3:
        new_id +=  new_id[-1]
    return new_id


# Solution_3
import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)   # '\-'로 구분
    st = re.sub('\.+', '.', st)            # '\.+' -> . 이 1개 이상인 것은 . 하나로 치환
    st = re.sub('^[.]|[.]$', '', st)    
    st = 'a' if len(st) == 0 else st[:15]  # 길이와 관련된 부분을 동시에 처리
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])  # for문으로 길이가 부족한 만큼 반복 후 리스트로 나온 값을 join
    return st
    #  st + st[-1] * (3-len(st))도 가능


# test case
test_case1 = solution("...!@BaT#*..y.abcdefghijklm")
test_case2 = solution("z-+.^.")
test_case3 = solution("=.=")
test_case4 = solution("123_.def")
test_case5 = solution("abcdefghijklmn.p")
print(test_case1)  # bat.y.abcdefghi
print(test_case2)  # z--
print(test_case3)  # aaa
print(test_case4)  # 123_.def
print(test_case5)  # abcdefghijklmn