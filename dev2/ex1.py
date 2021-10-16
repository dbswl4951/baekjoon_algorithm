import re

def check(registered_list, new_id):
    if new_id not in registered_list:
        return new_id,1
    return new_id,0

def solution(registered_list, new_id):
    new_id,flag = check(registered_list, new_id)
    if flag: return new_id

    while True:
        alpa = re.sub('\d', '', new_id)
        number = re.sub('[a-zA-Z]','',new_id)
        if not number:
            number = 0
        intNumber = int(number)+1
        registered_new_id = alpa+str(intNumber)
        new_id,flag = check(registered_list,registered_new_id)
        if flag: break
    return new_id

print(solution(["card", "ace13", "ace16", "banker", "ace17", "ace14"],'ace15'))
print(solution(["cow", "cow1", "cow2", "cow3", "cow4", "cow9", "cow8", "cow7", "cow6", "cow5"],'cow'))
print(solution(["bird99", "bird98", "bird101", "gotoxy"],"bird98"))
print(solution(["apple1", "orange", "banana3"],"apple"))
print(solution(["apple", "apple2"],'apple'))