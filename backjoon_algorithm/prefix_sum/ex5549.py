#행성 탐사
'''
누적합으로 풀이
'''
import sys

m,n=map(int,sys.stdin.readline().split())
k=int(sys.stdin.readline().strip())
board=[list(sys.stdin.readline().strip()) for _ in range(m)]
info=[]
for _ in range(k):
    a,b,c,d=map(int,sys.stdin.readline().split())
    info.append([a-1,b-1,c-1,d-1])
dic={'J':0,'O':1,'I':2}
pBoard=[[[0,0,0] for _ in range(n)] for _ in range(m)]
pBoard[0][0][dic[board[0][0]]]+=1

# 0행 채우기
for i in range(1,n):
    area=dic[board[0][i]]
    pBoard[0][i]=[pBoard[0][i-1][0],pBoard[0][i-1][1],pBoard[0][i-1][2]]
    pBoard[0][i][area]+=1
# 0열 채우기
for i in range(1,m):
    area = dic[board[i][0]]
    pBoard[i][0] = [pBoard[i-1][0][0], pBoard[i-1][0][1], pBoard[i-1][0][2]]
    pBoard[i][0][area] += 1
# 나머지 칸 채우기
for i in range(1,m):
    for j in range(1,n):
        area = dic[board[i][j]]
        pBoard[i][j]=[pBoard[i-1][j][0]+pBoard[i][j-1][0]-pBoard[i-1][j-1][0],
                      pBoard[i-1][j][1]+pBoard[i][j-1][1]-pBoard[i-1][j-1][1],
                      pBoard[i-1][j][2]+pBoard[i][j-1][2]-pBoard[i-1][j-1][2]]
        pBoard[i][j][area]+=1

result=[]
for sx,sy,ex,ey in info:
    if sx==0 and sy==0:
        result.append(pBoard[ex][ey])
        continue
    elif sx==0:
        temp=[pBoard[ex][ey][0]-pBoard[ex][sy-1][0],
              pBoard[ex][ey][1]-pBoard[ex][sy-1][1],
              pBoard[ex][ey][2]-pBoard[ex][sy-1][2]]
    elif sy==0:
        temp=[pBoard[ex][ey][0]-pBoard[sx-1][ey][0],
              pBoard[ex][ey][1]-pBoard[sx-1][ey][1],
              pBoard[ex][ey][2]-pBoard[sx-1][ey][2]]
    else:
        temp=[pBoard[ex][ey][0]-pBoard[ex][sy-1][0]-pBoard[sx-1][ey][0]+pBoard[sx-1][sy-1][0],
            pBoard[ex][ey][1]-pBoard[ex][sy-1][1]-pBoard[sx-1][ey][1]+pBoard[sx-1][sy-1][1],
            pBoard[ex][ey][2]-pBoard[ex][sy-1][2]-pBoard[sx-1][ey][2]+pBoard[sx-1][sy-1][2]]
    result.append(temp)
for r in result:
    print(*r)