# Insertion Sort

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):      # index가 i부터 1까지 감소
        if array[j] < array[j-1]:  # 1칸씩 왼쪽으로 이동
            array[j], array[j-1] = array[j-1], array[j]
        else:  # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break
        
print(array)   # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]