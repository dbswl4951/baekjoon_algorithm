#마법사 상어와 토네이도

dx = [0,1,0,-1]
dy = [-1,0,1,0]

def check(x,y,sand):
    global result

    if 0<=x<n and 0<=y<n:
        board[x][y] += sand
    else: result += sand

n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
x,y,result,dirCnt = n//2,n//2,0,1

# 큰 회전 (상하좌우)
for k in range(n//2+1):
    moveCnt,flag = 0,0
    # 상,하,좌,우 하나씩 이동
    for i in range(4):
        for j in range(dirCnt):
            nx,ny = x+dx[i],y+dy[i]
            sand = board[nx][ny]
            nnx, nny = nx+dx[i],ny+dy[i]

            if board[nx][ny]:
                # 현재 이동방향에 따라 모래 이동방향이 달라짐
                if i==0 or i==2: d1,d2 = 1,3
                else: d1,d2 = 0,2

                oneX1, oneX2, oneY1, oneY2 = x+dx[d1],x+dx[d2],y+dy[d1],y+dy[d2]
                sevenX1, sevenX2, sevenY1, sevenY2 = nx+dx[d1],nx+dx[d2],ny+dy[d1], ny+dy[d2]
                twoX1, twoX2, twoY1, twoY2 = sevenX1+dx[d1], sevenX2+dx[d2], sevenY1+dy[d1], sevenY2+dy[d2]
                tenX1, tenX2, tenY1, tenY2 = nnx+dx[d1], nnx+dx[d2], nny+dy[d1], nny+dy[d2]
                fiveX, fiveY = nnx+dx[i], nny+dy[i]
                onePer, sevenPer, twoPer, tenPer, fivePer = int(sand*0.01), int(sand*0.07), int(sand*0.02), int(sand*0.1), int(sand*0.05)
                alpaPer = sand - 2 * (onePer+sevenPer+twoPer+tenPer) - fivePer

                # 범위 확인하고 모래 이동시키기
                check(oneX1,oneY1,onePer); check(oneX2,oneY2,onePer)
                check(sevenX1,sevenY1,sevenPer); check(sevenX2,sevenY2,sevenPer)
                check(twoX1,twoY1,twoPer); check(twoX2,twoY2,twoPer)
                check(tenX1,tenY1,tenPer); check(tenX2,tenY2,tenPer)
                check(fiveX,fiveY,fivePer); check(nnx,nny,alpaPer)
                board[nx][ny] = 0

            if nx==0 and ny==0: flag=1; break
            x, y = nx, ny
        if flag: break
        moveCnt += 1
        if moveCnt != 0 and moveCnt % 2 == 0: dirCnt += 1
    if flag: break

print(result)