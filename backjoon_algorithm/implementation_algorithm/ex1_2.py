#상하좌우2

n = int(input())
path = input().split()
x,y=1,1

#L,R,U,D
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move=['L','R','U','D']

for p in path:
    for i in range(len(move)):
        if p==move[i]:
            nx=x+dx[i]
            ny=y+dy[i]
    if nx<1 or nx>n or ny<1 or ny>n:    #만약 정사각형의 공간을 벗어나는 움직임이라면
        continue    #저장하지 않고 무시한채 다음 움직임 실행
    x,y=nx,ny
print(x,y)