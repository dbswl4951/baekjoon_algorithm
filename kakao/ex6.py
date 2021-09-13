'''
- 내구도 <=0 : 파괴 됨
- 회복으로 내구도 올리면 복구 가능
- 내구도 0이하인것도 계속 내구도 -

- type 1 : 공격
- type 2 : 회복

파괴되지 않은 건물 개수 구하기

정확성 100
효율성 0
'''
def change(board,x1,y1,x2,y2,degree):
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            board[i][j]+=degree
    return board

def solution(board, skill):
    result = 0
    for sk in skill:
        type,x1,y1,x2,y2,degree = sk
        if type==1:
            board = change(board,x1,y1,x2,y2,-degree)
        else:
            board = change(board,x1,y1,x2,y2,degree)

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]>0: result+=1
    return result

print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]],[[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]))
print(solution([[1,2,3],[4,5,6],[7,8,9]],[[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]))