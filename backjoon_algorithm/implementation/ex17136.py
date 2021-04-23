#색종이 붙이기
'''
큰 색종이부터 붙이면 안됨
모든 케이스에 대해서 dfs 실행해야함!
=> 브루트포스
'''

def dfs(x,y,cnt):
    global result
    # 탐색 끝
    if y>9:
        result=min(result,cnt)
        return
    if x>9:
        dfs(0,y+1,cnt)
        return

    if board[x][y]:
        for k in range(5):
            if paper[k]==0: continue
            if x+k>9 or y+k>9: continue

            flag=0
            for i in range(x,x+k+1):
                for j in range(y,y+k+1):
                    # k번 색종이를 붙일 수 없음
                    if not board[i][j]:
                        flag=1
                        break
                if flag: break

            # k번 색종이 붙이기
            if not flag:
                paper[k]-=1
                for i in range(x,x+k+1):
                    for j in range(y,y+k+1):
                        board[i][j]=0

                # 다음 탐색
                dfs(x+k+1,y,cnt+1)

                # 색종이 떼기
                paper[k]+=1
                for i in range(x,x+k+1):
                    for j in range(y,y+k+1):
                        board[i][j]=1
    else:
        dfs(x+1,y,cnt)

board=[list(map(int,input().split())) for _ in range(10)]
paper=[5,5,5,5,5]
result=int(1e9)
dfs(0,0,0)
if result==int(1e9): print(-1)
else: print(result)