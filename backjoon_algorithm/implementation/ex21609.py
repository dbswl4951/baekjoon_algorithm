#상어 중학교
'''
[ PLAY ]
1. 크기가 가장 큰 블록 그룹 찾기
    1) 여러개라면 무지개 블록이 많은 것
    2) (1)이 여러개 => 기준 블록 행이 큰거
    3) (2)가 여러개 => 기준 블록 열이 가장 큰거
            (1) 방문하지 않은 모든 좌표에서 BFS 실행
            (2) 이 때, 무지개 블록은 방문 체크 X
            (3) 가장 크기가 가장 큰 블록 그룹 리턴
2. 1에서 찾은 블록 모두 제거 + (블록 수^2)점 획득
3. 검은 블록 제외 모든 블록 중력 작용
            (1) 열 한 개씩 검은색 블록이 있는지 확인
            (2) 검은색 블록 O
                몇번째 행인지 저장
                그 행보다 작은 행들 블록 행 큰 애들부터 검사 (내려갈 수 있는지 없는지)
                내려갈 수 있다면 다른 블록 or 검은색 블록 위 or 바닥에 도달 할 때까지 중력 작용
            (3) 검은색 블록 X
                아래부터 내려갈 수 있는지 없는지 검사
                내려갈 수 있으면 다른 블록 or 바닥 만나기 전까지 계속 중력 작용
4. 모든 블록 90도 반시계 방향 회전
5. 3번 다시 실행
'''
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 가장 크기가 큰 블록 그룹 찾기
def findBolckGroup(x,y,color):
    global nomalBlockCnt, colorBlockCnt, standardBlock, blockGroup

    q = deque()
    q.append([x,y])
    visited = [[0]*n for _ in range(n)]     # 일반 + 무지개 블록 방문 체크
    visited[x][y]=1
    nomalCnt,colorCnt,standard = 1,0,[x,y]     # 일반 블록 개수, 무지개 블록 개수, 기준 블록 (x,y)
    group = [[x,y]]

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<n and (board[nx][ny]==0 or board[nx][ny]==color) and not visited[nx][ny]:
                # 일반 블록
                if board[nx][ny] == color:
                    nomalVisited[nx][ny] = 1
                    nomalCnt += 1
                    # 기준 블록 찾기
                    if standard[0] == nx:
                        if standard[1] > ny:
                            standard = [nx, ny]
                    elif standard[0] > nx:
                        standard = [nx, ny]
                # 무지개 블록
                else:
                    colorCnt += 1

                visited[nx][ny]=1
                group.append([nx,ny])
                q.append([nx,ny])

    if nomalCnt+colorCnt > 1:
        # 무지개 블록 더 많은 애 찾기
        if nomalBlockCnt+colorBlockCnt == nomalCnt+colorCnt:
            if colorBlockCnt == colorCnt:
                # 기준 블록 행 큰거 찾기
                if standardBlock[0] == standard[0]:
                    if standardBlock[1] < standard[1]:
                        changeBlockGroup(nomalCnt,colorCnt,standard)
                        return group
                elif standardBlock[0] < standard[0]:
                    changeBlockGroup(nomalCnt,colorCnt,standard)
                    return group
            elif colorBlockCnt < colorCnt:
                changeBlockGroup(nomalCnt,colorCnt,standard)
                return group
        elif nomalBlockCnt+colorBlockCnt < nomalCnt+colorCnt:
            changeBlockGroup(nomalCnt,colorCnt,standard)
            return group
    return None

# 블록 그룹 변경
def changeBlockGroup(nomalCnt,colorCnt,standard):
    global nomalBlockCnt, colorBlockCnt, standardBlock, blockGroup

    nomalBlockCnt, colorBlockCnt = nomalCnt, colorCnt
    standardBlock = standard

# 블록 그룹 삭제 + 점수 얻기
def removeBlock(blockGroup):
    global result

    for block in blockGroup:
        board[block[0]][block[1]] = -2
    result += (len(blockGroup)**2)

# 중력 작용
def worksGravity():
    for j in range(n):
        top = -1
        for i in range(n-1,-1,-1):
            if board[i][j] != -2:
                if top != -1:
                    if i!=top-1 and board[i][j] != -1:
                        board[top-1][j] = board[i][j]
                        board[i][j] = -2
                        top = top-1
                    else: top = i
                else:
                    if board[i][j] != -1:
                        value = board[i][j]
                        board[i][j] = -2
                        board[n-1][j] = value
                        top = n-1
                    else:
                        top = i

# 반시계 방향으로 90도 회전
def rotate270():
    newBoard = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            newBoard[n-1-j][i] = board[i][j]
    return newBoard

n,m = map(int,input().split())
board=[list(map(int,input().split())) for _ in range(n)]
result = 0
while True:
    nomalVisited = [[0] * n for _ in range(n)]  # 일반 블록 방문 체크 리스트
    nomalBlockCnt,colorBlockCnt,standardBlock,blockGroup = 0,0,[],[]

    # 가장 크기가 큰 블록 그룹 찾기
    for i in range(n):
        for j in range(n):
            if board[i][j]>0 and not nomalVisited[i][j]:
                nomalVisited[i][j]=1
                group = findBolckGroup(i,j,board[i][j])
                if group: blockGroup = group

    # 블록 삭제 + 점수 얻기
    if blockGroup: removeBlock(blockGroup)
    else: break

    # 중력 작용
    worksGravity()
    # 반시계 방향 회전
    board = rotate270()
    # 중력 작용
    worksGravity()
print(result)