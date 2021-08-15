#원판 돌리기
import sys
from collections import deque

# 원판 회전
def rotateTable(d,k,xTable):
    if d==0:
        for xt in xTable:
            table[xt].rotate(k)
    else:
        for xt in xTable:
            table[xt].rotate(-k)
    return table

# 원판과 인접한 수 중 같은 수 찾기
def findSameNumbers():
    removeNums = set()

    for i in range(n):
        # 첫 번째 원판인 경우 => 양 옆, 다음 원판 확인
        if i==0:
            for j in range(m):
                if table[0][j]:
                    if j==m-1:
                        if table[0][j]==table[0][0]:
                            removeNums.add((0, j))
                            removeNums.add((0, 0))
                    else:
                        if table[0][j]==table[0][j+1]:
                            removeNums.add((0,j))
                            removeNums.add((0, j+1))
                    if table[0][j]==table[0][j-1]:
                        removeNums.add((0,j))
                        removeNums.add((0, j-1))
                    # 다음 원판과 비교
                    if table[0][j]==table[1][j]:
                        removeNums.add((0,j))
                        removeNums.add((1, j))
        # 마지막 원판인 경우 => 양 옆, 그 전 원판 확인
        elif i==n-1:
            for j in range(m):
                if table[i][j]:
                    if j==m-1:
                        if table[i][j] == table[i][0]:
                            removeNums.add((i, j))
                            removeNums.add((i, 0))
                    else:
                        if table[i][j] == table[i][j + 1]:
                            removeNums.add((i, j))
                            removeNums.add((i, j + 1))
                    if table[i][j] == table[i][j - 1]:
                        removeNums.add((i, j))
                        removeNums.add((i, j - 1))
                    # 그 전 원판과 비교
                    if table[i][j] == table[i-1][j]:
                        removeNums.add((i, j))
                        removeNums.add((i-1, j))
        # 중간에 있는 원판 => 양 옆, 그 전 원판, 그 후 원판 확인
        else:
            for j in range(m):
                if table[i][j]:
                    if j == m - 1:
                        if table[i][j] == table[i][0]:
                            removeNums.add((i, j))
                            removeNums.add((i, 0))
                    else:
                        if table[i][j] == table[i][j+1]:
                            removeNums.add((i, j))
                            removeNums.add((i, j+1))
                    if table[i][j] == table[i][j - 1]:
                        removeNums.add((i, j))
                        removeNums.add((i, j - 1))
                    # 다음 원판과 비교
                    if table[i][j] == table[i+1][j]:
                        removeNums.add((i, j))
                        removeNums.add((i+1, j))
                    # 그 전 원판과 비교
                    if table[i][j] == table[i - 1][j]:
                        removeNums.add((i, j))
                        removeNums.add((i - 1, j))
    return removeNums

n,m,t=map(int,sys.stdin.readline().split())
table=deque()
for _ in range(n):
    arr=deque(map(int,sys.stdin.readline().split()))
    table.append(arr)
rotateInfo=[list(map(int,sys.stdin.readline().split())) for _ in range(t)]

# t번 반복
for x,d,k in rotateInfo:
    # x배수의 원판 찾기
    xTable=[i for i in range(x-1,n,x)]

    # 원판 회전
    table=rotateTable(d,k,xTable)

    # 회전한 원판과 인접한 수 중 같은 수 찾기
    removeNums=findSameNumbers()

    # 삭제 할 수가 있다면 삭제
    if removeNums:
        for i,j in removeNums:
            table[i][j]=0
    # 삭제 할 수가 없다면 평균 구한 뒤, -1,+1
    else:
        count,tSum=0,0
        for tab in table:
            for t in tab:
                if t!=0:
                    count+=1
                    tSum+=t
        if count:
            average = tSum/count
            for i in range(n):
                for j in range(m):
                    if table[i][j]:
                        if average<table[i][j]: table[i][j]-=1
                        elif average>table[i][j]: table[i][j]+=1
result=0
# 남아있는 수의 합 구하기
for t in table: result+=sum(t)
print(result)