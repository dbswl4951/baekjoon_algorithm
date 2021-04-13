#미네랄
# 2차 시도 => 다른 사람 풀이 참고
'''
1. 클러스터 파괴
2. 파괴 한 클러스터 주변(상하좌우) bfs로 탐색 (떨어트려야 할 미네랄이 있는지)
    아래가 .라면 떨어질 수 있는 미네랄이므로, fall 리스트에 삽입
    visited 리스트로 현재 탐색 중인 클러스터 체크
3. fall 리스트 돌면서 떨어질 높이(h) 구하기
'''
import sys
from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

# 클러스터 파괴
def destroy(idx,left):
    x,y=r-idx,0
    if left==1:
        for j in range(c):
            if cave[x][j]=='x':
                cave[x][j]='.'
                y=j
                break
    else:
        for j in range(c-1,-1,-1):
            if cave[x][j]=='x':
                cave[x][j]='.'
                y=j
                break
    # 파괴 된 미네랄 주변(상하좌우) 탐색
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<r and 0<=ny<c and cave[nx][ny]=='x':
            explore.append([nx,ny])

# (x,y)좌표부터 미네랄 탐색 시작 => 떨어질 수 있는 미네랄 체크
def bfs(x,y):
    q=deque()
    q.append([x,y])
    visited=[[0]*c for _ in range(r)]   # 현재 클러스터 체크하기 위해
    visited[x][y]=1
    ableFall=[]     # 떨어질 가능성 있는 미네랄 저장
    while q:
        x,y=q.popleft()
        # 바닥에 닿아있다면 떨어트릴게 없음
        if x==r-1:
            return
        # 아래가 빈 칸이라면 떨어질 수 있으므로 ableFall 리스트에 저장
        if cave[x+1][y]=='.':
            ableFall.append([x,y])
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<r and 0<=ny<c and cave[nx][ny]=='x' and visited[nx][ny]==0:
                visited[nx][ny]=1
                q.append([nx,ny])
    fall(visited,ableFall)

# 얼마나 떨어트려야 하는지(h) 구한 뒤, 미네랄 떨어트리기
def fall(visited,ableFall):
    h,flag=1,0
    while True:
        for x,y in ableFall:
            # h칸 아래가 바닥인 경우
            if x+h==r-1:
                flag=1
                break
            # h칸 아래에 다른 클러스터가 있는 경우
            if cave[x+h+1][y]=='x' and visited[x+h+1][y]==0:
                flag=1
                break
        if flag: break
        h+=1
    for i in range(r-2,-1,-1):
        for j in range(c):
            # 현재 탐색 중인 클러스터의 미네랄이면 떨어트린다
            if cave[i][j]=='x' and visited[i][j]==1:
                cave[i][j]='.'
                cave[i+h][j]='x'

r,c=map(int,sys.stdin.readline().split())
cave=[list(sys.stdin.readline().strip()) for _ in range(r)]
n=int(sys.stdin.readline().strip())
throw=deque(map(int,sys.stdin.readline().split()))
explore=deque()     # 탐색 해야 할 미네랄 시작 위치 저장

left=1
while n:
    idx=throw.popleft() 
    destroy(idx,left)
    # 이부분에서 'for x,y in explore:'를 사용하면 시간 초과 남.. 아마 in 때문인듯하다
    while explore:
        x,y=explore.popleft()
        bfs(x,y)
    left*=-1
    n-=1
for ca in cave:
    print(''.join(ca))


# 1차 시도 => 실패
# 예제 테케랑 게시판 반례는 다 맞는데 왜 틀린지 모르겠다!!!
'''
import sys
from collections import deque
from collections import defaultdict

dx=[-1,1,0,0]
dy=[0,0,-1,1]

# 클러스터 덩어리 탐색 + 떠있는 클러스터 떨어트리기
def bfs(x,y,visited):
    q=deque()
    q.append([x,y])
    visited[x][y]=1
    dic = defaultdict(list)
    dic[y]=[x]
    # 클러스터 덩어리 탐색
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<r and 0<=ny<c and visited[nx][ny]==0 and cave[nx][ny]=='x':
                visited[nx][ny]=1
                q.append([nx,ny])
                if ny in dic.keys():
                    if nx not in dic[ny]: dic[ny].append(nx)
                else: dic[ny]=[nx]

    drop=[]
    flag=0
    # 떠있는 클러스터 검사
    for key,value in dic.items():
        value.sort(reverse=True)
        bottom=value[0]
        # 바닥에 붙어있는 경우
        if bottom==r-1:
            flag=1
            break
        # 아래에 클러스터가 있는 경우
        if cave[bottom+1][key]=='x':
            continue
        drop.append([key,value])

    # 공중에 떠있는 클러스터면 떨어트리기
    if not flag:
        high=101
        for col,row in drop:
            for ro in row:
                h = 0
                ny=ro+1
                # 떨어트릴 높이(h) 구하기
                while ny<r:
                    if cave[ny][col]=='x':
                        break
                    ny += 1
                    h+=1
                if h:
                    high=min(high,h)
        # high만큼 떨어트리기
        for col,row in drop:
            for ro in row:
                cave[ro+high][col]='x'
                cave[ro][col]='.'
                visited[ro+high][col]=1
                visited[ro][col]=0

def gameStart():
    for i in range(n):
        # 1) 막대 던져서 미네랄 파괴
        if i%2==0:
            for j in range(c):
                if cave[r-throw[i]][j]=='x':
                    cave[r - throw[i]][j]='.'
                    break
        else:
            for j in range(c-1,-1,-1):
                if cave[r-throw[i]][j]=='x':
                    cave[r - throw[i]][j]='.'
                    break

        visited = [[0] * c for _ in range(r)]
        # 2) 미네랄이 떠있는지 확인
        for j in range(r-1,-1,-1):
            for k in range(c):
                if not visited[j][k] and cave[j][k]=='x':
                    bfs(j,k,visited)

r,c=map(int,sys.stdin.readline().split())
cave=[list(sys.stdin.readline().strip()) for _ in range(r)]
n=int(sys.stdin.readline().strip())
throw=list(map(int,sys.stdin.readline().split()))
gameStart()
for ca in cave:
    print(''.join(ca))
'''