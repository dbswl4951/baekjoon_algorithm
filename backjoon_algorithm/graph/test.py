from collections import deque
import sys, copy
input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    q.append([x, y])
    c[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if na[nx][ny] != 0 and c[nx][ny] == 0:
                    c[nx][ny] = 1
                    q.append([nx, ny])

def ice():
    a2 = copy.deepcopy(a)
    for i in range(n):
        for j in range(m):
            if a[i][j] != 0:
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < n and 0 <= ny < m:
                        if a[nx][ny] == 0:
                            a2[i][j] -= 1
                            if a2[i][j] == 0:
                                break
    return a2

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
q = deque()
year = 1

while True:
    na = ice()
    flag = 0
    for i in na:
        flag += i.count(0)
    if flag == n*m:
        print(0)
        sys.exit()
    a = copy.deepcopy(na)
    c = [[0]*m for _ in range(n)]
    cnt = 1
    for i in range(n):
        for j in range(m):
            if na[i][j] != 0 and c[i][j] == 0:
                if cnt == 2:
                    print(year)
                    sys.exit()
                bfs(i, j)
                cnt += 1
    year += 1