#연구소
'''
bfs 사용
1. 벽을 세울 위치 정한 후, 벽 세움
2. 바이러스 퍼트림
3. 0이 있는 방 몇개인지 조사
정답 비율이 높고 골드5였는데도 처음에 벽을 세울 곳을 정하는게 어려웠다.
더 많은 문제를 풀어 볼 것!
'''
import sys,copy
from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs():
    global result
    q=deque()
    count = 0
    copyArea=copy.deepcopy(area)

    for i in range(n):
        for j in range(m):
            if copyArea[i][j]==2:
                q.append([i,j]) #바이러스가 있는 위치 저장
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and copyArea[nx][ny]==0:
                copyArea[nx][ny]=2  #바이러스 퍼짐
                q.append([nx,ny])
    for i in copyArea:
        for j in i:
            if j==0: count+=1
    result =max(result,count)

def wall(cnt):
    if cnt == 3:  #벽을 3개 세우면
        bfs()   #바이러스 퍼트림
        return
    for i in range(n):
        for j in range(m):
            if area[i][j] == 0:
                area[i][j] = 1
                wall(cnt + 1)
                area[i][j] = 0

n,m = map(int,sys.stdin.readline().split())
area=[]
for i in range(n):
    area.append(list(map(int,sys.stdin.readline().rsplit())))
result=0
wall(0)
print(result)