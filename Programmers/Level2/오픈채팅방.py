# 2019 KAKAO BLIND RECRUITMENT | https://programmers.co.kr/learn/courses/30/lessons/42888

# Solution_1
def solution(record):
    answer = []
    user = {}
    
    for i in record:
        txt = i.split()
        if txt[1] not in user:
            user[txt[1]] = txt[2]
        else:
            if txt[0] == "Enter":
                
                if txt[2] != user[txt[1]]:
                    user[txt[1]] = txt[2]
                else:
                    continue
            elif txt[0] == "Change":
                user[txt[1]] = txt[2]
    
    for i in record:
        txt = i.split()
        if txt[0] == "Enter":
            answer.append(user[txt[1]]+"님이 들어왔습니다.")
        elif txt[0] == "Leave":
            answer.append(user[txt[1]]+"님이 나갔습니다.")
            
    return answer



test_case = solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo",
                      "Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])
print(test_case) # ['Prodo님이 들어왔습니다.', 'Ryan님이 들어왔습니다.', 'Prodo님이 나갔습니다.', 'Prodo님이 들어왔습니다.']