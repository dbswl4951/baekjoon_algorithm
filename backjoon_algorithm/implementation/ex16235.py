#나무 재테크
import sys

dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, 1, -1, 1, 1, -1, -1]

n,m,k=map(int,sys.stdin.readline().split())
a=[]
for _ in range(n):
    a.append(list(map(int,sys.stdin.readline().split())))
tree=[[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x,y,age=map(int,sys.stdin.readline().split())
    tree[x-1][y-1].append(age)
board=[[5]*n for _ in range(n)]

for year in range(k):
    #봄:양분 먹고 나이 증가, 여름:죽은 나무 양분으로 변하기
    for i in range(n):
        for j in range(n):
            if tree[i][j]:
                #나이 적은 애부터 양분 먹기위해 정렬
                tree[i][j].sort()
                tempTree,deadTree=[],0
                for age in tree[i][j]:
                    #양분 먹을 수 있으면 나이 증가
                    if board[i][j]>=age:
                        board[i][j]-=age
                        age+=1
                        tempTree.append(age)
                    #양분 부족하면 나무 죽음
                    else:
                        deadTree+=age//2
                board[i][j]+=deadTree
                tree[i][j]=[]
                #새로운 나이 나무로 갱신
                tree[i][j].extend(tempTree)
    if not tree:
        print(0)
        sys.exit()

    #가을 : 나무 번식
    for i in range(n):
        for j in range(n):
            if tree[i][j]:
                for age in tree[i][j]:
                    if age%5==0:
                        for d in range(8):
                            ni,nj=i+dx[d],j+dy[d]
                            if 0<=ni<n and 0<=nj<n:
                                tree[ni][nj].append(1)
    #겨울 : 양분 추가
    for i in range(n):
        for j in range(n):
            board[i][j]+=a[i][j]

result=0
for i in range(n):
    for j in range(n):
        result+=len(tree[i][j])
print(result)