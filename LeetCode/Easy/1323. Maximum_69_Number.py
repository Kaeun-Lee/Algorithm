# https://leetcode.com/problems/maximum-69-number/

# Solution_1 -> 6 하나만 9로 바꾸기
class Solution():
    def maximum69Number(self, num):
        return int(str(num).replace('6', '9', 1))  # replace('변경하고 싶은 문자', '변경 후 문자', 횟수)
    
    
# Solution_2 -> 공간 복잡도 줄임
class Solution:
    def maximum69Number (self, num: int) -> int:
        i = 0                   # first digit of 6
        tem = num               # original value num
        sixidx = -1             # store the first occurance of 6 in the integer
        while tem > 0:
            if tem % 10 == 6:
                sixidx = i      # refresh sixidx when found 6 at large digit
            tem = tem // 10       # shift tem by 1 digit
            i += 1              # increase the digit index by 1
        return (num + 3 *(10**sixidx)) if sixidx != -1 else num  # (9669 + 3 * (10^2)) = 9969


# Solution_3 -> divide and take the mod. divmod() 사용
class Solution:
    def maximum69Number (self, num: int) -> int:

        six_index = -1
        remainder = num
        pos = 0

        while remainder:
            remainder, digit = divmod(remainder, 10)
            if digit == 6:
                six_index = pos
            pos += 1

        return num + 3 * 10 ** six_index if six_index >= 0 else num



sol = Solution()
test_case1 = sol.maximum69Number(9669)
test_case2 = sol.maximum69Number(9996)
test_case3 = sol.maximum69Number(9999)
print(test_case1)  # 9969
print(test_case2)  # 9999
print(test_case3)  # 9999