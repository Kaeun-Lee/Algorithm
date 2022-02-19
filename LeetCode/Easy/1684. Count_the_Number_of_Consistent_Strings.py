# https://leetcode.com/problems/count-the-number-of-consistent-strings/

# Solution_1
from typing import List
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        char = list(allowed)
        cnt = 0
        
        for word in words:
            tmp = 0
            for i in list(word):  
                if i in char:     # 각 문자가 char에 있다면 count
                    tmp += 1
            if tmp == len(word):  # word 안의 모든 문자가 char에 있는 경우 count
                cnt += 1
        return cnt
 
 
 # Solution_2
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)             # set은 hash table로 구현됨
        count = 0
        
        for word in words:
            for letter in word:
                if letter not in allowed:  # 각 문자가 allowed에 없는 경우 count 후 break
                    count += 1
                    break
                
        return len(words) - count 
 
 
 
sol = Solution()
test_case1 = sol.countConsistentStrings(allowed = "ab", words = ["ad","bd","aaab","baa","badab"])
test_case2 = sol.countConsistentStrings(allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"])
test_case3 = sol.countConsistentStrings(allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"])
print(test_case1)  # 2
print(test_case2)  # 7
print(test_case3)  # 4