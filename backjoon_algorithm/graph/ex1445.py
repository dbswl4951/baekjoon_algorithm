#일요일 아침의 데이트
'''
BFS문제인줄 알았는데 다익스트라 + 우선순위 큐 문제였다

[ 문제 풀이 ]
쓰레기가 있는 칸 (g) = 2500,
g와 인접한 칸 = 1,
나머지 칸 = 0
으로 둔 뒤, 다익스트라 실행

2500으로 나눈 몫 = 쓰레기를 지난 횟수,
2500으로 나눠 생긴 나머지 = 쓰레기 옆을 지난 횟수
'''
import sys,heapq

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dijkstra():
    while q:
        # 가중치가 작은 곳부터 간다
        weight,x,y = heapq.heappop(q)
        if board[x][y] == 'F':
            print(distance[x][y]//2500, distance[x][y]%2500)
            break

        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                nw = weight+weightMap[nx][ny]
                if distance[nx][ny] > nw:
                    distance[nx][ny] = nw
                    heapq.heappush(q,[nw,nx,ny])

n,m = map(int,sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(n)]
weightMap = [[0]*m for _ in range(n)]    # 가중치 저장 (2500,1,0)
distance = [[int(1e9)]*m for _ in range(n)] # (x,y)까지의 총 가중치
q = []

for i in range(n):
    for j in range(m):
        if board[i][j] == 'S':
            heapq.heappush(q,[0,i,j])
            distance[i][j] = 0
        elif board[i][j] == 'g':
            weightMap[i][j] = 2500
            # 쓰레기와 인접한 곳은 가중치 1
            for k in range(4):
                ni,nj = i+dx[k],j+dy[k]
                if 0<=ni<n and 0<=nj<m and board[ni][nj]=='.':
                    weightMap[ni][nj] = 1
dijkstra()