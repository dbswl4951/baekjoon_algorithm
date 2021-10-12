#문자열 게임 2
import sys
from collections import deque

t = int(sys.stdin.readline().strip())

for _ in range(t):
    string = sys.stdin.readline().strip()
    k = int(sys.stdin.readline().strip())
    indexDic,shortDic,longDict = {},{},{}

    for i,s in enumerate(string):
        if s not in indexDic:
            indexDic[s] = deque([i])
        else:
            if len(indexDic[s])>=k:
                indexDic[s].popleft()
            indexDic[s].append(i)

        if len(indexDic[s])==k:
            num = indexDic[s][-1]-indexDic[s][0]+1
            if s not in shortDic:
                shortDic[s] = num
            else:
                shortDic[s] = min(num,shortDic[s])
            if s not in longDict:
                longDict[s] = num
            else:
                longDict[s] = max(num,longDict[s])

    if not shortDic or not longDict: print(-1)
    else:
        sd = sorted(shortDic.values())
        ld = sorted(longDict.values(),reverse=True)
        print(sd[0],end=' ')
        print(ld[0])