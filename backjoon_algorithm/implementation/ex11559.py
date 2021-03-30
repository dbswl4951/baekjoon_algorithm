#Puyo Puyo
'''
같은 뿌요를 찾고, 떨어트릴 배열에 저장 하는 것 까지 했으나
밑에 빈 칸이 있으면 떨어트리고 없으면 그 위에 쌓는 작업을 하지 못해서 찾아봤다.
'''
import sys
from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

#뿌요들이 내려오게 하는 함수
def down():
    for i in range(10,-1,-1):
        for j in range(6):
            #블럭 밑에 빈 칸이 있다면 떨어트린다
            if board[i][j]!='.' and board[i+1][j]=='.':
                for k in range(i+1,12): #k : 아래로 떨어지는 것을 나타내기 위한 변수
                    if k==11 and board[k][j]=='.':
                        board[k][j]=board[i][j]
                    #board[k][j]가 빈 칸이 아닐 때 까지 k를 증가시켜 내려간다음, 빈 칸이 아닌 칸 바로 위에 뿌요를 놓음.
                    #뿌요를 위에 쌓은 후 더이상 내려 갈 필요 없으므로 break
                    elif board[k][j]!='.':
                        board[k-1][j]=board[i][j]
                        break
                board[i][j]='.'

#같은 색의 뿌요 터트리기
def bfs(x,y,color):
    global result,flag
    count=1 #color와 같은 색의 뿌요 개수
    sameColor=[[x,y]]    #같은 색의 뿌요를 담는 list
    visited[x][y]=1
    q=deque()
    q.append([x,y])
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<12 and 0<=ny<6 and board[nx][ny]==color and visited[nx][ny]==0:
                visited[nx][ny]=1
                count+=1
                q.append([nx,ny])
                sameColor.append([nx,ny])
    if count>=4:
        flag=1
        for sc in sameColor:
            x,y=sc
            board[x][y]='.'

board=[]
for _ in range(12):
    board.append(list(sys.stdin.readline().strip()))
result=0
while True:
    visited=[[0]*6 for _ in range(12)]
    flag=0  #연쇄가 일어났는지 확인하는 변수
    for i in range(11,-1,-1):
        for j in range(6):
            if board[i][j]!='.' and visited[i][j]==0:
                bfs(i,j,board[i][j])
    if flag==1: result+=1   #연쇄가 일어났으면 result+=1
    else: break #더이상 터트릴 뿌요가 없으면 break
    #터진 후, 뿌요들이 내려가게 함
    down()
print(result)