#섬의 개수
'''
dfs 사용
실수때문에 실수 고치느라 시간을 좀 썼지만 맞음!
'''
import sys
sys.setrecursionlimit(30000)

dx=[-1,-1,-1,0,0,1,1,1]
dy=[-1,0,1,-1,1,-1,0,1]

def dfs(i,x,y):
    global allVisitied
    for j in range(8):
        nx=x+dx[j]
        ny=y+dy[j]
        if 0<=nx<len(allMap[i]) and 0<=ny<len(allMap[i][x]):
            if allVisitied[i][nx][ny]==0 and allMap[i][nx][ny]==1:
                allVisitied[i][nx][ny]=1
                dfs(i,nx,ny)

allMap=[]
allVisitied=[]
n=0
while True: #테스트 케이스 입력 받음
    w, h = map(int, input().split())
    if w==0 and h==0:
        break
    littleMap = []
    for _ in range(h):
        littleMap.append(list(map(int,input().split())))
    allMap.append(littleMap)
    n+=1
    visited = [[0] * w for _ in range(h)]
    allVisitied.append(visited)

result=[]
for i in range(len(allMap)):
    count=0
    for j in range(len(allMap[i])):
        for k in range(len(allMap[i][j])):
            if allMap[i][j][k]==1 and allVisitied[i][j][k]==0:
                dfs(i,j,k)
                count+=1
    print(count)
