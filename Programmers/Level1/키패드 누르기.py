# 2020 카카오 인턴십 | https://programmers.co.kr/learn/courses/30/lessons/67256

# Solution_1
def solution(numbers, hand):
    left_num = ['*', 1, 4, 7]
    right_num = ['#', 3, 6, 9]
    
    left = []
    right = []

    answer = []
    
    if hand == "left":
        left.append('*')
    else:
        right.append('#')
    for i in numbers:
        if i in left_num:
            left.append(i)
            answer.append('L')
        elif i in right_num:
            right.append(i)
            answer.append('R')
              
        else: 
            l = abs(i-left[-1])
            r = abs(i-right[-1])
            print(left)
            print(right)
            if l < r :
                print(l,r)
                left.append(i)
                answer.append('L')
            elif r < l :
                print(l,r)
                answer.append('R')
            else:
                print(l,r)
                if hand == 'left':
                    left.append(i)
                    answer.append('L')
                elif hand == 'right':
                    right.append(i)
                    answer.append('R')
  
    return "".join(answer)




test_case1 = solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")
print(test_case1)