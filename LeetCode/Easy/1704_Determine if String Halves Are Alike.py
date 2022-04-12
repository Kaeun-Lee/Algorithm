# https://leetcode.com/problems/determine-if-string-halves-are-alike/

# Solution_1
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        split_num = len(s) // 2
        a = s[:split_num]
        b = s[split_num:]
        cnt = 0
        
        for i in a:
            if i in vowels:
                cnt += 1
        for i in b:
            if i in vowels:
                cnt -= 1
                
        if cnt == 0:
            return True

   
# Solution_2
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set('aeiouAEIOU')
        a = b = 0
        i, j = 0, len(s) - 1  # 0, 3 / 맨 앞 인덱스, 맨 뒤 인덱스
        while i < j:
            a += s[i] in vowels
            b += s[j] in vowels
            i += 1  # 1
            j -= 1  # 2
        return a == b  
                
        
# Solution_3 -> Counter 함수 사용
from collections import Counter
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vs, n =  ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'], len(s)//2
        a, b = Counter(s[:n]), Counter(s[n:])                  # Counter({'b': 1, 'o': 1}), Counter({'o': 1, 'k': 1})

        return sum(a[v] for v in vs) == sum(b[v] for v in vs)  # [a[v] for v in vs] -> [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
        
        
        
sol = Solution()
test_case1 = sol.halvesAreAlike(s = "book")
test_case2 = sol.halvesAreAlike(s = "textbook")
print(test_case1)  # true
print(test_case2)  # false
        