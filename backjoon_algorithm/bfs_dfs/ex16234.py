#인구 이동
'''
1차 시도 : dfs => 실패
힌트 본 후 2차 시도: bfs
'''
import sys
from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    q=deque()
    q.append([x,y])
    temp=[] #이동 할 수 있는 모든 국가들 저장
    temp.append([x,y])
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==0:
                if l<=abs(nation[nx][ny]-nation[x][y])<=r:
                    visited[nx][ny]=1
                    q.append([nx,ny])
                    temp.append([nx,ny])
    return temp

n,l,r=map(int,sys.stdin.readline().split())
nation=[]
for i in range(n):
    nation.append(list(map(int,sys.stdin.readline().split())))
result=0
while True:
    visited=[[0]*n for _ in range(n)]
    isTrue=False
    for i in range(n):
        for j in range(n):
            if visited[i][j]==0:
                visited[i][j]=1
                temp=bfs(i,j)
                if len(temp)>1:    #이동 할 수 있는 국가가 하나라도 있으면 인구이동
                    isTrue=True
                    num=sum(nation[x][y] for x,y in temp)//len(temp)
                    for x,y in temp:
                        nation[x][y]=num
    if not isTrue:  #더 이상 이동 할 수 없으면 break
        break
    result+=1
print(result)


#1차 시도 (실패)
'''
dx=[-2,2,0,0]
dy=[0,0,-2,2]

def dfs(x,y):
    global sumVal
    sumVal+=nation[x][y]
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<2*n-1 and 0<=ny<2*n-1 and visited[nx][ny]==0:
            if ny!=2*n-2 and nation[nx][ny+1]==0:    #국경선이 열려있다면
                visited[nx][ny] = 1
                dfs(nx,ny)
            if nx!=2*n-2 and nation[nx+1][ny]==0:
                visited[nx][ny] = 1
                dfs(nx,ny)

n,l,r=map(int,sys.stdin.readline().split())
nation=[]
for i in range(2*n-1):
    if i%2!=0:
        nation.append([-1]*n)
    else:
        nation.append(list(map(int,sys.stdin.readline().split())))
    for j in range(2*n-1):
        if j%2!=0:
            nation[i].insert(j,-1)
visited=[[0]*(2*n-1) for _ in range(2*n-1)]
#인구 차이 계산 후 국경 열기
for i in range(2*n-1):
    for j in range(2*n-1):
        if i%2==0 and j%2==0:
            if j!=2*n-2 and l<=abs(nation[i][j]-nation[i][j+2])<=r:
                nation[i][j+1]=0    #국경 열기 (-1:닫힘,0:열림)
            if i!=2*n-2 and l<=abs(nation[i][j]-nation[i+2][j])<=r:
                nation[i+1][j]=0    #국경 열기
for i in range(2*n):
    for j in range(2*n):
        sumVal=0
        if i%2==0 and j%2==0 and visited[i][j]==0:
            visited[i][j]=1
            dfs(i,j)
'''