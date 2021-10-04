#탈출
'''
DFS로 탐색하기엔 t값이 너무 커서 시간초과 발생
'''
import sys
from collections import deque

def bfs():
    q = deque()
    q.append([n,0])
    visited = [0]*100000
    visited[n] = 1

    while q:
        x,cnt = q.popleft()
        if cnt>t: return 'ANG'
        if x==g: return cnt

        # A 버튼
        if x+1<=99999 and not visited[x+1]:
            visited[x+1] = 1
            q.append([x+1,cnt+1])

        # B 버튼
        if x*2<=99999:
            temp = str(x*2)
            if int(temp)!=0:
                temp = str(int(temp[0])-1)+temp[1:]
            temp = int(temp)
            if not visited[temp]:
                visited[temp] = 1
                q.append([temp,cnt+1])

    return 'ANG'

n,t,g = map(int,sys.stdin.readline().split())
print(bfs())