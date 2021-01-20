def solution(participant, completion):
    if(len(set(participant))==len(set(completion))):      #동명이인
        participant.sort()
        completion.sort()
        for i in range(len(completion)):
            if(participant[i]!=completion[i]):
                return "".join(participant[i])
    return "".join(list(set(participant)-set(completion)))