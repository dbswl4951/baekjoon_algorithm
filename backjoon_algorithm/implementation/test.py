def rotate_90(board):
    N = len(board)
    M=len(board[0])
    ret = [[0] * M for _ in range(N)]

    for r in range(N):
        for c in range(M):
            ret[c][N-1-r] = board[r][c]
    return ret


arr=[[1,1,1,1],[2,2,2,2],[3,3,3,3]]
print(list(map(list,zip(*arr))))
print(rotate_90(arr))