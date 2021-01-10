#ACM Craft
'''
dp + 위상정렬
'''
import sys
from collections import deque

t=int(sys.stdin.readline().strip())
result=[]
for _ in range(t):
    n,k=map(int,sys.stdin.readline().split())
    time=[0]+list(map(int,sys.stdin.readline().split()))
    rule=[[] for _ in range(n+1)]   #건물 순서 규칙
    inDegree=[0]*(n+1)  #진입 차수
    dp=[0]*(n+1)    #건물까지 걸리는 시간
    for _ in range(k):  #건설 규칙 저장
        x,y=map(int,sys.stdin.readline().split())
        rule[x].append(y)
        inDegree[y]+=1
    w=int(sys.stdin.readline().strip()) #건설 해야 할 건물의 번호
    q=deque()
    for i in range(1,n+1):  #진입차수 0 큐에 넣기
        if inDegree[i]==0:
            q.append(i)
            dp[i]=time[i]   #해당 건물의 건설 시간 넣기

    while q:
        x=q.popleft()
        for i in rule[x]:
            inDegree[i]-=1  #진입차수 -1
            dp[i]=max(dp[i],dp[x]+time[i])  #건설 비용 갱신
            if inDegree[i]==0:
                q.append(i)
    result.append(dp[w])

for i in result:
    print(i)