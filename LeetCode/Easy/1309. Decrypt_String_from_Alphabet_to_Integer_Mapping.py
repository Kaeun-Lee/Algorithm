# https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/

# Solution_1
# 1. #이 있는 두 자리의 숫자를 바꾼 후, 나머지 숫자는 한 자리씩 문자로 대체
# 2. ord('a')는 97 이며 이것은 chr(97)이 'a'라는 것을 의미함 -> 숫자를 기반으로 문자를 만들 수 있음
# 'a'는 알파벳의 첫 문자이고, 이 숫자의 index를 1로 한다 -> 즉 chr(96+1)은 'a'
class Solution:
    def freeAlphabets(s: str) -> str:
        for i in range(26, 0, -1): s = s.replace(str(i)+'#'*(i>9), chr(96+i))  # (i>9)가 True이면 두 자리 숫자 중 #가 붙은 숫자를 찾음
        return s
        
        
sol = Solution()
test_case1 = Solution.freeAlphabets(s = "10#11#12")
test_case2 = Solution.freeAlphabets(s = "1326#")
print(test_case1)  # "jkab"
print(test_case2)  # "acz"