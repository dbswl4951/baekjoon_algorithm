#여왕벌
'''
애벌레가 자랄 때마다 board 업데이트 => 시간초과 발생

1행 1열 ~ 이후에는 0행 i열과 값 동일
따라서 왼쪽 아래 ~ 오른쪽 위까지 n일동안 자라는 정도 누적합 구하기 (day)
1열 이후 는 0열과 동일하게 설정
'''
import sys

m,n=map(int,sys.stdin.readline().split())
board=[[1]*m for _ in range(m)]
day=[0 for i in range(m*2-1)]
for _ in range(n):
    a,b,c=map(int,sys.stdin.readline().split())
    for i in range(a,a+b):
        day[i]+=1
    for i in range(a+b,2*m-1):
        day[i]+=2
# 0열 (맨 왼쪽)
for i in range(m-1,-1,-1):
    board[i][0]+=day[m-i-1]
# 0행 (맨 위)
for i in range(1,m):
    board[0][i]+=day[i+m-1]
# 나머지
for i in range(1,m):
    for j in range(1,m):
        board[i][j]=board[i-1][j]
for b in board:
    print(*b)