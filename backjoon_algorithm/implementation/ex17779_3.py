#게리맨더링 2

# 선거구 나누기
def divideArea(x,y,d1,d2):
    global result
    area = [[0] * (n + 1) for _ in range(n + 1)]  # 선거구 구역(1~5) 배열

    # 칸 경계 생성 => 선거구 5로 설정
    i,j = 0,0
    while i<=d1 and j>=-d1:
        area[x+i][y+j] = 5
        i += 1; j -=1
    i, j = 0, 0
    while i <= d2 and j<=d2:
        area[x + i][y + j] = 5
        i += 1; j += 1
    i, j = d1, -d1
    while i <= d1+d2 and j <= -d1+d2:
        area[x + i][y + j] = 5
        i += 1; j += 1
    i, j = d2, d2
    while i <= d1 + d2 and j >=d2-d1:
        area[x + i][y + j] = 5
        i += 1; j -= 1

    # 경계선 안은 선거구 5
    for i in range(x+1,x+d1+d2):
        flag = 1
        for j in range(1,n+1):
            if area[i][j] == 5:
                flag*=-1
                if flag==1: break
            if flag==-1:
                area[i][j] = 5

    # 선거구 1~4 설정
    for i in range(1,x+d1):
        for j in range(1,y+1):
            if area[i][j]==0: area[i][j] = 1
    for i in range(1,x+d2+1):
        for j in range(y+1,n+1):
            if area[i][j] == 0: area[i][j] = 2
    for i in range(x+d1,n+1):
        for j in range(1,y-d1+d2):
            if area[i][j] == 0: area[i][j] = 3
    for i in range(d2+1,n+1):
        for j in range(y-d1+d2,n+1):
            if area[i][j] == 0: area[i][j] =4

    people = [0,0,0,0,0]
    # 인구 차이의 최솟값 구하기
    for i in range(1,n+1):
        for j in range(1,n+1):
            num = area[i][j]
            people[num-1] += board[i][j]
    result = min(result,max(people)-min(people))

n = int(input())
board = [[0]*(n+1)] + [[0]+list(map(int,input().split())) for _ in range(n)]
result = int(1e9)
for x in range(1,n+1):
    for y in range(1,n+1):
        for d1 in range(1,n+1):
            for d2 in range(1,n+1):
                if d1+d2<=n-x and d1<=y-1 and d2<=n-y:
                    divideArea(x,y,d1,d2)
print(result)