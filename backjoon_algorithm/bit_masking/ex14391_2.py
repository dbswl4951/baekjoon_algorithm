#종이 조각
import sys,itertools

# nXm 행렬로 변환
def makeMatrix(c):
    board=[[-1]*m for _ in range(n)]
    k=0
    for i in range(n):
        for j in range(m):
            board[i][j]=c[k]
            k+=1
    return board

def getMaxSum(board):
    global result
    score=0

    # 가로
    for i in range(n):
        temp=''
        for j in range(m):
            if board[i][j]==0:
                temp+=str(paper[i][j])
            # 세로행을 만나거나, 마지막 열이면 그전까지 수 더하기
            if temp!='' and (board[i][j]==1 or j==m-1):
                score+=int(temp)
                temp=''

    # 세로
    for j in range(m):
        temp=''
        for i in range(n):
            if board[i][j]==1:
                temp+=str(paper[i][j])
            # 가로행을 만나거나, 마지막 행이면 그 전까지 수 더하기
            if temp!='' and (board[i][j]==0 or i==n-1):
                score+=int(temp)
                temp=''
    result=max(result,score)

n,m=map(int,sys.stdin.readline().split())
paper=[list(map(int,sys.stdin.readline().strip())) for _ in range(n)]
# [0,1]을 선택해서 n*m개 요소를 가지는 집합 반환 (0:가로, 1:세로)
# product : 두 개 이상의 리스트의 조합 구하기
case=itertools.product([0,1],repeat=n*m)
result=0

for c in case:
    # 일차원 배열을 nXm 형태로 변환
    board=makeMatrix(c)
    # 가로, 세로 나눈대로 계산
    getMaxSum(board)
print(result)