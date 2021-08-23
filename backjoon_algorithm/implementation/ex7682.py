#틱택토
'''
[발생 할 수 있는 최종 상태 ]
1. xNum = oNum
    1) 'O'빙고
2. xNum = oNum+1
    1) xNum = 5, oNum=4
    2) 'X'빙고
'''
import sys

# 3칸이 이어지는지 확인 (빙고인지 확인)
def checkBingo(xo):
    # 가로, 세로 체크
    for i in range(3):
        if board[i][0]==board[i][1]==board[i][2]==xo: return 1
        if board[0][i]==board[1][i]==board[2][i]==xo: return 1
    # 대각선 체크
    if board[0][0]==board[1][1]==board[2][2]==xo: return 1
    if board[0][2]==board[1][1]==board[2][0]==xo: return 1
    return 0

while True:
    temp = sys.stdin.readline().strip()
    if temp=='end': break

    result='invalid'
    xNum,oNum,board=0,0,[]
    for i in range(0,9,3):
        board.append(temp[i:i+3])
        for j in range(3):
            if board[i//3][j]=='X': xNum+=1
            elif board[i//3][j]=='O': oNum+=1

    if not xNum==oNum and not xNum==oNum+1:
        print(result)
        continue

    # 빙고인지 아닌지 확인
    xBingo = checkBingo('X')
    oBingo = checkBingo('O')

    if xNum==oNum and not xBingo and oBingo: result='valid'
    elif xNum==oNum+1:
        if xBingo and not oBingo: result='valid'
        elif not xBingo and not oBingo and xNum==5 and oNum==4: result='valid'
    print(result)