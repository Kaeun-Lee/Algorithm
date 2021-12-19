# 2019 KAKAO BLIND RECRUITMENT | https://programmers.co.kr/learn/courses/30/lessons/42888

# Solution_1
def solution(record):
    answer = []
    user = {}
    
    for i in record:
        txt = i.split()
        if txt[1] not in user: # 사용자 id와 이름 등록
            user[txt[1]] = txt[2]
        else:
            if txt[0] == "Enter":               
                if txt[2] != user[txt[1]]: # 입장 시 이름이 이미 등록된 이름과 다르다면 변경
                    user[txt[1]] = txt[2]
                else:
                    continue
            elif txt[0] == "Change": # 이름 변경
                user[txt[1]] = txt[2]
    
    for i in record:
        txt = i.split()
        if txt[0] == "Enter":
            answer.append(user[txt[1]]+"님이 들어왔습니다.")
        elif txt[0] == "Leave":
            answer.append(user[txt[1]]+"님이 나갔습니다.")
            
    return answer


# Solution_2
def solution(record):
    answer = []
    namespace = {}
    printer = {'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}
    for r in record:
        rr = r.split(' ')
        if rr[0] in ['Enter', 'Change']: # 입장, 변경 시 이름 등록
            namespace[rr[1]] = rr[2]   
    
    for r in record:
        if r.split(' ')[0] != 'Change':  # 이름을 변경하는 경우가 아니면, 기록함
            answer.append(namespace[r.split(' ')[1]] + printer[r.split(' ')[0]])
            
    return answer



test_case = solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo",
                      "Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])
print(test_case) # ['Prodo님이 들어왔습니다.', 'Ryan님이 들어왔습니다.', 'Prodo님이 나갔습니다.', 'Prodo님이 들어왔습니다.']