#원판 돌리기
import sys
from collections import deque

# num번째 원판 양 옆 확인
def checkSide(num,idx):
    temp = set()
    # 맨 첫 번째 수 확인
    if idx == 0 and table[num][0]!=0:
        if table[num][0] == table[num][1]:
            temp.add((num, 0))
            temp.add((num, 1))
        if table[num][0] == table[num][m-1]:
            temp.add((num, 0))
            temp.add((num, m-1))
    # 맨 마지막 수 확인
    elif idx == m - 1 and table[num][m-1]!=0:
        if table[num][m-1] == table[num][0]:
            temp.add((num, m-1))
            temp.add((num, 0))
        if table[num][m - 1] == table[num][m - 2]:
            temp.add((num, m - 1))
            temp.add((num, m - 2))
    # 나머지 수
    elif table[num][idx]!=0:
        if table[num][idx]==table[num][idx+1]:
            temp.add((num, idx))
            temp.add((num, idx+1))
        if table[num][idx]==table[num][idx-1]:
            temp.add((num, idx))
            temp.add((num, idx-1))
    return temp

# i+1, i-1 번째 원판 확인
def checkPreNext(num,idx):
    temp = set()
    # 맨 첫 원판
    if num==1 and table[1][idx]!=0:
        if table[1][idx]==table[2][idx]:
            temp.add((1,idx))
            temp.add((2,idx))
    # 맨 마지막 원판
    elif num==n and table[n][idx]!=0:
        if table[n][idx]==table[n-1][idx]:
            temp.add((n,idx))
            temp.add((n-1,idx))
    # 2번째 ~ n-1번째 원판
    elif table[num][idx]!=0:
        if table[num][idx]==table[num+1][idx]:
            temp.add((num, idx))
            temp.add((num+1, idx))
        if table[num][idx]==table[num-1][idx]:
            temp.add((num, idx))
            temp.add((num-1, idx))
    return temp

def start(x,d,k):
    # 시계 방향으로 k만큼 회전
    if d==0:
        for i in range(x,n+1,x):
            table[i].rotate(k)
    # 반시계 방향으로 k만큼 회전
    else:
        for i in range(x,n+1,x):
            table[i].rotate(-k)

    delete=set()
    # 모든 원판의 인접한 수 확인 => delete에 넣기
    for i in range(1,n+1):
        for j in range(m):
            # 인접한 양 옆 수 확인
            delete=delete|checkSide(i,j)
            # 인접한 원판 수 확인
            delete=delete|checkPreNext(i,j)

    # 인접한 수가 있으면 삭제 (0으로 변환)
    if delete:
        for num,idx in delete:
            if table[num][idx]!=0:
                table[num][idx]=0
    # 인접한 수 없으면, 평균보다 큰 수-=1, 평균보다 작은수+=1
    else:
        val=0
        a=0
        for i in range(1,n+1):
            for j in range(m):
                if table[i][j]!=0:
                    a+=1
                    val+=table[i][j]
        if a!=0: val/=a
        for i in range(1,n+1):
            for j in range(m):
                if table[i][j]!=0:
                    if table[i][j]>val:
                        table[i][j]-=1
                    elif table[i][j]<val:
                        table[i][j]+=1

n,m,t=map(int,sys.stdin.readline().split())
table=[[0]*n]+[deque(map(int,sys.stdin.readline().split())) for _ in range(n)]
for _ in range(t):
    x,d,k = map(int, sys.stdin.readline().split())
    start(x,d,k)
result=0
for i in range(1,n+1):
    result+=sum(table[i])
print(result)