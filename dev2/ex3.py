from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(board,i,j,color):
    q = deque()
    q.append([i,j])
    visit = [[0]*7 for _ in range(7)]
    visit[i][j] = 1
    maca = [[i,j]]

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0<nx<7 and 0<ny<7 and board[nx][ny]==color and not visit[nx][ny]:
                visit[nx][ny] = 1
                q.append([nx,ny])
                maca.append([nx,ny])

    if len(maca)>2: return maca
    return None

def solution(macaron):
    board = [[0]*7 for _ in range(7)]
    top = [6,6,6,6,6,6,6]

    for num,color in macaron:
        print('num, color : ',num,color,top)
        # 마카롱 쌓기
        board[top[num]][num] = color
        top[num] -= 1
        print('마카롱 쌓은 후')
        for b in board: print(b)

        # 마카롱 터트릴 수 있는지 확인
        while True:
            flag,check = 1,0
            for i in range(1, 7):
                for j in range(1, 7):
                    if board[i][j] != 0:
                        maca = bfs(board, i, j, board[i][j])
                        print('maca : ',i,j,board[i][j],maca)
                        if maca == None:
                            if not check: flag=0
                            continue

                        mySet = set()
                        #print('maca : ',maca)
                        # 마카롱 터트리기
                        for mx,my in maca:
                            board[mx][my] = 0
                            mySet.add(my)
                            check = 1
                        print('마카롱 터진 후')
                        for b in board: print(b)

                        # 아래방향으로 떨어트리기
                        for my in mySet:
                            #print('my : ',my)
                            cnt = 0
                            for mx in range(6,0,-1):
                                if board[mx][my]==0:
                                    cnt += 1
                                else:
                                    if cnt!=0:
                                        board[mx+cnt][my] = board[mx][my]
                                        board[mx][my] = 0
                        print('마카롱 떨어진 후')
                        for b in board: print(b)

                        # top 갱신
                        for j in range(1,7):
                            for i in range(6,0,-1):
                                if board[i][j]==0:
                                    top[j] = i
                                    break
                        print('top : ',top)
                    if check: break
                if check: break
            if not flag: print('break!!!'); break

    result = []
    for i in range(1,7):
        temp = ''
        for j in range(1,7):
            temp += str(board[i][j])
        result.append(temp)
    return result

#print(solution([[1,1],[2,1],[1,2],[3,3],[6,4],[3,1],[3,3],[3,3],[3,4],[2,1]]))
print(solution([[1,1],[1,2],[1,4],[2,1],[2,2],[2,3],[3,4],[3,1],[3,2],[3,3],[3,4],[4,4],[4,3],[5,4],[6,1]]))
#print(solution([[4,3],[1,3],[2,3],[3,3],[4,1],[2,1],[3,1],[4,3],[3,3],[4,3],[1,3]]))