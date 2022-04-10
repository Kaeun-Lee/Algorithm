# Binary Search

# Solution_1 -> 이진 탐색 (반복문)
n, m  = map(int, input().split())
array = list(map(int, input().split()))
height = [i for i in range(max(array))]  # 가장 긴 길이만큼 배열 생성

def binary_search(array, height, target, start, end):
    result = 0
    while start <= end:
        mid = (start + end) // 2
        rest_sum = 0

        for i in array:
            rest = i - height[mid]
            if rest > 0:
                rest_sum += rest
        
        if rest_sum >= target:
            result = height[mid]
            start = mid + 1
        else:
            end = mid - 1
    return result

print(binary_search(array, height, m, 0, len(height) - 1))


# Solution_2 -> 이진 탐색 (답안)
n, m = list(map(int, input().split()))   # 떡의 개수(N)와 요청한 떡의 길이(M)을 입력받기
array = list(map(int, input().split()))  # 각 떡의 개별 높이 정보를 입력받기

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array)

# 이진 탐색 수행 (반복적)
result = 0
while (start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        # 잘랐을 때의 떡의 양 계산
        if x > mid:
            total += x - mid
    # 떡의 양이 부족한 경우 더 많이 자르기(왼쪽 부분 탐색)
    if total < m:
        end = mid - 1
    # 떡의 양이 충분한 경우 덜 자르기(오른쪽 부분 탐색)
    else:
        result = mid  # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
        start = mid + 1

print(result)



# test_case
# 입력
# 4 6
# 19 15 10 17
# 출력 : 15