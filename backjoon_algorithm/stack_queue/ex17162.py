# 가희의 수열놀이 (Small)
import sys

n,mod = map(int,sys.stdin.readline().split())
q,mList,idx = [],[[] for _ in range(mod)],0
for _ in range(n):
    temp = sys.stdin.readline().strip()
    tmp = list(map(int,temp.split(' ')))

    if tmp[0]==1:
        m = tmp[1]%mod
        q.append(tmp[1])
        mList[m].append(idx)
        idx += 1
    elif tmp[0]==2 and q:
        num = q.pop()
        mList[num%mod].pop()
        idx -= 1
    elif tmp[0]==3:
        if len(q)<mod: print(-1)
        else:
            minIdx = int(1e9)
            for i in range(mod):
                if not mList[i]:
                    print(-1)
                    break
                minIdx = min(minIdx,mList[i][-1])
            else: print(idx-minIdx)