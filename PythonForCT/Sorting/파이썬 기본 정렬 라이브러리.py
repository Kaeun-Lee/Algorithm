# sorted() : 퀵 정렬과 동작 방식이 비슷한 '병합 정렬' 기반
#         -> 병합 정렬은 퀵 정렬보다 느리지만, 최악의 경우에도 시간 복잡도 O(NlogN) 보장 
# sort() : 리스트 객체의 내장 함수
#       -> 내부 원소를 바로 정렬

# sorted()
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

result = sorted(array)
print(result)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# sort()
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

array.sort()
print(array)

# key 매개변수 활용
# key 값 : '정렬 기준'이 되며, 함수가 들어가야 함
# 리스트의 데이터가 튜플로 구성되어 있을 때, 각 데이터의 2번째 원소를 기준으로 설정하는 경우
array = [('바나나',2), ('사과', 5), ('당근',3)]

def setting(data):
    return data[1]

result = sorted(array, key=setting)
print(result)