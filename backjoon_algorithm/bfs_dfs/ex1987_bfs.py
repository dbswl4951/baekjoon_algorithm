#알파벳
'''
dfs 알고리즘 사용해서 풀이 시작 => 실패 왜 못 풀었지..?
다른 사람들의 풀이를 보니 dfs로도 풀 수 있지만, 거의 다 BFS으로 품(시간이 덜 걸림).
길이와 관련해서 구하는 경우는 BFS가 대부분 유리 한 것 같음
'''

r,c=map(int,input().split())
alpha=[list(input()) for _ in range(r)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
count=1

def bfs(x,y):
    global count
    q= set([(x, y,alpha[x][y])])
    while q:
        x,y,passed=q.pop()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0 <= nx < r and 0 <= ny < c and alpha[nx][ny] not in passed:
                # 지나간 알파벳인지를 확인하기 위해 지나갈 때마다 이전 거에 지나간 알파벳을 더해줌
                q.add((nx,ny,passed+alpha[nx][ny]))
                print(passed)
                count=max(count,len(passed)+1)

bfs(0,0)
print(count)