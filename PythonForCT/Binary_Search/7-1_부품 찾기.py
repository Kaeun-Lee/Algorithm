# Search

# Solution_1-1 -> 이진 탐색 (재귀 함수)
n = int(input())
data = list(map(int, input().split()))
m = int(input())
request = list(map(int, input().split()))
# 이진 탐색을 위해 data를 정렬
data.sort()

def binary_search(array, target, start, end):
     # 제품이 없는 경우
    if start > end:
        return False
     
    mid = (start + end) // 2
     
    if array[mid] == target:
        return True
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)

# (1) 반복문 안에서 함수를 적용하여 각 target의 결과를 구하고 비교해서 출력
for i in request:
    if binary_search(data, i, 0, n -1) == True:
        print("yes", end=' ')
    else:
        print("no", end=' ')

# (2) map 함수를 적용해서 결과값을 모두 구한 뒤 결과를 비교해서 출력
# result = list(map(lambda i: binary_search(data, i, 0, n -1, request)))
# for r in result:
#     if r == True:
#         print("yes", end=' ')
#     else:
#         print("no", end=' ')


# Solution_1-2 -> 이진 탐색 (반복문)
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 index 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우, 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우, 오른쪽 확인
        else:
            start = mid + 1
    return None

n = int(input())                         # N(가게의 부품 개수) 입력
array = list(map(int, input().split()))  # 가게에 있는 전체 부품 번호를 공백으로 구분하여 입력
array.sort()                             # 이진 탐색을 수행하기 위해 사전에 정렬 수행
m = int(input())                         # M(손님이 확인 요청한 부품 개수) 입력
x = list(map(int, input().split()))      # 손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
    result = binary_search(array, i, 0, n - 1)  # 해당 부품이 존재하는지 확인
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')


# Solution_2-1 -> 계수 정렬
n = int(input())
data = list(map(int, input().split()))
m = int(input())
request = list(map(int, input().split()))

# data에서 최솟값과 최댓값을 찾고 그것을 다 담을 수 있는 list 생성)
count = [0] * (max(data) + 1)
# 원소를 돌면서 해당하는 index에 + 1
for i in data:
    count[i] += 1

# reqeust에서 하나씩 가져와서 해당 count가 0 이상이면 yes 아니면 no로 출력
for i in request:
    if count[i] >= 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')
        

# Solution_2-2 -> 계수 정렬 (답안)
n = int(input())
array = [0] * 1000001  # 모든 원소의 번호를 포함할 수 있는 크기의 리스트 (부품의 고유 번호 최댓값 -> 1,000,000)

# 가게에 있는 전체 부품 번호를 입력받아서 기록
for i in input().split():
    array[int(i)] += 1

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')

    
# Solution_3 -> 집합 자료형, 코드 간결성 우수
n = int(input())
data = list(map(int, input().split()))
m = int(input())
request = list(map(int, input().split()))

# data와 request의 set 집합 확인
set_data = set(data)
set_request = set(request)

# 교집합 찾기
inter = set_data & set_request

for i in request:
    if i in inter:
        print('yes', end=' ')
    else:
        print('no', end=' ')


# Solution_3-2 -> 집합 자료형 (답안)
n = int(input())
# 가게에 있는 전체 부품 번호를 입력받아서 집합(set) 자료형에 기록
array = set(map(int, input().split()))

m = int(input())
x = set(map(int, input().split()))

for i in x:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')



# *참고 : 데이터가 최대 1백만 개까지 주어질 수 있으므로 sys.stdin.readline()으로 input data 가져오기
# import sys
# n = int(sys.stdin.readline())
# total = list(map(int, sys.stdin.readline().strip().split()))
# total.sort()
# m = int(sys.stdin.readline())
# request = list(map(int, sys.stdin.readline().strip().split()))



# test_case
# 입력
# 5
# 8 3 7 9 2
# 3
# 5 7 9 2
# 출력 : no yes yes