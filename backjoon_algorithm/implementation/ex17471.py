#게리맨더링
'''
1. dfs로 구역을 n//2개 뽑기
2. 뽑은 구역들 bfs로 돌면서 인구수 세기 (2번 실행)
3. 인구수1-인구수2 최솟값으로 갱신

< 느낀점 >
- (1)번을 생각하기 어려웠던 것 같다.
- 처음에 bfs로 선거구 1개를 돌고, (전체 인구수-선거구1 인구수)로 인구 차이 최솟값을 구할려고 했는데,
    그러면 인접해있지 않은 구역을 탐색 할 때, 제대로 탐색이 되지 X
    따라서 선거구1, 선거구2 따로 bfs를 돌려서 총 2번을 실행해야 함!
'''
from collections import deque

def bfs(group):
    q=deque()
    q.append(group[0])
    visited=[0]*n
    visited[group[0]]=1
    cnt,peopleCnt = 0,0

    while q:
        x=q.popleft()
        for i in graph[x]:
            if i in group and not visited[i]:
                visited[i]=1
                q.append(i)

    for i in range(n):
        if visited[i]:
            cnt+=1
            peopleCnt+=people[i]

    if cnt==len(group): return peopleCnt
    return 0

def dfs(cnt,x,end):
    global result

    if cnt==end:
        group1,group2=deque(),deque()
        for i in range(n):
            if check[i]: group1.append(i)
            else: group2.append(i)
        peopleCnt=bfs(group1)
        peopleCnt2=bfs(group2)
        if peopleCnt==0 or peopleCnt2==0: return
        result=min(result,abs(peopleCnt-peopleCnt2))
        return

    # x를 안 넣어주면 시간초과
    # x를 안 넣어줬을 경우 : 0,1 선택 한 걸 확인하고 1,0 선택도 확인 함
    for i in range(x,n):
        if check[i]: continue
        check[i]=1
        dfs(cnt+1,i,end)
        check[i]=0

n=int(input().strip())
people=list(map(int,input().split()))
graph=[[] for _ in range(n)]
for i in range(n):
    temp=list(map(int,input().split()))[1:]
    for t in temp:
        graph[i].append(t-1)

result=int(1e9)
# 몇개의 구역을 선택 할 것인지
for i in range(1,n//2+1):
    check=[0]*n
    dfs(0,0,i)
if result==int(1e9): print(-1)
else: print(result)