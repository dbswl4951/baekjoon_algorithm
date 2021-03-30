#행렬
'''
1. 3x3매트릭스의 특성을 고려하면 x의 범위는 [0~N-3] 이고 y의 범위는 [0~M-3]이다.
2. [i][j]를 하나씩 늘려가며, flip(x,y)연산을 호출한다.
3. 마지막에는 A행렬과 B행렬이 같은지를 확인하고 같다면 flip 호출 횟수를, 다르다면 -1을 반환한다.
'''
n,m=map(int,input().split())
matrixA=[list(map(int,list(input()))) for _ in range(n)]
matrixB=[list(map(int,list(input()))) for _ in range(n)]

def flip(x,y):
    for i in range(x,x+3):
        for j in range(y,y+3):
            matrixA[i][j]=1-matrixA[i][j]

def checkEquality():
    for i in range(n):
        for j in range(m):
            if matrixA[i][j]!=matrixB[i][j]:
                return 0

count=0
for i in range(n-2):
    for j in range(m-2):
        if matrixA[i][j]!=matrixB[i][j]:
            flip(i,j)
            count+=1
if checkEquality()==0:
    print(-1)
else:
    print(count)