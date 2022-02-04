# https://leetcode.com/problems/maximum-69-number/

# Solution_1
def maximum69Number(self, num):
    return int(str(num).replace('6', '9', 1))  # replace("찾을 값", "바꿀 값", [바꿀 횟수])