# Sorting

# Solution_1 -> 정렬 라이브러리의 key를 활용
n = int(input())
student = [tuple(input().split()) for i in range(n)]

def setting(student):
    return student[1]

result = sorted(student, key=setting)

for i in range(len(result)):
    print(result[i][0], end = ' ')
    

# Solution_2 -> lambda 함수로 정렬 기준 정하는 방법
# N을 입력받기
n = int(input())

# N명의 학생 정보를 입력받아 리스트에 저장
array = []
for i in range(n):
    input_data = input().split()
    # 이름은 문자열 그대로, 정수는 정수형으로 변환하여 저장
    array.append((input_data[0], int(input_data[1])))
    
# 키(Key)를 이용하여, 점수를 기준으로 정렬
array = sorted(array, key=lambda student: student[1])

# 정렬이 수행된 결과를 출력
for student in array:
    print(student[0], end=' ')
    
    
    
# test_case
# 입력
# 2
# 홍길동 95
# 이순신 77
# 출력 : 이순신 홍길동