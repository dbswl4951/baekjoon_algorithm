#이차원 배열과 연산
import sys
from collections import Counter
from functools import reduce

def rcSort(board):
   m=0
   for i in range(len(board)):
       counter=Counter(board[i])
       #0 제거
       del counter[0]
       counter=list(counter.items())
       counter.sort(key=lambda x:(x[1],x[0]))
       #크기가 100넘으면 그 이상 무시
       if len(counter)>50: counter=counter[:50]
       #reduce(함수 식, 반복 객체) : 누적 집계 낼 때 사용
       #초기 값:list(counter[0]), counter[1:]부터 값 누적하면서 list(x)+list(y) 실행
       board[i]=reduce(lambda x,y:list(x)+list(y),counter[1:],list(counter[0]))
       m=max(m,len(board[i]))
       #길이 맞추기 위해 0 추가
       for i in range(len(board)):
           if len(board[i])<m:
               board[i].extend([0]*(m-len(board[i])))

r,c,k=map(int,sys.stdin.readline().split())
r,c=r-1,c-1
board=[]
for _ in range(3):
    board.append(list(map(int,sys.stdin.readline().split())))
result=0
if r<len(board) and c<len(board[0]) and board[r][c]==k:
    print(result)
    sys.exit(0)
while True:
    #R 연산
    if len(board)>=len(board[0]):
        rcSort(board)
    #C 연산
    else:
        board=list(map(list,zip(*board)))   #Transpose
        rcSort(board)
        board=list(map(list,zip(*board)))   #Transpose
    result+=1
    if result>100:
        print(-1)
        sys.exit(0)
    if r<len(board) and c<len(board[0]) and board[r][c]==k: break
print(result)