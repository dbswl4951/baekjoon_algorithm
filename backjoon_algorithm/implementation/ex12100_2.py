#2048 (Easy)
'''
< POINT >
1) dfs 실행 하기 전마다 board의 상태를 copy로 저장
2) 재귀가 끝난 후, 그 전 상태로 돌아가기 위해 copy 한 board 값 가져와서 다시 재귀 실행
그렇지 않으면, board의 상태가 바뀌기 때문에 그 전 함수로 돌아 갔을 때 문제 발생!!
'''
import copy

# 한 턴 시작 => 모든 블럭 한 방향으로 이동
def turnStart(dir):
    # 위쪽 방향으로 블럭 이동
    if dir==0:
        for j in range(n):
            idx=0   # idx : 블럭이 놓여야 할 위치
            for i in range(1, n):
                if board[i][j]:
                    temp = board[i][j]
                    board[i][j] = 0
                    # 같은 수 => 블럭 합치기
                    if temp == board[idx][j]:
                        board[idx][j] *= 2
                        idx += 1
                    # 빈 칸으로 이동
                    elif board[idx][j] == 0:
                        board[idx][j] = temp
                    # 합칠 수 없는 경우
                    else:
                        idx += 1
                        board[idx][j] = temp

    # 아래 방향으로 블럭 이동
    elif dir==1:
        for j in range(n):
            idx = n-1
            for i in range(n-2,-1,-1):
                if board[i][j]:
                    temp=board[i][j]
                    board[i][j]=0
                    if temp==board[idx][j]:
                        board[idx][j]*=2
                        idx-=1
                    elif board[idx][j]==0:
                        board[idx][j]=temp
                    else:
                        idx-=1
                        board[idx][j]=temp

    # 왼쪽으로 블럭 이동
    elif dir==2:
        for i in range(n):
            idx = 0
            for j in range(1,n):
                if board[i][j]:
                    temp=board[i][j]
                    board[i][j]=0
                    if temp==board[i][idx]:
                        board[i][idx]*=2
                        idx+=1
                    elif board[i][idx]==0:
                        board[i][idx]=temp
                    else:
                        idx+=1
                        board[i][idx]=temp

    # 오른쪽으로 블럭 이동
    else:
        for i in range(n):
            idx = n - 1
            for j in range(n-2,-1,-1):
                if board[i][j]:
                    temp = board[i][j]
                    board[i][j] = 0
                    if temp == board[i][idx]:
                        board[i][idx]*=2
                        idx-= 1
                    elif board[i][idx] == 0:
                        board[i][idx] = temp
                    else:
                        idx-= 1
                        board[i][idx] = temp

def dfs(cnt):
    global result,board
    if cnt==5:
        for b in board:
            result = max(result, max(b))
        return

    # 합치기 전 상태 저장
    tBoard=copy.deepcopy(board)
    for i in range(4):
        # 블럭 합치기
        turnStart(i)
        dfs(cnt+1)
        # 재귀가 끝난 후, 그 전 board의 상태 가져옴
        board=copy.deepcopy(tBoard)

n=int(input().strip())
board=[list(map(int,input().split())) for _ in range(n)]
result=0
dfs(0)
print(result)