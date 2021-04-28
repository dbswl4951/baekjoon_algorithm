#게리맨더링 2

# 인수 차이 최솟값 구하기
def getMinPopulation(area):
    global result
    sumList=[0]*5
    for i in range(1,n+1):
        for j in range(1,n+1):
            sumList[area[i][j]-1]+=board[i][j]
    minVal,maxVal=min(sumList),max(sumList)
    result=min(result,maxVal-minVal)

# 선거구 만들기
def makeArea(d1,d2,x,y):
    area = [[0] * (n + 1) for _ in range(n + 1)]
    # 경계선
    for i in range(d1+1):
        area[x+i][y-i]=5
        area[x+d2+i][y+d2-i]=5
    for i in range(d2+1):
        area[x+i][y+i]=5
        area[x+d1+i][y-d1+i] = 5

    # 5구역 (경계선 안 채우기)
    temp=[]
    for i in range(x+1,x+d1+d2):
        flag=0
        for j in range(y-d1,y+d2+1):
            if area[i][j]==5: flag+=1
            if flag==2: break
            if not area[i][j] and flag==1: temp.append([i,j])
    for tx,ty in temp:
        area[tx][ty]=5

    # 1구역
    for i in range(1,x+d1):
        for j in range(1,y+1):
            if not area[i][j]: area[i][j]=1
    # 2구역
    for i in range(1,x+d2+1):
        for j in range(y+1,n+1):
            if not area[i][j]: area[i][j] =2
    # 3구역
    for i in range(x+d1,n+1):
        for j in range(1,y-d1+d2):
            if not area[i][j]: area[i][j]=3
    # 4구역
    for i in range(x+d2+1,n+1):
        for j in range(y-d1+d2,n+1):
            if not area[i][j]: area[i][j] =4
    return area

n=int(input().strip())
board=[[0]*(n+1)]+[[0]+list(map(int,input().split())) for _ in range(n)]
result=int(1e9)
# d1,d2,x,y 선택
for d1 in range(1,n//2+1):
    for d2 in range(1,n//2+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if i+d1+d2<=n and 1<=j-d1 and j+d2<=n:
                    area=makeArea(d1,d2,i,j)
                    # 인구 차이 최소 구하기
                    getMinPopulation(area)
print(result)