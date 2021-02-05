#미친 로봇
'''
단순하게 이동 하는 경로만을 dfs로 구하여 그 확률을 더해준다.
방문 한 경로는 visited 배열에 넣어 방문 경로를 저장하고, n번만큼 방문이 완료되면 확률값을 더하고 return한다.
모든 경우의 수를 확인 할 때까지 visited 배열에 경로 저장, 경로 삭제를 반복적으로 수행한다.

<주의 할 점>
1. 단순 이동 (문제에서 요구하는) 경로의 확률만을 구한다.
2. 방문 한 경로를 visited에 저장 후, dfs를 돈 후 다시 뒤에서 부터 하나씩 방문 경로를 삭제해야 한다 (visited.pop())

확률이 나오는 경로문제라 어떻게 풀어야 할지 감이 안잡혔다..
'''
import sys
sys.setrecursionlimit(100000)

dx=[-1,1,0,0]
dy=[0,0,-1,1]

#로봇의 이동 경로가 단순 한 경우의 확률을 모두 더함
def dfs(x,y,cnt,p,visited):
    global result
    #로봇이 n번 움직였을 경우 확률 더한 후 return
    if cnt==n:
        result+=p
        return
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        #로봇은 방문하지 않았던 경로로만 이동
        if (nx,ny) not in visited:
            visited.append((nx,ny))
            dfs(nx,ny,cnt+1,p*pro[i],visited)
            #확률 계산 후, 맨 마지막 위치를 방문하기 전으로 이동
            visited.pop()

n,ep,wp,np,sp=map(int,sys.stdin.readline().split())
pro=[ep/100,wp/100,np/100,sp/100]
result=0
visited=[(0,0)] #로봇이 방문 한 경로 저장
dfs(0,0,0,1,visited)    #(현재 x좌표, 현재 y좌표, 로봇 이동 횟수, 이동한 경로 확률, 방문 경로)
print(result)