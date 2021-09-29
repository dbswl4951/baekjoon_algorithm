#팀원 모집
'''
쉬운 문젠데 ... 문제를 잘못봐서 고생한 문제
문제를 잘 읽자 ㅠㅠ
'''
import sys

def dfs(idx,qCount,sCount,visited,check):
    global result

    if qCount == 0:
        result = min(result,sCount)
        return

    for i in range(idx,m):
        if not visited[i]:
            visited[i]=1
            qCnt = qCount
            s = set()
            for a in arr[i]:
                if not check[a]:
                    qCnt-=1
                    check[a]=1
                    s.add(a)
            dfs(i+1,qCnt,sCount+1,visited,check)
            for ss in s:
                check[ss] = 0
        visited[i]=0

n,m = map(int,sys.stdin.readline().split())
arr = []
for _ in range(m):
    temp = list(map(int,sys.stdin.readline().split()))
    arr.append(temp[1:])
visited,check = [0]*(m+1), [0]*(n+1)
result = int(1e9)
dfs(0,n,0,visited,check)
if result==int(1e9): print(-1)
else: print(result)