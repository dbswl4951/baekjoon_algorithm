#뱀
import sys
from collections import deque

#북,동,남,서
dx=[-1,0,1,0]
dy=[0,1,0,-1]

def chageDirection(direction,d):    #방향 전환
    if direction=='D':  #오른쪽 회전
        d=(d+1)%4
    else:   #왼쪽 회전
        d=(d-1)%4
    return d

def startGame(nx,ny,d):
    global times
    snake=deque()
    snake.append([1,1])
    while True:
        times+=1
        nx,ny=nx+dx[d],ny+dy[d]
        if times in change.keys():  #방향 전환
            d=chageDirection(change[times],d)
        if 0<nx<n+1 and 0<ny<n+1:
            if [nx,ny] in snake:    #몸에 부딪힌 경우
                break
            if board[nx][ny]==1:    #사과가 있는 경우
                board[nx][ny]=0
                snake.append([nx,ny])
            else:   #사과가 없는 경우
                snake.append([nx,ny])
                snake.popleft()
        else: break
    print(times)
    return

n=int(sys.stdin.readline().strip()) #보드의 크기
an=int(sys.stdin.readline().strip())    #사과 개수
board=[[0]*(n+1) for _ in range(n+1)]
for _ in range(an): #사과 위치 저장
    x,y=map(int,sys.stdin.readline().split())
    board[x][y]=1
cn=int(sys.stdin.readline().strip()) #뱀의 방향 전환 개수
change={}   #dict형
for _ in range(cn):
    x,c = sys.stdin.readline().split()
    change[int(x)]=c
times=0
startGame(1,1,1)    #(머리x,머리y,동쪽방향)