#새로운 게임2

dx = [0,0,-1,1]
dy = [1,-1,0,0]

# 방향 반대로 변경
def changeDir(d):
    if d==0: return 1
    elif d==1: return 0
    elif d==2: return 3
    else: return 2

# 말 이동
def moveHorses():
    for idx,loc in enumerate(horseLoc):
        x,y,d = loc
        nx,ny = x+dx[d],y+dy[d]
        temp,flag,f = [],0,0

        # 자신부터 위에있는 모든 말들 구하기
        for i in range(n):
            for j in range(n):
                for k in range(len(horses[i][j])):
                    if horses[i][j][k][0]==idx:
                        temp = horses[i][j][k:]
                        del horses[i][j][k:]
                        flag = 1
                        break
                if flag: break
            if flag: break

        # 범위 밖 or 파란색 칸
        if not 0<=nx<n or not 0<=ny<n or board[nx][ny]==2:
            d = changeDir(d)
            nx,ny = x+dx[d],y+dy[d]

        if 0<=nx<n and 0<=ny<n and board[nx][ny]!=2:

            # 빨간색 칸
            if board[nx][ny] == 1:
                temp.reverse()
                f = 1
            for ix,t in enumerate(temp):
                if f and ix==len(temp)-1: t[1]=d
                elif not f and ix==0: t[1] = d
                horseLoc[t[0]] = [nx,ny,t[1]]
                horses[nx][ny].append(t)
        else:
            for ix, t in enumerate(temp):
                if f and ix == len(temp) - 1: t[1] = d
                elif not f and ix == 0: t[1] = d
                horseLoc[t[0]] = [x,y,t[1]]
                horses[x][y].append(t)

        # 말이 4개 이상이면 끝
        for i in range(n):
            for j in range(n):
                if len(horses[i][j]) > 3: return 1
    return 0

n,k = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
horses = [[[] for _ in range(n)] for _ in range(n)] # (x,y)에 있는 말들의 [번호, 방향]
horseLoc = [[-1,-1,-1] for _ in range(k)]    # n-1번 말들의 [x,y,d]
for i in range(k):
    a,b,c = map(int,input().split())
    horses[a-1][b-1].append([i,c-1])
    horseLoc[i] = [a-1,b-1,c-1]

result = 0
while result<1001:
    result += 1
    # 말 이동
    if moveHorses(): break
if result==1001: print(-1)
else: print(result)