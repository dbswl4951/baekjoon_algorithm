# Strahler 순서
'''
위상 정렬 변형 문제

100%에서 계속 틀렸다고 나와서 반례 찾느라 오래 걸린 문제!
'''
import sys
from collections import deque

def tSort():
    q=deque()
    for i in range(1,m+1):  #진입 차수 0이면 큐에 삽입 & strahler=1로 설정
        if indgree[i]==0:
            q.append(i)
            strahler[i]=1
    temp=0
    while q:
        now=q.popleft()
        for i in graph[now]:    #현재 노드에서 연결된 노드 탐색
            indgree[i]-=1
            if strahler[i]==0:  #처음 strahler 값을 설정하는 거라면 그 전 노드 값으로 갱신
                strahler[i]=strahler[now]
                temp=strahler[now]  #다음에 i노드로 올 strahler값과 비교하기 위해 temp 변수에 저장
            else:   #이미 설정 된 strahler값이 있고
                if strahler[now]==temp: #그 전 결과 값인 temp와 현재 노드의 strahler값이 일치 한다면
                    strahler[i]=strahler[now]+1 #strahler가 x인 값이 2개 이상이므로 strahler+=1
                else:   #그 전 결과 값인 temp와 같지 않다면 이미 있던 strahler값과 현재 노드의 strahler값을 비교해 큰 값으로 갱신
                    strahler[i]=max(strahler[i],strahler[now])
            if indgree[i]==0:
                q.append(i)

t = int(sys.stdin.readline().strip())
result=[]
for i in range(t):
    k, m, p = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(m + 1)]
    indgree=[0]*(m+1)
    for _ in range(p):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        indgree[b]+=1
    strahler=[0]*(m+1)  #strahler순서
    tSort()
    result.append([k,strahler[m]])
for r in result:
    print(*r)