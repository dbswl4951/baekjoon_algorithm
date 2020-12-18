#2048(Easy)
'''
dfs()함수 다시 이해해보기
dfs 알고리즘 공부 필요!!
재귀함수 너무 어렵다..
'''
import sys,copy

def move(direction):
    if direction==0:    #위쪽 방향으로 이동
        for j in range(n):
            idx=0   #0행부터 차례대로 검사하기 위한 변수
            for i in range(1,n):
                if board[i][j]: #0이 아니라면
                    temp=board[i][j]    #temp에 값 일시 저장
                    board[i][j]=0   #블럭이 옮겨졌다고 생각하고 0으로 수정
                    if board[idx][j]==0:    #위쪽이 비어있으면
                        board[idx][j]=temp  #저장한 temp값을 위쪽으로 옮김
                    elif board[idx][j]==temp:   #저장한 값과 위쪽에 있는 값이 같으면
                        board[idx][j]=temp*2   #블록 합침
                        idx+=1  #그 다음 행을 탐색하기 위해서
                    else:   #위쪽이 비어있지도, 같은 블럭도 아니라면
                        idx+=1  #그 위에 블럭을 쌓아야 하기 때문에 idx먼저 증가 시킨 후
                        board[idx][j]=temp  #임시저장한 값을 그대로 다시 보드에 넣음

    elif direction == 1:    #아래로 이동
        for j in range(n):
            idx = n - 1 #보드의 맨 아래 행
            for i in range(n - 2, -1, -1):
                if board[i][j]: #옮길 블럭이 있다면
                    temp = board[i][j]  #temp에 값 일시 저장 후
                    board[i][j] = 0 #블럭을 옮겼다 치고 0으로 수정
                    if board[idx][j] == 0:  #비어있다면
                        board[idx][j] = temp    #임시저장한 값 넣음 (아래로 이동)
                    elif board[idx][j] == temp: #옮길 값(temp)와 아래에 있는 블럭이 같다면
                        board[idx][j] = temp * 2    #블럭 합침
                        idx -= 1    #블럭이 쌓임
                    else:
                        idx -= 1
                        board[idx][j] = temp

    elif direction == 2:     #왼쪽으로 이동
        for i in range(n):
            idx = 0 #열을 나타 냄
            for j in range(1, n):
                if board[i][j]:
                    temp = board[i][j]
                    board[i][j] = 0
                    if board[i][idx] == 0:
                        board[i][idx] = temp
                    elif board[i][idx] == temp:
                        board[i][idx] = temp * 2
                        idx += 1
                    else:
                        idx += 1
                        board[i][idx] = temp

    else:   #오른쪽으로 이동
        for i in range(n):
            idx = n - 1
            for j in range(n - 2, -1, -1):
                if board[i][j]:
                    temp = board[i][j]
                    board[i][j] = 0
                    if board[i][idx] == 0:
                        board[i][idx] = temp
                    elif board[i][idx] == temp:
                        board[i][idx] = temp * 2
                        idx -= 1
                    else:
                        idx -= 1
                        board[i][idx] = temp

def dfs(count):
    global maxBlock,board
    if count==5:    #최대 5번 움직였다면 멈추고 전체 배열의 최대 값을 반환
        for i in range(n):
            for j in range(n):
                maxBlock=max(maxBlock,board[i][j])
        return
    copyBoard=copy.deepcopy(board)  #이동 전 보드의 상태 저장
    for i in range(4):
        move(i) #move()함수로 이동 뒤
        dfs(count+1)    #재귀적으로 호출
        board=copy.deepcopy(copyBoard)

n=int(sys.stdin.readline())
board=[]
for i in range(n):
    board.append(list(map(int,sys.stdin.readline().split())))
maxBlock=0
dfs(0)
print(maxBlock)