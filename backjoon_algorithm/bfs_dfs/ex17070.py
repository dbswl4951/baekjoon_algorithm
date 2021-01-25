#파이프 옮기기1
'''
파이프 밀기
1) 가로로 밀 때 : (x,y+1)이 0 (빈 칸)이여야 함
2) 대각선으로 밀 때 : (x+1,y),(x,y+1),(x+1,y+1)이 0 (빈 칸)이여야 함
3) 세로로 밀 때 : (x+1,y)가 0이여야 함
'''
import sys

def dfs(x,y,r,l):   #다음에 올 수 있는 파이프 r:가로, l:세로
    global result
    if x==n-1 and y==n-1:
        result+=1
        return
    # 가로로 이동
    if 0<=y<n-1 and house[x][y+1]==0 and r==1:  
        dfs(x,y+1,1,0)
    # 대각선으로 이동
    if 0<=x<n-1 and 0<=y<n-1 and house[x+1][y]==0 and house[x][y+1]==0 and house[x+1][y+1]==0: 
        dfs(x+1,y+1,1,1)
    # 세로로 이동
    if 0<=x<n-1 and house[x+1][y]==0 and l==1:    
        dfs(x+1,y,0,1)

n=int(sys.stdin.readline().strip())
house=[]
for _ in range(n):
    house.append(list(map(int,sys.stdin.readline().split())))
result=0
dfs(0,1,1,0)
print(result)