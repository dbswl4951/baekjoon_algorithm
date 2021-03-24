#마법사 상어와 토네이도
import sys

#좌하우상
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

#모래가 이동 할 좌표가 격자안에 있는지 검사
def storm(x,y,sand):
    global result
    #격자 안 => 지도의 모래양 갱신
    if 0<=x<n and 0<=y<n:
        board[x][y]+=sand
    else:
        result+=sand

n=int(sys.stdin.readline().strip())
board=[list(map(int,sys.stdin.readline().split()))for _ in range(n)]
x,y=n//2,n//2
#dir:방향, cnt:한 방향으로 이동한 칸 갯수, reuslt:칸 밖으로 나간 모래 양
#m:2 될때마다 move 1 증가시키는 변수, move: 이동해야 하는 칸 갯수
dir,cnt,result,m,move=0,0,0,0,1

while True:
    nx,ny=x+dx[dir],y+dy[dir]
    if board[nx][ny]:
        # 비율에 따른 모래 양 구하기
        p1 = int(board[nx][ny] * 0.01)
        p2 = int(board[nx][ny] * 0.02)
        p5 = int(board[nx][ny] * 0.05)
        p7 = int(board[nx][ny] * 0.07)
        p10 = int(board[nx][ny] * 0.1)
        rem = board[nx][ny] - 2 * (p1 + p2 + p7 + p10) - p5

        # 모래가 이동 할 좌표 구하기
        xu_p1, yu_p1 = x + dx[(dir + 3) % 4], y + dy[(dir + 3) % 4]
        xd_p1, yd_p1 = x + dx[(dir + 1) % 4], y + dy[(dir + 1) % 4]
        nxu_p2, nyu_p2 = nx + 2 * dx[(dir + 3) % 4], ny + 2 * dy[(dir + 3) % 4]
        nxd_p2, nyd_p2 = nx + 2 * dx[(dir + 1) % 4], ny + 2 * dy[(dir + 1) % 4]
        nxu_p7, nyu_p7 = nx + dx[(dir + 3) % 4], ny + dy[(dir + 3) % 4]
        nxd_p7, nyd_p7 = nx + dx[(dir + 1) % 4], ny + dy[(dir + 1) % 4]
        tx, ty = nx + dx[dir], ny + dy[dir]
        txu_p10, tyu_p10 = tx + dx[(dir + 3) % 4], ty + dy[(dir + 3) % 4]
        txd_p10, tyd_p10 = tx + dx[(dir + 1) % 4], ty + dy[(dir + 1) % 4]
        txf_p5, tyf_p5 = tx + dx[dir], ty + dy[dir]

        #좌표가 격자 칸 안에 있는지 검사, 있으면 모래 이동
        storm(tx,ty,rem)
        storm(xu_p1,yu_p1,p1)
        storm(xd_p1,yd_p1,p1)
        storm(nxu_p2,nyu_p2,p2)
        storm(nxd_p2,nyd_p2,p2)
        storm(nxu_p7,nyu_p7,p7)
        storm(nxd_p7,nyd_p7,p7)
        storm(txu_p10,tyu_p10,p10)
        storm(txd_p10,tyd_p10,p10)
        storm(txf_p5,tyf_p5,p5)

    if x==0 and y==0: break
    board[nx][ny]=0
    x,y=nx,ny
    #한 방향으로 이동 한 칸 갯수+1
    cnt+=1
    #이동해야 할 횟수(move)를 다 이동했으면
    if cnt==move:
        #방향 변경
        dir=(dir+1)%4
        cnt=0
        m+=1
        if m%2==0:
            move+=1
            m=0

print(result)