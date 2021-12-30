# https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

from typing import List

# Solution_1
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        word1 = ''.join(word1)
        word2 = ''.join(word2)
        return word1 == word2
    
    
# Solution_2 -> wSolution_1과 같지만 좀 더 짧은 코드
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return ''.join(word1) == ''.join(word2)
    
    
# Solution_3 -> generator 사용(generator는 모든 값을 메모리에 담고 있지 않고, 그때그때 값을 생성해서 반환함)
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        for c1, c2 in zip(self.gen(word1), self.gen(word2)):
            if c1 != c2:
                return False
        return True

    def gen(self, word: List[str]):
        for s in word:
            for c in s:
                yield c # return과 비슷하게 사용되는 키워드
        yield None
        
        
# Solution_4 -> Solution_3과 비슷하지만 더 짧음
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        # all : 반복 가능한 자료형(iterable)의 모든 요소가 참이면 True를 반환하는 함수
        return all(c1 == c2 for c1, c2 in zip(self.gen(word1)), self.gen(word2)) 

    def gen(self, word: List[str]):
        for s in word:
            for c in s:
                yield c # return과 비슷하게 사용되는 키워드
        yield None       
        
        
        
sol = Solution()
test_case1 = sol.arrayStringsAreEqual(["ab", "c"], ["a", "bc"])
test_case2 = sol.arrayStringsAreEqual(["a", "cb"], ["ab", "c"])
print(test_case1) # True
print(test_case2) # False