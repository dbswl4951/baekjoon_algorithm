#감시
import sys,copy

dx=[0,0,-1,1]
dy=[-1,1,0,0]
#1,2,..번 카메라에서 탐색 할 수 있는 방향을 dx,dy의 index로 가짐
direction = [0,[[0],[1],[2],[3]],[[0,1],[2,3]],[[1,2],[1,3],[0,2],[0,3]],
             [[0,1,2],[0,1,3],[0,2,3],[1,2,3]],[[0,1,2,3]]]

def dfs(count,room,cctv):
    global result
    cnt=0
    if count==len(cctv):
        for i in range(n):
            for j in range(m):
                if room[i][j]==0:
                    cnt+=1
        result=min(result,cnt)
        return

    num,x,y=cctv[count]
    # 회전 해서 볼 수 있는 모든 cctv 방향들
    for dir in direction[num]:
        temp=copy.deepcopy(room)
        # 한번에 볼 수 있는 cctv 방향들
        for i in dir:
            nx,ny=x+dx[i],y+dy[i]
            while True:
                if 0<=nx<n and 0<=ny<m and temp[nx][ny]!=6:
                    if temp[nx][ny]==0:
                        temp[nx][ny]='#'
                    nx,ny=nx+dx[i],ny+dy[i]
                else: break
        # 다음 cctv로 이동
        dfs(count+1,temp,cctv)

n,m=map(int,sys.stdin.readline().split())
room=[]
cctv=[]
for i in range(n):
    row=list(map(int,sys.stdin.readline().split()))
    room.append(row)
    for j in range(m):
        if 1<=room[i][j]<=5:
            cctv.append([room[i][j],i,j])
result=int(1e9)
dfs(0,room,cctv)
print(result)