# https://leetcode.com/problems/find-first-palindromic-string-in-the-array/

# Solution_1
from typing import List
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word  in words:
            rev_word = word.sort()
            if word == rev_word:
                return word
                break
            return ""
        
        