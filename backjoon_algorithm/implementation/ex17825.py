#주사위 윷놀이
'''
dfs+백트레킹

처음에 문제를 보고, 윷놀이 판을 어떻게 구현해야 할지 감이 안잡혔다
결국 구글 풀이 참고 후, 따라 풀었다
'''

# 말을 이동시키면서 모든 케이스 실행
def dfs(idx,sumVal):
    global result
    # 주사위 10번 굴렸으면, 최댓값 갱신 후 종료
    if idx==10:
        result=max(result,sumVal)
        return

    # 말 4개 이동
    for i in range(4):
        x,ix,move=chess[i],chess[i],dice[idx]   # (현재 위치, 이동전 초기 위치, 남은 이동 횟수)
        # 파란 칸에 도착 => 안쪽으로 이동
        if x in (5,10,15):
            x=moveIn[x]
            move-=1
        # 외곽을 따라 이동하는 경우
        if x+move<=21:
            x+=move
        else:
            for _ in range(move):
                x=board[x]

        # 이동 후, 현재 좌표에 말이 있고 도착 지점이 아니면 말 이동 저장하지 않음
        if check[x] and x!=21:
            continue

        check[ix],check[x],chess[i]=0,1,x
        dfs(idx+1,sumVal+scoreBorad[x])
        check[ix],check[x],chess[i]=1,0,ix


dice=list(map(int,input().split()))
chess=[0]*4     # 말 위치 저장
check=[0]*33    # 현재 인덱스에 말 있는지 저장
board=[0]*33    # 다음에 이동 할 인덱스 저장
for i in range(21):
    board[i]=i+1
# 끝지점은 도착지점을 반복
board[21]=21
# 10에서 안쪽으로 이동
board[22],board[23],board[24]=23,24,30
# 10에서 안쪽으로 이동
board[25],board[26]=26,30
# 30에서 안쪽으로 이동
board[27],board[28],board[29]=28,29,30
# 25에서 도착지점으로 이동
board[30],board[31],board[32]=31,32,20

moveIn=[0]*16   # 안쪽으로 들어가는 애들의 다음 좌표 저장
moveIn[5],moveIn[10],moveIn[15]=22,25,27
scoreBorad=[0]*33   # 점수가 적힌 board
for i in range(1,21):
    scoreBorad[i]=i*2
scoreBorad[22],scoreBorad[23],scoreBorad[24] = 13, 16, 19
scoreBorad[25],scoreBorad[26] = 22, 24
scoreBorad[27],scoreBorad[28],scoreBorad[29] = 28, 27, 26
scoreBorad[30],scoreBorad[31],scoreBorad[32] = 25, 30, 35

result=0
dfs(0,0)
print(result)