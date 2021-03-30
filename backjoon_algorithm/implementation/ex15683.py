#감시
'''
각 cctv를 회전해서 탐색 할 수 있는 모든 방향 경우에 대해 탐색해야 함
브루트포스 + DFS

골드5가 맞나? 싶을 정도로 너무 어려웠다..
'''
import sys,copy
from collections import deque

dx=[0,0,-1,1]
dy=[-1,1,0,0]
#1,2,..번 카메라에서 탐색 할 수 있는 방향을 dx,dy의 index로 가짐
direction = [0,[[0],[1],[2],[3]],[[0,1],[2,3]],[[1,2],[1,3],[0,2],[0,3]],
             [[0,1,2],[0,1,3],[0,2,3],[1,2,3]],[[0,1,2,3]]]
minVal=int(1e9)

def dfs(start,room,cctv):
    global minVal
    #cctv 끝까지 다 탐색하면 사각지대 개수 저장 후 return => 그 전 bfs 함수로 돌아간다.
    if start==len(cctv):
        cnt=0
        for i in range(n):
            for j in range(m):
                if room[i][j]==0: cnt+=1
        minVal=min(minVal,cnt)
        return

    #cctv를 회전시켜서 탐색 할 수 있는 모든 방향 탐색
    num,x,y=cctv[start]
    for d in direction[num]:
        temp=copy.deepcopy(room)
        for i in d:
            nx,ny=x+dx[i],y+dy[i]
            while 0<=nx<n and 0<=ny<m:
                if temp[nx][ny]==6: #벽 마주치면 그 방향으로 가는거 stop => 다른 cctv 탐색(bfs)으로 이동
                    break
                if temp[nx][ny]==0: #빈 칸이면 감시 할 수 있다는 표시(#)
                    temp[nx][ny]='#'
                nx+=dx[i]
                ny+=dy[i]
        dfs(start+1,temp,cctv)

n,m=map(int,sys.stdin.readline().split())
room=[]
for _ in range(n):
    room.append(list(map(int,sys.stdin.readline().split())))
cctv=deque()
#CCTV 위치 cctv 큐에 저장
for i in range(n):
    for j in range(m):
        if room[i][j] in [1,2,3,4,5]:
            cctv.append([room[i][j],i,j])   #(cctv 종류, x좌표, y좌표)
dfs(0,room,cctv)
print(minVal)


#1차 시도 : CCTV마다 다른 리스트를 만들어서 BFS로 구현 => 반례 발생. 실패
'''
dx1,dy1=[0,1,0,-1],[1,0,-1,0]
dx2,dy2=[[0,0],[-1,1]],[[1,-1],[0,0]]
dx3,dy3=[[-1,0],[0,1],[1,0],[0,-1]],[[0,1],[1,0],[0,-1],[-1,0]]
dx4,dy4=[[0,-1,0],[-1,0,1],[0,1,0],[-1,0,1]],[[-1,0,1],[0,1,0],[-1,0,1],[0,-1,0]]
dx5,dy5=[-1,0,1,0],[0,1,0,-1]

def bfs(room,no,x,y):
    count=0
    returnRoom=copy.deepcopy(room)
    if no==1:
        for i in range(4):
            copyRoom = copy.deepcopy(room)
            nx, ny = x, y
            cnt = 0
            while True:
                nx,ny=nx+dx1[i],ny+dy1[i]
                if 0<=nx<n and 0<=ny<m and room[nx][ny]!=6:
                    if room[nx][ny]==0:
                        cnt+=1
                        copyRoom[nx][ny]=-1
                else: break
            if count<cnt:
                count=cnt
                returnRoom=copy.deepcopy(copyRoom)
    elif no==2:
        for i in range(2):
            copyRoom = copy.deepcopy(room)
            cnt = 0
            for j in range(2):
                nx, ny = x, y
                while True:
                    nx,ny=nx+dx2[i][j],ny+dy2[i][j]
                    if 0<=nx<n and 0<=ny<m and room[nx][ny]!=6:
                        if room[nx][ny] == 0:
                            cnt+=1
                            copyRoom[nx][ny] = -1
                    else: break
            if count < cnt:
                count = cnt
                returnRoom=copy.deepcopy(copyRoom)
    elif no==3:
        for i in range(4):
            copyRoom = copy.deepcopy(room)
            cnt = 0
            for j in range(2):
                nx, ny = x, y
                while True:
                    nx,ny=nx+dx3[i][j],ny+dy3[i][j]
                    if 0<=nx<n and 0<=ny<m and room[nx][ny]!=6:
                        if room[nx][ny] == 0:
                            cnt+=1
                            copyRoom[nx][ny] = -1
                    else: break
            if count < cnt:
                count = cnt
                returnRoom=copy.deepcopy(copyRoom)
    elif no==4:
        for i in range(4):
            copyRoom = copy.deepcopy(room)
            cnt = 0
            for j in range(3):
                nx, ny = x, y
                while True:
                    nx,ny=nx+dx4[i][j],ny+dy4[i][j]
                    if 0<=nx<n and 0<=ny<m and room[nx][ny]!=6:
                        if room[nx][ny] == 0:
                            cnt+=1
                            copyRoom[nx][ny] = -1
                    else: break
            if count < cnt:
                count = cnt
                returnRoom=copy.deepcopy(copyRoom)
    else:
        cnt = 0
        copyRoom = copy.deepcopy(room)
        for i in range(4):
            nx, ny = x, y
            while True:
                nx,ny=nx+dx5[i],ny+dy5[i]
                if 0<=nx<n and 0<=ny<m and room[nx][ny]!=6:
                    if room[nx][ny] == 0:
                        cnt+=1
                        copyRoom[nx][ny] = -1
                else: break
        if count < cnt:
            count = cnt
            returnRoom=copy.deepcopy(copyRoom)
    return returnRoom

def simulation():
    global room
    while cctv:
        no,x,y=cctv.popleft()
        returnRoom=bfs(room,no,x,y)
        room=copy.deepcopy(returnRoom)

n,m=map(int,sys.stdin.readline().split())
room=[]
for _ in range(n):
    room.append(list(map(int,sys.stdin.readline().split())))
cctv=deque()
#CCTV 위치 cctv 큐에 저장
for i in range(n):
    for j in range(m):
        if room[i][j] in [1,2,3,4,5]:
            cctv.append([room[i][j],i,j])   #(cctv 종류, x좌표, y좌표)
simulation()
result=0
for i in range(n):
    for j in range(m):
        if room[i][j]==0:
            result+=1
print(result)
'''