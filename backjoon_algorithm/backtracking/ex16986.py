#인싸들의 가위바위보
import sys
'''
무승부 일 때, '경기 진행 순서 상 뒤인 사람이 이김'

즉, 순서가 A->B->C로 진행되고,
C vs A가 무승부라면 C가 이기도록 함

그냥 순서가 뒤인 사람(A)이 이기게 된다고 생각했는데, 아니였음
이거 때문에 엄청 시간 낭비했다 ㅠ 문제 설명이 참
'''

def dfs(bIdx,cIdx,now,next,victory):
    global result

    if victory[0]==k:
        result = 1
        return
    if victory[1]==k or victory[2]==k:
        return

    if now == 0:
        # A vs B
        if next==1:
            nextPic = bList[bIdx]
            for i in range(n):
                if not visited[i]:
                    visited[i] = 1
                    if info[i][nextPic]==2:
                        victory[0] += 1
                        dfs(bIdx+1,cIdx,0,2,victory)
                        victory[0] -= 1
                    else:
                        victory[1] += 1
                        dfs(bIdx+1,cIdx,1,2,victory)
                        victory[1] -= 1
                    visited[i]=0
        # A vs C
        else:
            nextPic = cList[cIdx]
            for i in range(n):
                if not visited[i]:
                    visited[i] = 1
                    if info[i][nextPic] == 2:
                        victory[0] += 1
                        dfs(bIdx, cIdx+1, 0, 1, victory)
                        victory[0] -= 1
                    else:
                        victory[2] += 1
                        dfs(bIdx, cIdx+1, 2, 1, victory)
                        victory[2] -= 1
                    visited[i] = 0

    elif now == 1:
        # B vs A
        if next == 0:
            nextPic = bList[bIdx]
            for i in range(n):
                if not visited[i]:
                    visited[i] = 1
                    if info[i][nextPic] == 2:
                        victory[0] += 1
                        dfs(bIdx+1, cIdx, 0, 2, victory)
                        victory[0] -= 1
                    else:
                        victory[1] += 1
                        dfs(bIdx+1, cIdx, 1, 2, victory)
                        victory[1] -= 1
                    visited[i] = 0
        # B vs C
        else:
            if info[bList[bIdx]][cList[cIdx]] == 2:
                victory[1] += 1
                dfs(bIdx + 1, cIdx+1, 1, 0, victory)
                victory[1] -= 1
            else:
                victory[2] += 1
                dfs(bIdx + 1, cIdx+1, 2, 0, victory)
                victory[2] -= 1

    else:
        # C vs A
        if next == 0:
            nextPic = cList[cIdx]
            for i in range(n):
                if not visited[i]:
                    visited[i] = 1
                    if info[i][nextPic] == 2:
                        victory[0] += 1
                        dfs(bIdx, cIdx+1, 0, 1, victory)
                        victory[0] -= 1
                    else:
                        victory[2] += 1
                        dfs(bIdx, cIdx+1, 2, 1, victory)
                        victory[2] -= 1
                    visited[i] = 0
        # C vs B
        else:
            if info[bList[bIdx]][cList[cIdx]] == 2:
                victory[1] += 1
                dfs(bIdx + 1, cIdx + 1, 1, 0, victory)
                victory[1] -= 1
            else:
                victory[2] += 1
                dfs(bIdx + 1, cIdx + 1, 2, 0, victory)
                victory[2] -= 1

n,k = map(int,sys.stdin.readline().split())
info = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
bList = [int(x) -1 for x in sys.stdin.readline().split()]
cList = [int(x) -1 for x in sys.stdin.readline().split()]
visited = [0]*n
result = 0
dfs(0,0,0,1,[0,0,0])
print(result)