#봄버맨
'''
1. 폭탄을 설치할 때, 현재 몇 초인지도 같이 저장 (-9:빈 칸)
2. 폭탄을 터트릴 때 같이 저장했던 시간이 3초 뒤라면 터트린다
'''

#원래 위치, 위,왼쪽,아래,오른쪽
dx=[0,-1,0,1,0]
dy=[0,0,-1,0,1]

def fill(num):  #짝수초일때는 모든 칸에 폭탄 있음
    for i in range(r):
        for j in range(c):
            if board[i][j][0]=='.':
                board[i][j][0],board[i][j][1]='O',num

def boom(num):  #홀수 초 일 때 폭탄 터트림
    list=[]
    for i in range(r):
        for j in range(c):
            if board[i][j][0]=='O' and num==board[i][j][1]+3:
                for k in range(5):  #모든 방향 탐색
                    if 0<=i+dx[k]<r and 0<=j+dy[k]<c:
                        list.append([i+dx[k],j+dy[k]])    #폭탄이 터질 곳을 list에 담음
    for x,y in list:
        board[x][y][0],board[x][y][1]='.',-9    #폭탄이 터진 곳을 빈칸으로 변경

def solve(num):
    if num>n:
        for i in range(r):
            temp=''
            for j in range(c):
                temp+=board[i][j][0]
            print(temp)
        return
    if num%2==0:    #짝수 초 일 때
        fill(num)
        solve(num+1)
    else:   #홀수 초 일 때
        boom(num)
        solve(num + 1)

r,c,n=map(int,input().split()) #행,열,초
board=[]
for i in range(r):
    temp = []
    for j in input():
        if j == 'O':
            temp.append(['O', 0])
        else:
            temp.append(['.', -9])
    board.append(temp)
solve(2)