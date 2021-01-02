#중량 제한
'''
이분탐색 + BFS 사용
1. 이분 탐색으로 무게를 찾으면서 start->end까지 도착이 가능한지 bfs로 검사
 이분 탐색 범위 : 중량 (mid)
2. 탐색 중 가장 최댓값 출력

BFS까지만 생각하고 BFS에 이분탐색을 접목시키는건 생각 못 함.
풀이를 보면 간단한데 왜 못 푸는걸까!!
'''
import sys
from collections import deque

def bfs(mid):
    visitied[fac1-1]=1    #시작점은 이미 주어져있음
    q=deque()
    q.append(fac1-1)
    while q:
        x=q.popleft()
        if x==fac2-1: #도착점에 도달
            return True
        for nx,nz in island[x]: #nx:다음 방문 할 섬, nz:다리 무게 중량
            if visitied[nx]==0 and mid<=nz: #제한 한 중량 이상만 방문
                visitied[nx]=1
                q.append(nx)
    return False    #큐를 다 돌았는데도 도착점에 도착하지 못함

n,m=map(int,sys.stdin.readline().split())
island=[[] for _ in range(n)]    #이어진 섬,다리 중량 제한 저장
for i in range(m):
    x,y,z=map(int,sys.stdin.readline().split())
    island[x-1].append([y-1,z])
    island[y-1].append([x-1,z])
fac1,fac2=map(int,sys.stdin.readline().split()) #공장이 있는 섬
start,end=1,1000000000

while start<=end:
    visitied=[0 for i in range(n)]
    mid=(start+end)//2  #중량 제한
    # 만약 현재 중량 제한으로 도착점에 도달 했다면, 최댓값을 구하기 위해 중량 제한을 올린다
    if bfs(mid):
        start=mid+1
    else:
        end=mid-1
print(end)