# Quick Sort

# 1. 널리 사용되고 있는 가장 직관적인 형태의 퀵 정렬
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end:  # 원소가 1개인 경우 종료
        return 
    
    pivot = start     # 피벗은 첫 번째 원소 (호어 분할(Hoare Partition) 방식)
    left = start + 1
    right = end
    
    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복    
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:  # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[pivot], array[right] = array[right], array[pivot]
        else:             # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각자 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)
    
quick_sort(array, 0, len(array) - 1)
print(array)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# 2. 파이썬의 장점을 살려 짧게 작성한 퀵 정렬 -> pivot과 data를 비교하는 연산 횟수 증가
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    #  리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array
    
    pivot = array[0]  # 피벗은 첫 번째 원소
    tail = array[1:]  # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot]  # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot]  # 분할된 오른쪽 부분
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))
