#알파벳
'''
백트래킹 사용
'''

r,c=map(int,input().split())
alpha=[list(input()) for _ in range(r)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
count=1

def dfs(x,y,passed):
    global count
    check=0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and alpha[nx][ny] not in passed:
            print("passed111:",passed)
            dfs(nx,ny,passed+alpha[nx][ny])
        else:
            check+=1
    if check==4:    #네 방향 다 이동 할 수 없으면 길이 확인
        count=max(count,len(passed))
        return

dfs(0,0,alpha[0][0])
print(count)