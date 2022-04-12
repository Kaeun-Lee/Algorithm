# https://leetcode.com/problems/sorting-the-sentence/

# Solution_1
import re
class Solution:
    def sortSentence(self, s: str) -> str:
        s = re.split(' ', s)      # 공백으로 split
        temp = ['']* len(s)       # split된 길이만큼 공간 확보
        
        for i in s:
            idx = int(i[-1]) - 1  # 각 문자열의 맨 끝에 있는 숫자를 index로 사용
            temp[idx] = i[:-1]    # index 자리에 문자열을 넣어줌
        return ' '.join(temp)
    

# Solution_2 -> 조금 더 빠름
class Solution:
    def sortSentence(self, s: str) -> str:
        words = s[::-1].split()                      # 맨 끝에서 부터 가져온 뒤 split / ['3a', '1sihT', '4ecnetnes', '2si']
        words.sort()                                 # 맨 앞에 위치한 숫자를 기준으로 sort / ['1sihT', '2si', '3a', '4ecnetnes']
        result = [word[1:][::-1] for word in words]  # ['This', 'is', 'a', 'sentence']
        return ' '.join(result)
    
    
    
sol = Solution()   
test_case1 = sol.sortSentence("is2 sentence4 This1 a3")
test_case2 = sol.sortSentence("Myself2 Me1 I4 and3")
print(test_case1)  # "This is a sentence"
print(test_case2)  # "Me Myself and I"