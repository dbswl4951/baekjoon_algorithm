#구슬 탈출2
'''
BFS (너비 우선 탐색)알고리즘 이용
'''

dm=[(-1,0),(1,0),(0,-1),(0,1)]  #위,아래,왼,오른쪽으로 이동 방향

def move(x,y,dx,dy):     #구슬 이동
    cnt=0
    while boardMap[x+dx][y+dy]!='#' and boardMap[x][y]!='O':
        cnt+=1
        x+=dx
        y+=dy
    return x,y,cnt

def play(rx,ry,bx,by,count):
    queue=[(rx,ry,bx,by,count)] #큐에 넣음
    visited.append((rx,ry,bx,by))   #처음 시작 위치를 방문 list에 넣음

    while queue:
        srx,sry,sbx,sby,count=queue.pop(0)
        if count>10:    #10번 이내에 성공 하지 못한 경우
            return -1

        for dx,dy in dm:    #dm에 있는 방향들 하나씩 실행 -> 갈 수 있는 방향으로 이동
            # 빨간 구슬이 벽에 부딪히거나 구멍에 도달 할 때의 x,y좌표와 움직인 횟수
            nrx,nry,nRcount = move(srx,sry,dx,dy)
            # 파란 구슬이 벽에 부딪히거나 구멍에 도달 할 때의 x,y좌표와 움직인 횟수
            nbx,nby,nBcount = move(sbx,sby,dx,dy)
            if boardMap[nbx][nby]!='O':    #파란구슬이 출구에 도달하지 않고
                if boardMap[nrx][nry]=='O': #빨간 구슬만 출구에 도달
                    return count
                if nrx==nbx and nry==nby:   #빨간구슬과 파란구슬의 위치가 같다면
                    if nRcount>nBcount: #빨간 구슬이 더 많이 움직이면 빨간구슬을 뒤로 이동
                        nrx-=dx
                        nry-=dy
                    else:   #파란 구슬이 더 많이 움직였으면 파란 구슬을 뒤로
                        nbx-=dx
                        nby-=dy
                if (nrx,nry,nbx,nby) not in visited:
                    visited.append((nrx,nry,nbx,nby))
                    queue.append((nrx,nry,nbx,nby,count+1))
    return -1   #빨간 구슬이 구멍에 도달하지 못 했을 때

n,m = map(int,input().split())  #n:세로, m:가로
visited=[]  #방문한 위치 저장
boardMap=[]     #전체 맵을 담는 list
for i in range(n):
    boardMap.append(list(input()))

for i in range(n):  #파란구슬, 빨간구슬 위치 얻기
    for j in range(m):
        if boardMap[i][j]=='R':     #빨간 구슬의 위치 얻기
            rx,ry=i,j
            continue
        if boardMap[i][j]=='B':     #파란구슬의 위치 얻기
            bx,by=i,j
result=play(rx,ry,bx,by,1)  #count=1부터 시작
print(result)