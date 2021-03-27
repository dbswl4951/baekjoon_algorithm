#주사위 굴리기
'''
dice[0]은 항상 아래면이, dice[5]는 항상 윗면이 되게 갱신

어떻게 구현해야 할지 감이 안와서 힌트 참조 후 문제 풀이
'''
import sys

#동,서,북,남
dx=[0,0,-1,1]
dy=[1,-1,0,0]

def startGame():
    global x,y
    for order in orders:
        print("order:",order)
        d=order-1
        nx,ny=x+dx[d],y+dy[d]
        if not 0<=nx<n or not 0<=ny<m:
            continue
        if d==0:    #동쪽
            dice[0],dice[2],dice[3],dice[5]=dice[3],dice[0],dice[5],dice[2]
        elif d==1:  #서쪽
            dice[0],dice[2],dice[3],dice[5]=dice[2],dice[5],dice[0],dice[3]
        elif d==2:  #북쪽
            dice[0],dice[1],dice[4],dice[5] =dice[4],dice[0],dice[5],dice[1]
        else:   #남쪽
            dice[0],dice[1],dice[4],dice[5] =dice[1],dice[5],dice[0],dice[4]
        if board[nx][ny]==0:
            board[nx][ny]=dice[0]
        else:
            dice[0]=board[nx][ny]
            board[nx][ny]=0
        print("dice:",dice)
        x,y=nx,ny
        print(dice[5])

n,m,x,y,k=map(int,sys.stdin.readline().split())
board=[]
for _ in range(n):
    board.append(list(map(int,sys.stdin.readline().split())))
orders=list(map(int,sys.stdin.readline().split()))
dice=[0 for _ in range(6)]
startGame()