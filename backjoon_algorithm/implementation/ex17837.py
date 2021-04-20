#새로운 게임2
'''
< 1차 시도 - 실패 >
처음에 deque를 사용 해서 모든 체스 (x,y,방향) 저장, popleft(), 이동 후 다시 저장...
형태로 한게 실패 요인
=> 말 위에 있는 말들도 같이 이동하므로, deque에 (x,y)좌표를 저장하면 안됨!!
=> 말 한 개만 옮겨도, 연관된 다른 말들의 좌표 (x,y)가 다같이 변경되기 때문

< 2차 시도 >
말을 chess list (x, y, 방향)에 저장 후, 순서 그대로 유지 한 채 x,y,d만 바꿔준다!!

< 느낀점 >
1. 이 문제와 같이 한 객체의 이동이 다른 객체 좌표 이동에 영향을 미친다면,
모든 좌표를 deque에 저장해 popleft()로 꺼내서 사용하는 것은 옮지 않음!!
2. 파란색/범위밖 => 방향 반대로 설정 => 이동하려는 칸이 흰색or빨간색 이여서 옮길 수 있을 때
처음부터 흰색/빨간색 칸을 만난 것과 같이 실행 됨!
따라서 처리 순서 :: 파란색/범위밖 먼저 처리 후, 그 후에 빨간색/흰색 칸 만났을 때를 처리
'''

dx=[0,0,-1,1]
dy=[1,-1,0,0]

# num번 말 옮기기
def move(num):
    x,y,d=chess[num]
    nx,ny=x+dx[d],y+dy[d]
    # 범위 밖 or 파란색 칸으로 이동
    if not 0<=nx<n or not 0<=ny<n or board[nx][ny]==2:
        if 0<=d<=1: nd=(d+1)%2
        else: nd=(d-1)%2+2
        chess[num][2]=nd
        nx,ny=x+dx[nd],y+dy[nd]
        # 방향 반대로 바꾼 후에도 이동 할 수 없으면 return 0
        if not 0<=nx<n or not 0<=ny<n or board[nx][ny]==2: return 0

    chessSet=[]     # num번 ~ 맨 위의 말까지 임시 저장
    for idx,key in enumerate(chessMap[x][y]):
        if num==key:
            chessSet.extend(chessMap[x][y][idx:])
            chessMap[x][y]=chessMap[x][y][:idx]
            break

    # 빨간 칸으로 이동
    if board[nx][ny]==1:
        chessSet=chessSet[-1::-1]

    # 말 이동 갱신
    for cNum in chessSet:
        chessMap[nx][ny].append(cNum)
        chess[cNum][:2]=[nx,ny]

    # 말 4개 이상 쌓였는지 확인
    if len(chessMap[nx][ny])>=4: return 1
    return 0

n, k = map(int,input().split())
board=[list(map(int, input().split())) for _ in range(n)]
chessMap=[[[] for _ in range(n)] for _ in range(n)]     # 말 번호 저장
chess = [0 for _ in range(k)]   # 체스 (x, y, 방향) 저장
for i in range(k):
    x,y,d=map(int,input().split())
    chessMap[x-1][y-1].append(i)
    chess[i]=[x-1,y-1,d-1]

time=1
while time<=1000:
    flag=0
    # 말 하나씩 옮기기
    for i in range(k):
        flag=move(i)
        if flag: break
    if flag: break
    time+=1
if time==1001: print(-1)
else: print(time)