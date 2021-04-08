#드래곤 커브
'''
동:0, 서:2, 남:3, 북:1
0세대: 0
1세대: 0, 1
2세대: 0, 1, 2, 1
3세대: 0, 1, 2, 1, 2, 3, 2, 1
4세대: 0, 1, 2, 1, 2, 3, 2, 1, 2, 3, 0, 3, 2, 3, 2, 1
=> 전 세대들에 1을 더하고 뒤집어준 형식
'''
import sys
from collections import deque

dx=[1,0,-1,0]
dy=[0,-1,0,1]

# 세대 커브마다 방향 구하기
def getDirections(directions):
    temp=[]
    for i in range(len(directions)-1,-1,-1):
        temp.append((directions[i]+1)%4)
    return directions+temp

def start(curve):
    q=deque()
    for c in curve:
        q.append(c)
        xy.add((c[0],c[1]))

    while q:
        x,y,d,g=q.popleft()
        directions = [d]
        # g세대의 모든 방향 저장
        for _ in range(g):
            directions = getDirections(directions)
        for i in range(2**g):
            nx,ny=x+dx[directions[i]],y+dy[directions[i]]
            if 0<=nx<=100 and 0<=ny<=100:
                xy.add((nx,ny))
                x,y=nx,ny

# 정사각형 개수 구하기
def countRectangle():
    result=0
    for x,y in xy:
        if (x+1,y) in xy and (x,y+1) in xy and (x+1,y+1) in xy:
            result+=1
    return result

n=int(sys.stdin.readline().strip())
curve=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
xy = set()  # 들리는 모든 (x,y)좌표 저장
start(curve)
print(countRectangle())