#드래곤 커브
'''
동:0, 서:2, 남:3, 북:1
0세대: 0
1세대: 0, 1
2세대: 0, 1, 2, 1
3세대: 0, 1, 2, 1, 2, 3, 2, 1
4세대: 0, 1, 2, 1, 2, 3, 2, 1, 2, 3, 0, 3, 2, 3, 2, 1
=> 전 세대들에 1을 더하고 뒤집어준 형식

규칙을 찾지 못해서 풀이 참고
'''
import sys

dx=[1,0,-1,0]
dy=[0,-1,0,1]

n=int(sys.stdin.readline().strip())
curve=[]
visited=[[0]*101 for _ in range(101)]
for _ in range(n):
    x,y,d,g=map(int,sys.stdin.readline().split())
    visited[x][y]=1
    dir=[d]
    q=[d]
    for _ in range(g+1):
        for i in q:
            x,y=x+dx[i],y+dy[i]
            visited[x][y]=1
        q=[(d+1)%4 for d in dir]
        q.reverse()
        dir+=q
result=0
for i in range(100):
    for j in range(100):
        if visited[i][j] and visited[i][j+1] and visited[i+1][j] and visited[i+1][j+1]:
            result+=1
print(result)