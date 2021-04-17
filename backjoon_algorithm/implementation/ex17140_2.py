#이차원 배열과 연산
from collections import Counter

def rc(board):
    maxLen=0
    for i in range(len(board)):
        temp=[j for j in board[i] if j!=0]
        temp=Counter(temp).most_common()
        temp.sort(key=lambda x:(x[1],x[0]))
        # 길이가 100 넘으면 100까지만 저장
        if len(temp)>50: temp=temp[:50]
        board[i]=[]
        for x,y in temp:
            board[i].append(x)
            board[i].append(y)
        maxLen=max(maxLen,len(board[i]))

    # 빈 칸은 0으로 채우기
    for i in range(len(board)):
        for j in range(maxLen-len(board[i])):
            board[i].append(0)

r,c,k=map(int,input().split())
r,c=r-1,c-1
board=[list(map(int,input().split())) for _ in range(3)]
result=0
if r<len(board) and c<len(board[0]) and board[r][c]==k:
    print(0)
else:
    while result<101:
        result+=1
        # R연산
        if len(board)>=len(board[0]):
            rc(board)
        # C연산
        else:
            board=list(map(list,zip(*board)))
            rc(board)
            board=list(map(list,zip(*board)))
        if r<len(board) and c<len(board[0]) and board[r][c]==k: break
    if result==101: print(-1)
    else: print(result)