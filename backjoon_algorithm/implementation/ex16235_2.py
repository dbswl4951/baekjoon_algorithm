#나무 재테크
import sys

direction=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

# 봄, 여름 (나무는 나이만큼 양분을 먹는다 or 죽음, 죽은 나무 => 양분)
def springTosummer():
    # 봄
    for i in range(1,n+1):
        for j in range(1,n+1):
            if forest[i][j]:
                forest[i][j].sort()
                idx=0
                while idx<len(forest[i][j]):
                    # 양분 섭취
                    if forest[i][j][idx]<=nourish[i][j]:
                        nourish[i][j]-=forest[i][j][idx]
                        forest[i][j][idx]+=1
                        idx+=1
                    # 양분 없음
                    else:
                        die=forest[i][j][idx:]
                        # 여름
                        for d in die:
                            nourish[i][j]+=(d//2)
                        forest[i][j]=forest[i][j][:idx]
                        break

# 가을, 겨울 (나무 번식, 양분 추가)
def autumnTowinter():
    # 가을
    for i in range(1,n+1):
        for j in range(1,n+1):
            nourish[i][j] += A[i][j]    # 겨울
            if forest[i][j]:
                for k in forest[i][j]:  # k : 나무 나이
                    if k%5==0:
                        for d in range(8):
                            ni,nj=i+direction[d][0],j+direction[d][1]
                            if 0<ni<=n and 0<nj<=n:
                                # 나이가 1인 나무 생김
                                forest[ni][nj].append(1)

n,m,k=map(int,sys.stdin.readline().split())
# 겨울에 추가 될 양분 list
A=[[0]*(n+1)]+[[0]+list(map(int,sys.stdin.readline().split())) for _ in range(n)]
nourish=[[5]*(n+1) for _ in range(n+1)]  # 땅의 양분 나타내는 list
forest=[[[] for _ in range(n+1)] for _ in range(n+1)]   # 나무들 나이
result=0
for _ in range(m):
    x,y,a=map(int,sys.stdin.readline().split())
    forest[x][y].append(a)
for _ in range(k):
    springTosummer()
    autumnTowinter()
for i in range(1,n+1):
    for j in range(1,n+1):
        result+=len(forest[i][j])
print(result)