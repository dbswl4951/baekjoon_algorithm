#나무 재태크
from collections import deque

dx = [-1,-1,-1,0,1,1,1,0]
dy = [-1,0,1,1,1,0,-1,-1]

def springAndSummer():
    die = []

    # 봄
    for i in range(n):
        for j in range(n):
            alive = deque()
            for idx,age in enumerate(treeAge[i][j]):
                if energe[i][j] >= age:
                    alive.append(age+1)
                    energe[i][j] -= age
                else:
                    cnt = len(treeAge[i][j]) - idx
                    while cnt:
                        die.append([i,j,treeAge[i][j].pop()])
                        cnt -= 1
                    break
            treeAge[i][j] = alive

    # 여름
    for x,y,age in die:
        age = int(age//2)
        energe[x][y] += age

# 가을, 겨울
def fallAndWinter():
    # 가을
    for i in range(n):
        for j in range(n):
            for age in treeAge[i][j]:
                if age%5 == 0:
                    # 8방향으로 나이 1인 나무 생김
                    for k in range(8):
                        ni,nj = i+dx[k],j+dy[k]
                        if 0<=ni<n and 0<=nj<n:
                            treeAge[ni][nj].appendleft(1)

    # 겨울
    for i in range(n):
        for j in range(n):
            energe[i][j] += board[i][j]

n,m,k = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
treeAge = [[deque() for _ in range(n)] for _ in range(n)]    # 나무의 나이 저장
energe = [[5]*n for _ in range(n)]  # 양분 저장
result = 0
for _ in range(m):
    a,b,c = map(int,input().split())
    treeAge[a-1][b-1].append(c)

for _ in range(k):
    # 봄, 여름
    springAndSummer()
    # 가을, 겨울
    fallAndWinter()
for i in range(n):
    for j in range(n):
        result += len(treeAge[i][j])
print(result)