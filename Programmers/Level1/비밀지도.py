# 2018 KAKAO BLIND RECRUITMENT [1차] | https://programmers.co.kr/learn/courses/30/lessons/17681

# Solution_1
def solution(n, arr1, arr2):
    answer = []
    arr1_ = []
    arr2_ = []
    test = ''
    
    for i in arr1:
        a = bin(i).lstrip('0b')
        if len(a) < n:  # 지도의 한 변의 길이 n에 맞춰 0을 채워줌
            for i in range(n-len(a)):
                test += '0'
            test += a
            arr1_.append(test)
            test = ''
        else:
            arr1_.append(str(a))

    for j in arr2:
        b = bin(j).lstrip('0b')
        if len(b) < n:
            for j in range(n-len(b)):
                test += '0'
            test += b
            arr2_.append(test)
            test = ''
        else:
            arr2_.append(str(b))
    
    test2 = ''
    for x in range(len(arr1_)): 
        for y in range(len(arr1_)):
            if arr1_[x][y] == '0' and arr2_[x][y] == '0':  # 2진수로 변경된 arr1_과 arr_2의 각 원소들을 비교
                test2 += ' '
            else: 
                test2 += '#'
        answer.append(test2)
        test2 = ''
    return answer


# Solution_2 -> 비트 연산자 활용
def solution(n, arr1, arr2): 
    answer = []
    for i, j in zip(arr1, arr2):
        a12 = str(bin(i|j)[2:])  # i와 j를 이진변환한 뒤 같은 자리에 모두 0이 오면 0, 하나라도 1이 있으면 1로 출력 후 '0b'제거
        a12 = a12.rjust(n, '0')
        a12 = a12.replace('1','#')
        a12 = a12.replace('0', ' ')
        answer.append(a12)
    return answer
        
        
# Solution_3 -> 정규표현식 사용
import re
def solution(n, arr1, arr2): 
    answer = ["#"] * n  # 리스트를 n 만큼 '#'으로 채워서 늘려줌
    for i in range(0, n): 
        answer[i] = str(bin(arr1[i]|arr2[i]))[2:]  # array[0], array[1]...
        answer[i] = re.sub('1', '#', '0'*(n-len(answer[i]))+answer[i])  # '0'*0 = '', '0'*1 = '0', '0'*2 = '00'
        answer[i] = re.sub('0', ' ', answer[i])
    return answer


# Solution_4 -> 이진법을 직접 구현
def solution(n, arr1, arr2):
    answer_1 = []
    answer_2 = []
    final =[]
    rules = [2**i for i in range(n-1, -1, -1)]
    ret =''
    
    for ans_1 in arr1:
        for i in rules:
            if ans_1 >= i:
                ret += '#'
                ans_1 -= i
            else:
                ret += ' '
        answer_1.append(ret)
        ret = ''
        
    for ans_2 in arr2:
        for i in rules:
            if ans_2 >= i:
                ret += '#'
                ans_2 -= i
            else:
                ret += ' '
        answer_2.append(ret)
        ret = ''
    
    for i in range(n):
        for j in range(n):
            if answer_1[i][j] == ' ' and answer_2[i][j] == ' ':
                ret += ' '
            else:
                ret += '#'
        final.append(ret)
        ret = ''
    return final



test_case1 = solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])
test_case2 = solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10])

print(test_case1)  # ['#####', '# # #', '### #', '#  ##', '#####']
print(test_case2)  # ['######', '###  #', '##  ##', ' #### ', ' #####', '### # ']