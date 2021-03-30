#배열 돌리기 4
'''
순열 대신 백트레킹 + dfs + bfs 사용
'''
from collections import deque
from copy import deepcopy
import sys

dx=[0,1,0,-1]
dy=[1,0,-1,0]

# 연산 수행 순서 정하기
def dfs(cnt):
    global result
    if cnt==k:
        q2=deepcopy(q)
        result=min(result,rotate(q2))
        return
    for i in range(k):
        if select[i]: continue
        select[i]=1
        q.append(oper[i])
        dfs(cnt+1)
        select[i]=0
        q.pop()

# 배열 회전
def rotate(q):
    arr2=deepcopy(arr)
    # 하나씩 연산 수행
    while q:
        x,y,z=q.popleft()
        lx,ly,rx,ry=x-z,y-z, x+z, y+z
        # 회전하는 하나의 정사각형
        while True:
            if lx>=rx or ly>=ry: break
            dir=0
            # 정사각형 시작 지점 (맨위 맨오른쪽)
            x,y,before=lx,ly,arr2[lx][ly]
            # 한 방향
            while True:
                nx,ny=x+dx[dir],y+dy[dir]
                # 한 방향으로 계속 가다가 정사각형 경계 밖으로 나가면 방향 변경
                if not lx<=nx<=rx or not ly<=ny<=ry:
                    dir+=1
                    continue
                temp=arr2[nx][ny]
                arr2[nx][ny]=before
                before=temp
                x,y=nx,ny
                # 우하좌상 방향 다 돌아서 다시 시작지점으로 온다면, 안에 있는 더 작은 사각형으로 이동
                if [x,y]==[lx,ly]:
                    lx+=1
                    ly+=1
                    rx-=1
                    ry-=1
                    break
    val=int(1e9)
    for row in arr2:
        val=min(val,sum(row))
    return val

n,m,k=map(int,sys.stdin.readline().split())
arr=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
oper=[]
for _ in range(k):
    r,c,s=map(int,sys.stdin.readline().split())
    r,c=r-1,c-1
    oper.append((r,c,s))
select=[0 for _ in range(k)]
result=int(1e9)
q=deque()
dfs(0)
print(result)