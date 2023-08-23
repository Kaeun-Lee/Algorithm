# 코딩 기초 트레이닝


# My Solution
def solution(arr1, arr2):
    if len(arr1) != len(arr2):
        return 1 if len(arr1) > len(arr2) else -1
    if sum(arr1) > sum(arr2):
        return 1
    elif sum(arr1) < sum(arr2):
        return -1
    return 0


# Another Solution 1
# arr1이 더 길거나 합이 크면 : True(1) - False(0)
# arr2이 더 길거나 합이 크면 : False(0) - True(1)
# arr1, arr2 길이가 같거나 합이 같으면 : False(0) - False(0) or False(0) - False(0)
def solution(arr1, arr2):
    return (len(arr1) > len(arr2)) - (len(arr2) > len(arr1)) or (
        sum(arr1) > sum(arr2)
    ) - (sum(arr2) > sum(arr1))


# Another Solution 2
def solution(arr1, arr2):
    arr1, arr2 = [[sum(arr1), sum(arr2)], [len(arr1), len(arr2)]][
        len(arr1) != len(arr2)
    ]
    return (arr1 != arr2) * (1 if arr1 > arr2 else -1)
