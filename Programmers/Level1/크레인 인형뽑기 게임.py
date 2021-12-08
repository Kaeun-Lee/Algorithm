# 2019 카카오 개발자 겨울 인턴십 | https://programmers.co.kr/learn/courses/30/lessons/64061

# Solution_1
def solution(board, moves):
    answer = 0
    basket = []
    
    for i in moves:
        for j in range(len(board)):
            doll = board[j][i-1]   # 인덱스에 접근하려면 입력값에서 -1을 해줘야 함
            if doll != 0:          # 0 이 아닌 숫자가 나오는 순간(인형이 있는 곳)
                basket.append(doll)
                board[j][i-1] = 0  # 뽑힌 숫자는 0으로 바꿔줌
                if (len(basket) > 1) and (doll == basket[-2]):          # 바구니에 숫자가 담긴 뒤 숫자가 연속된 경우
                    basket.pop()
                    basket.pop()
                    answer += 2
                elif (len(basket) > 1) and (basket[-1] == basket[-2]):  # 앞의 두 숫자가 제거된 뒤 다시 숫자가 연속된 경우
                    basket.pop()
                    basket.pop()
                    answer += 2
                break              # 하나의 숫자가 뽑힌 뒤 다음 행으로 넘어가지 않도록 멈춤
    
    return answer


# Solution_2
def solution(board, moves):
    stacklist = []
    answer = 0
    
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0
                
                if len(stacklist) > 1:  # 숫자가 연속된 경우를 한 번에 처리함
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop()
                        stacklist.pop()
                        answer += 2
                break
                    
    return answer


# Solution_3
def solution(Board, moves):
    cols = list(map(lambda x : list(filter(lambda y : y > 0, x)), zip(*Board)))  # board의 [행, 열]을 cols [열, 행] 형태로 바꿔줌
    a, s = 0, [0]  # 빈 리스트에서 s.pop()을 하면 에러가 발생하기 때문에 0을 미리 넣어줌
    
    for m in moves:
        if len(cols[m-1]) > 0 :
            if (d := cols[m - 1].pop(0)) == (l := s.pop()):  # 바다코끼리 연산자(:=) : 할당과 테스트를 한 단계로 줄일 수 있음(python 3.8 이상)
                a += 2
            else:
                s.extend([l, d])    
            
    return a



test_case1 = solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])
print(test_case1)  # 4