#마법사 상어와 파이어볼
import math

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

def start():
    newBoard = [[[]*n for _ in range(n)] for _ in range(n)]

    # 모든 파이어 볼 이동
    for i in range(n):
        for j in range(n):
            if board[i][j]:
                idx = 0
                while idx<len(board[i][j]):
                    m,s,d = board[i][j][idx]
                    ni,nj = i+dx[d]*s,j+dy[d]*s
                    while ni<0: ni+=n
                    while ni>=n: ni-=n
                    while nj<0: nj+=n
                    while nj>=n: nj-=n
                    newBoard[ni][nj].append([m,s,d])
                    idx+=1

    # 2개 이상 파이어볼이 있는 칸
    for i in range(n):
        for j in range(n):
            if len(newBoard[i][j])>1:
                idx,nm,ns,nd,flag = 0,0,0,[],[]
                while idx < len(newBoard[i][j]):
                    nm += newBoard[i][j][idx][0]
                    ns += newBoard[i][j][idx][1]
                    flag.append(newBoard[i][j][idx][2]%2)
                    idx += 1

                nm = math.trunc(nm/5)
                ns = math.trunc(ns/len(newBoard[i][j]))
                if nm == 0:
                    newBoard[i][j] = []
                    continue

                # 방향이 모두 홀수이거나 짝수인 경우
                if len(set(flag)) == 1:
                    newBoard[i][j] = [[nm,ns,0],[nm,ns,2],[nm,ns,4],[nm,ns,6]]
                else:
                    newBoard[i][j] = [[nm, ns, 1], [nm, ns, 3], [nm, ns, 5], [nm, ns, 7]]
    return newBoard

n,m,k = map(int,input().split())
board = [[[]*n for _ in range(n)] for _ in range(n)]
for _ in range(m):
    a,b,c,d,e = map(int,input().split())
    board[a-1][b-1].append([c,d,e])
result = 0

for _ in range(k):
    # 파이어볼 이동
    board = start()
for i in range(n):
    for j in range(n):
        if board[i][j]:
            idx = 0
            while idx < len(board[i][j]):
                result += board[i][j][idx][0]
                idx+=1
print(result)
