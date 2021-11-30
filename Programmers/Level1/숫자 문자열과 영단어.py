# 2021 카카오 채용연계형 인턴십 | https://programmers.co.kr/learn/courses/30/lessons/81301

# Solution_1
def solution(s):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    for word in words:
        if word in s:
            s = s.replace(word, str(words.index(word)))  # 리스트의 index를 사용하여 문자열 치환
    return int(s)                                        # 문자열 -> 정수 return


# Solution_2 -> Solution_1과 유사
def solution(s):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    for i in range(len(words)):                          # 리스트의 길이를 사용하여 index로 활용
        s = s.replace(words[i], str(i))
    return int(s)


# Solution_3
num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", 
           "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for k, v in num_dic.items():                         # dict의 key, value를 활용
        answer = answer.replace(k, v)
    return int(answer)
        
    
    
test_case1 = solution("one4seveneight")
test_case2 = solution("23four5six7")
test_case3 = solution("2three45sixseven")
test_case4 = solution("123")
print(test_case1)  # 1478
print(test_case2)  # 234567
print(test_case3)  # 234567
print(test_case4)  # 123