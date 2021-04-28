#마법사 상어와 비바라기
'''
2021 상반기 삼성 오후 문제
'''

dx=[0,-1,-1,-1,0,1,1,1]
dy=[-1,-1,0,1,1,1,0,-1]

def moveCloud(cloud,move):
    d,s=move
    check=[[0]*n for _ in range(n)]

    # 모든 구름 이동
    for i in range(len(cloud)):
        x,y=cloud[i]
        nx,ny=x+dx[d]*s,y+dy[d]*s
        while True:
            if 0<=nx<n and 0<=ny<n: break
            if ny<0: ny+=n
            elif ny>=n: ny-=n
            if nx<0: nx+=n
            elif nx>=n: nx-=n
        cloud[i]=[nx,ny]
        board[nx][ny]+=1
        check[nx][ny]=1

    # 대각선 확인
    for i in range(len(cloud)):
        x, y = cloud[i]
        for j in range(1,8,2):
            nx,ny=x+dx[j],y+dy[j]
            if 0<=nx<n and 0<=ny<n and board[nx][ny]>0:
                board[x][y]+=1

    newCloud=[]
    # 새로운 구름 생성
    for i in range(n):
        for j in range(n):
            if board[i][j]>=2 and not check[i][j]:
                board[i][j]-=2
                newCloud.append([i,j])
    return newCloud

n,m=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(n)]
move=[]     #(방향, 속력)
cloud=[[n-1,0],[n-1,1],[n-2,0],[n-2,1]]
for _ in range(m):
    d,s=map(int,input().split())
    move.append([d-1,s])

for i in range(m):
    cloud=moveCloud(cloud,move[i])

result=0
for b in board:
    result+=sum(b)
print(result)