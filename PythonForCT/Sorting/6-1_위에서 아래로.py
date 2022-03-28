# Sorting

# Solution_1
# N을 입력받기
n = int(input())

# N개의 정수를 입력받아 리스트에 저장
lst = [int(input()) for i in range(n)]

# 파이썬 기본 정렬 라이브러리를 이용하여 정렬 수행
lst = sorted(lst, reverse=True)

# 정렬이 수행된 결과를 출력
for i in lst:
    print(i, end = ' ')
    
    

# test_case
# 입력
# 3
# 15
# 27
# 12
# 출력 : 27 25 12