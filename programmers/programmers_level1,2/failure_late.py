def solution(N, stages):
    answer=[]
    fail=[]
    stage=0

    for i in range(1,N+1):
        for j in range(len(stages)):
            if(stages[j]>=i):
                stage+=1
        if(stage!=0):
            fail.append(stages.count(i)/stage)
        else:
            fail.append(0)
        stage=0

    while True:
        if len(fail)==len(answer):
            break
        idx=fail.index(max(fail))
        answer.append(idx+1)
        fail[idx]=-1

    return answer