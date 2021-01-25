#캐슬 디펜스
'''
고려 해야 할 점 (1차 시도때 고려 하지 못했던 점)
=> 여러 적을 죽일 수 있을 때, 거리&위치로 정렬해서, 가장 가까운 왼쪽 위치 적부터 죽여야 함
'''
#2차 시도
import sys,copy
from itertools import combinations

#궁수 한명씩에 대해 죽일 수 있는 모든 적 탐사 후, 가장 가까운 적을 죽임
def canShoot(boardTemp,row,col,d):
    global died
    ableList=[] #죽일 수 있는 적들
    for i in range(row-1,0,-1):
        for j in range(m):
            if boardTemp[i][j]==1:
                dist=abs(row - i)+abs(col - j)
                if dist<=d: #죽일 수 있는 거리에 있다면
                    #죽일 수 있는 적들 list에 추가 (여러 마리를 죽일 수 있으므로, 거리/방향에 대해 정렬 필요하기 때문)
                    ableList.append((dist,j,i))
    if ableList:    #죽일 수 있는 적들이 있다면
        ableList.sort() #가장 까가운 순으로 정렬
        died.append((ableList[0][2],ableList[0][1]))    #가장 가까운 위치, 왼쪽 적 죽임
        return True
    return False    #죽일 수 있는 적 없음

n,m,d=map(int,sys.stdin.readline().split()) #행, 열, 공격 거리
board=[[0]*(m+1) for _ in range(n+1)]
for i in range(1,n+1):
    board[i]=list(map(int,sys.stdin.readline().split()))
died=[]
temp=[i for i in range(m)]
hunters=list(combinations(temp,3))  #0열~m-1열까지 중 3명의 궁수를 배치하는 모든 경우
result=0
for hunter in hunters:  #3명의 궁수를 배치 한 모든 경우에 대해서
    boardTemp = copy.deepcopy(board)
    count=0
    for i in range(n+1,1,-1): #궁수 행
        shootCnt = 0
        for j in hunter:    #궁수 열
            if shootCnt<3:  #3발보다 적게 쐈다면
                if canShoot(boardTemp,i,j,d):   #화살을 쏠 수 있는 위치인지 판별
                    shootCnt+=1
        for enemy in died:  #죽인 적에 대해서
            if boardTemp[enemy[0]][enemy[1]]==1:    #쏘지 않았던 적이라면
                count+=1
                boardTemp[enemy[0]][enemy[1]]=0 #죽인 적은 0으로 변경
        died.clear()
    result=max(result,count)
print(result)


#1차 시도 : 메모리 초과 판정
'''
import sys,copy
from collections import deque
from itertools import combinations

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(i,j):
    global idx
    q=deque()
    q.append([i,j])
    while q:
        x,y=q.popleft()
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            if 0<=nx<idx and 0<=ny<m and (abs(i-nx)+abs(j-ny))<=d:
                if boardTemp[nx][ny]==1:
                    return True
                q.append([nx,ny])
    return False

n,m,d=map(int,sys.stdin.readline().split()) #행, 열, 공격 거리
board=[]
for _ in range(n):
    board.append(list(map(int,sys.stdin.readline().split())))
temp=[i for i in range(m)]
hunters=list(combinations(temp,3))  #0열~m-1열까지 중 3명의 궁수를 배치하는 모든 경우
result=0
for hunter in hunters:  #3명의 궁수를 배치 한 모든 경우에 대해서 bfs 실행
    boardTemp = copy.deepcopy(board)
    count=0
    idx=n
    h1,h2,h3=hunter
    boardTemp.append([0 for _ in range(m)])
    while len(boardTemp)>1:
        if idx<1:
            break
        boardTemp[idx][h1],boardTemp[idx][h2],boardTemp[idx][h3]=1,1,1  #궁수 위치:1
        success1,success2,success3=bfs(idx,h1),bfs(idx,h2),bfs(idx,h3)
        if success1==True: count+=1 #몬스터 처치 한 횟수 +1
        if success2 == True: count += 1
        if success3 == True: count += 1
        boardTemp=boardTemp[:idx-1][:]+[boardTemp[idx][:]]
        idx-=1
    result=max(result,count)
print(result)
'''