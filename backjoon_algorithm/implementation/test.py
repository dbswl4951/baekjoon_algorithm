from collections import deque
sx, sy = map(int, input().split())
ex, ey = map(int, input().split())
dist = [[-1]*9 for _ in range(10)]
dx = [(-1, -2, -3), (-1, -2, -3), (0, -1, -2), (0, -1, -2),
      (0, 1, 2), (0, 1, 2), (1, 2, 3), (1, 2, 3)]
dy = [(0, -1, -2), (0, 1, 2), (-1, -2, -3), (1, 2, 3),
      (-1, -2, -3), (1, 2, 3), (0, -1, -2), (0, 1, 2)]

def move(i, x, y):
    nx, ny = x, y
    for j in range(3):
        nx, ny = x+dx[i][j], y+dy[i][j]
        if nx < 0 or nx >= 10 or ny < 0 or ny >= 9:
            return -1, -1
        if j < 2 and nx == ex and ny == ey:
            return -1, -1
    return nx, ny

def bfs():
    q = deque()
    q.append((sx, sy))
    dist[sx][sy] = 0
    while q:
        x, y = q.popleft()
        print("x,y ===",x,y)
        if x == ex and y == ey:
            print('--------')
            print(dist[x][y])
            return
        for i in range(8):
            nx, ny = move(i, x, y)
            if nx != -1 and dist[nx][ny] == -1:
                print('nx,ny : ',nx,ny)
                q.append((nx, ny))
                dist[nx][ny] = dist[x][y]+1
                print("q:",q)
                for d in dist: print(d)
    print(-1)

bfs()