def rotation(board,queries):
    result=[]
    for i in range(len(queries)):
        s = set()
        x1,y1,x2,y2=queries[i]
        temp=board[x1][y2]
        s.add(temp)
        # 위쪽
        for j in range(y2,y1,-1):
            board[x1][j]=board[x1][j-1]
            s.add(board[x1][j])
        # 왼쪽
        for j in range(x1,x2):
            board[j][y1]=board[j+1][y1]
            s.add(board[j][y1])
        # 아래
        for j in range(y1,y2):
            board[x2][j]=board[x2][j+1]
            s.add((board[x2][j]))
        # 오른쪽
        for j in range(x2,x1,-1):
            board[j][y2]=board[j-1][y2]
            s.add(board[j][y2])
        board[x1+1][y2]=temp
        result.append(min(s))
    return result

def solution(rows, columns, queries):
    board=[[0]*(columns+1) for _ in range(rows+1)]
    for i in range(1,rows+1):
        for j in range(1,columns+1):
            board[i][j]=((i-1)*columns+j)
    return rotation(board,queries)

print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
print(solution(3,3,[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))
print(solution(100,97,[[1,1,100,97]]))