# 2020 카카오 인턴십 | https://programmers.co.kr/learn/courses/30/lessons/67256

# Solution_1
def solution(numbers, hand):
    left_key = {1 : (0,1), 4 : (1,1), 7 : (2,1), '*' : (3,1)} 
    right_key = {3 : (0,3), 6 : (1,3), 9 : (2,3), '#' : (3,3)}
    other_key = {2 : (0,2), 5 : (1,2), 8 : (2,2), 0 : (3,2)}

    left = []
    right = []
    answer = []
    
    left.append(left_key['*'])  # 손가락이 시작하는 key의 위치 
    right.append(right_key['#'])
        
    for i in numbers:
        if  i in left_key.keys():
            left.append(left_key[i])
            answer.append('L')
        elif i in right_key.keys():
            right.append(right_key[i])
            answer.append('R')
        else:
            l = sum([abs(x-y) for x, y in zip(left[-1], other_key[i])])   # 행렬 값을 이용하여 거리 계산
            r = sum([abs(x-y) for x, y in zip(right[-1], other_key[i])])    
            if l < r :
                left.append(other_key[i])
                answer.append('L')
            elif l > r :
                right.append(other_key[i])
                answer.append('R')
            else:
                if hand == "left":
                    left.append(other_key[i])
                    answer.append('L')
                else:
                    right.append(other_key[i])
                    answer.append('R')
    return "".join(answer)


# Solution_2
def solution(numbers, hand):
    answer = ''
    key_dict = {1:(0,0),2:(0,1),3:(0,2),
                4:(1,0),5:(1,1),6:(1,2),
                7:(2,0),8:(2,1),9:(2,2),
                '*':(3,0),0:(3,1),'#':(3,2)}

    left = [1,4,7]
    right = [3,6,9]
    lhand = '*'
    rhand = '#'
    
    for i in numbers:
        if i in left:
            answer += 'L'         # append 대신 문자열 합을 이용
            lhand = i             # key만 바꿔줌
        elif i in right:
            answer += 'R'
            rhand = i
        else:
            curPos = key_dict[i]  # i의 value 값
            lPos = key_dict[lhand]
            rPos = key_dict[rhand]
            ldist = abs(curPos[0]-lPos[0]) + abs(curPos[1]-lPos[1])  # 인덱스 값으로 계산
            rdist = abs(curPos[0]-rPos[0]) + abs(curPos[1]-rPos[1])

            if ldist < rdist:
                answer += 'L'
                lhand = i
            elif ldist > rdist:
                answer += 'R'
                rhand = i
            else:
                if hand == 'left':
                    answer += 'L'
                    lhand = i
                else:
                    answer += 'R'
                    rhand = i
    return answer



test_case1 = solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")
test_case2 = solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left")
test_case3 = solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right")
print(test_case1)  # LRLLLRLLRRL
print(test_case2)  # LRLLRRLLLRR
print(test_case3)  # LLRLLRLLRL