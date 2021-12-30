# https://leetcode.com/problems/count-items-matching-a-rule/

# Solution_1 -> 속도 빠름, 메모리 차지 적음
class Solution: 
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        rule = {'type' : 0, 'color' : 1, 'name' : 2}
        cnt, index = 0, rule[ruleKey]
        
        for item in items:
            if item[index] == ruleValue:
                cnt += 1
        return cnt
    
    
# Solution_2
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        rule = {'type' : 0, 'color' : 1, 'name' : 2}
        return sum(1 for item in items if item[rule[ruleKey]] == ruleValue)