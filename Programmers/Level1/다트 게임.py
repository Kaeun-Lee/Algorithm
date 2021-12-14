# 2018 KAKAO BLIND RECRUITMENT [1차] | https://programmers.co.kr/learn/courses/30/lessons/17682

# Solution_1
import re 
def solution(dartResult):
    temp = []
    sep = re.split('(\d+)(\w)', dartResult)  # ['', '1', 'S', '', '2', 'D', '*', '3', 'T', '']
    for i in range(len(sep)):   
        if sep[i] != '':
            if sep[i] in '12345678910':      # 숫자인 경우 계산을 위해 temp에 append
                temp.append(int(sep[i]))
            elif sep[i] == 'S':
                temp[-1] = temp[-1]**1
            elif sep[i] == 'D':
                temp[-1] = temp[-1]**2
            elif sep[i] == 'T':
                temp[-1] = temp[-1]**3
            elif sep[i] == '*': 
                if len(temp) >= 2:          
                    temp[-1] = temp[-1]*2
                    temp[-2] = temp[-2]*2
                else:                        # '*'이 첫 번째 기회에 나오는 경우
                    temp[-1] = temp[-1]*2
            elif sep[i] == '#':
                temp[-1] = temp[-1]*-1
    return sum(temp)
   

     
test_case1 = solution('1S2D*3T')
test_case2 = solution('1D2S#10S')
test_case3 = solution('1D2S0T')
test_case4 = solution('1S*2T*3S')
test_case5 = solution('1D#2S*3S')
test_case6 = solution('1T2D3D#')
test_case7 = solution('1D2S3T*')
print(test_case1)  # 37
print(test_case2)  # 9
print(test_case3)  # 3
print(test_case4)  # 23
print(test_case5)  # 5
print(test_case6)  # -4
print(test_case7)  # 59
