#(야구공)
import sys
from itertools import permutations

n=int(sys.stdin.readline().strip())
data=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
people=[i for i in range(1,9)]
result=0

# 순열로 타순 정하기
# case[i]=j : i번째 타자는 j (j:0~8)
for case in permutations(people,8):
    case=list(case)
    case=case[:3]+[0]+case[3:]      # 4번째 주자는 무조건 0번째 사람
    score,idx=0,0

    # i번째 이닝 실행
    for i in range(n):
        out=0
        base1,base2,base3=0,0,0     # 1,2,3루 주자
        while out<3:
            if data[i][case[idx]]==0: out+=1
            elif data[i][case[idx]]==1:
                score+=base3
                base1,base2,base3=1,base1,base2
            elif data[i][case[idx]]==2:
                score+=(base2+base3)
                base1, base2, base3 =0, 1, base1
            elif data[i][case[idx]]==3:
                score+=(base1+base2+base3)
                base1, base2, base3 =0, 0,1
            else:
                score+=(base1+base2+base3+1)
                base1,base2,base3=0,0,0
            idx+=1
            if idx==9: idx=0
    result=max(result,score)
print(result)