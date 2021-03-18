#종이 조각
'''
비트 마스크 사용
비트 마스크 개념은 처음인데 잘 익혀놔야겠다
'''
import sys,itertools

#1차원 배열 => 2차원 bitmask 배열로 변환
def matrix(case,m):
    return [case[i:i+m] for i in range(0,len(case),m)]

n,m=map(int,sys.stdin.readline().split())
board=[]
for _ in range(n):
    board.append(list(map(int,sys.stdin.readline().strip())))
#[0,1]을 선택해서 n*m개 요소를 가지는 집합 반환 (0:가로, 1:세로)
case=itertools.product([0,1],repeat=n*m)
result=0
for c in case:
    bitMask=matrix(c,m)
    sumh=0  #누적 가로 합
    sumv=0  #누적 세로 합
    #가로 합 구하기
    for i in range(n):
        temp=0
        for j in range(m):
            #0: 가로 방향
            if bitMask[i][j]==0:
                temp=10*temp+board[i][j]
            #1: 세로 방향 만나거나 열이 배열의 끝일 때
            if bitMask[i][j]==1 or j==m-1:
                sumh+= temp  #그 전까지 가로 값 저장
                temp=0
    #세로 합 구하기
    for j in range(m):
        temp=0
        for i in range(n):
            #1: 세로 방향
            if bitMask[i][j]==1:
                temp=10*temp+board[i][j]
            #0: 가로 방향 만나거나 행이 배열의 끝일 때
            if bitMask[i][j]==0 or i==n-1:
                sumv+=temp  #그 전까지 세로 값 저장
                temp=0
    result=max(result,sumh+sumv)
print(result)