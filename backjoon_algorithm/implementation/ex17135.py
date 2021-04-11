#캐슬 디펜스
'''
1. 궁수 3명 배치 할 위치 정하기 (조합)
2. for문으로 x:n-1부터 0까지 적의 위치 구하기
    1) 위치가 d이하면 적 삭제 + result+1
3. 적들 한 칸씩 아래로 밀기
'''
import sys,copy
from itertools import combinations

# 궁수 한 명 당 죽일 수 있는 적 return
def checkAble(tempBoard,archer):
    able=[]
    for i in range(n-1,-1,-1):
        for j in range(m):
            dist=abs(archer[0] - i) + abs(archer[1] - j)
            if tempBoard[i][j]==1 and dist<=d:
                able.append([dist,i,j])
    if able:
        able.sort(key=lambda x:(x[0],x[2]))
        return able[0]
    return

n,m,d=map(int,sys.stdin.readline().split())
board=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
r=[i for i in range(m)]
result = 0

for case in combinations(r,3):
    kill=[]
    count=0
    tempBoard=copy.deepcopy(board)
    archers=[[n,case[0]],[n,case[1]],[n,case[2]]]

    while True:
        for archer in archers:
            temp=checkAble(tempBoard,archer)
            if temp!=None:
                kill.append(temp)
        for k in kill:
            if tempBoard[k[1]][k[2]]==1:
                tempBoard[k[1]][k[2]]=0
                count+=1
        tempBoard=[[0]*m]+tempBoard[:n-1][:]
        kill.clear()
        s=0
        for i in range(n):
            s+=sum(tempBoard[i])
        if s==0: break
    result=max(result,count)

print(result)