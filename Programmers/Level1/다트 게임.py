# 2018 KAKAO BLIND RECRUITMENT [1차] | https://programmers.co.kr/learn/courses/30/lessons/17682

# Solution_1
import re 
def solution(dartResult):
    temp = []
    sep = re.split('(\d+)(\w)', dartResult)  # ['', '1', 'D', '', '2', 'S', '#', '10', 'S', '']
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
   


# Solution_2
import re
def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    for i in range(len(dart)):           # [('1', 'S', ''), ('2', 'D', '*'), ('3', 'T', '')]
        if dart[i][2] == '*' and i > 0:  # '*'이 2,3번째 기회에 나오는 경우
            dart[i-1] *= 2               # 앞 인덱스 값에 *2를 해줌
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]  
 
    
    answer = sum(dart)
    return answer


# Solution_3
import re
def solution(dartResult):
    point = []
    answer = []
    dartResult = dartResult.replace('10', 'k')             # 1D2S#kS / 자르기 힘든 수 10을 특정 문자로 치환
    point = ['10' if i == 'k' else i for i in dartResult]  # ['1', 'D', '2', 'S', '#', '10', 'S']
    
    i = -1
    sdt = ['S', 'D', 'T']
    for j in point:
        if j in sdt:
            answer[i] = answer[i] ** (sdt.index(j)+1)      # sdt.index(j)+1 -> 0+1, 1+1, 2+1
        elif j == '*':
            answer[i] = answer[i] * 2
            if i != 0:                                     # '*'이 2,3번째 기회에 나오는 경우
                answer[i -1] = answer[i -1] * 2
        elif j == '#':
            answer[i] = answer[i] * (-1)
        else:
            answer.append(int(j))
            i += 1                                         # 숫자가 들어갈 때 인덱스 값을 증가시킴
    return sum(answer)



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