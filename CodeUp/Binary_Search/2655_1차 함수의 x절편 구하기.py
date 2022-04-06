# Binary_Search | https://codeup.kr/problem.php?id=2655

# Solution
def cal():
    a, b = map(int, input().split())
    x = -b/a
    return "{:.4f}".format(x)

print(cal())



# test_case
# 입력 : 1 5
# 출력 : -5.0000