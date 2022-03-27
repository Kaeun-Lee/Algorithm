
# n, m = map(int, input().split())
# array = list(map(int, input().split()))

# def findh(array, h, max_h, m):
#     rest_sum = 0
#     while h <= max_h:
        
#         for i in range(len(array)):
#             rest = array[i] - h
#             if rest > 0:
#                 rest_sum += rest
        
#         if rest == m:
#             return h
 
#         elif rest < m:
#             h += 1
#             rest_sum = 0
#     return None
    
# max_h = max(array)
# h = sum(array) // len(array)    
# print(findh(array, h, max_h, m))
    
n, m = map(int, input().split())
array = list(map(int, input().split()))

def findh(array, h, max_h, m):
    if h > max_h:
        return

    rest_sum = 0
    for i in range(len(array)):
        rest = array[i] - h
        if rest > 0:
            rest_sum += rest

    if rest_sum == m:
        return h
    elif rest_sum > m:
        findh(array, h + 1, max_h, m)
    else:
        findh(array, h - 1, max_h, m)


h = sum(array) // len(array)
max_h = max(array)

print(findh(array, h, max_h, m))