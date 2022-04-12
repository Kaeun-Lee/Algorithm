# https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/

# Solution_1
# 1. #이 있는 두 자리의 숫자를 바꾼 후, 나머지 숫자는 한 자리씩 문자로 대체
# 2. ord('a')는 97 이며 이것은 chr(97)이 'a'라는 것을 의미함 -> 숫자를 기반으로 문자를 만들 수 있음
# 'a'는 알파벳의 첫 문자이고, 이 숫자의 index를 1로 한다 -> 즉 chr(96+1)은 'a'
class Solution:
    def freeAlphabets(self, s: str) -> str:
        for i in range(26, 0, -1): s = s.replace(str(i)+'#'*(i>9), chr(96+i))  # (i>9)가 True이면 두 자리 숫자 중 #가 붙은 숫자를 찾음
        return s
        
        
# # Solution_2 -> stack solution
class Solution:
    def freeAlphabets(self, s: str) -> str:
        s, res = list(s), ''  # s -> ['1', '0', '#', '1', '1', '#', '1', '2'] 
        while s:
            c = s.pop()                              # 맨 뒤 숫자를 꺼냄
            if c == '#':
                x = s.pop() + s.pop()                # 뒤에서 부터 2개 가져옴
                res += chr(ord('a')+int(x[::-1])-1)  # 뒤집힌 글자를 다시 원상 복귀한 후 int로 변환
            else:
                res += chr(ord('a')+int(c)-1)
        return res[::-1]                             # pop으로 인해 거꾸로 출력된 문자열을 원상 복귀


# Solution_3 -> Regex
import re
class Solution:
    def freeAlphabets(self, s: str) -> str:
        return ''.join(chr(int(i[:2]) + 96) for i in re.findall(r'\d\d#|\d',s))

    
        
sol = Solution()
test_case1 = sol.freeAlphabets(s="10#11#12")
test_case2 = sol.freeAlphabets(s="1326#")
print(test_case1)  # "jkab"
print(test_case2)  # "acz"