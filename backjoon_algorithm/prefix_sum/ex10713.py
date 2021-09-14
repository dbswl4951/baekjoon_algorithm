#기차 여행
'''
도로를 지나는 횟수를 구하기 위해 모든 도로 index에 접근하면 n^2로 시간초과
'''
import sys

n,m = map(int,sys.stdin.readline().split())
move = list(map(int,sys.stdin.readline().split()))
edges=[list(map(int,sys.stdin.readline().split())) for _ in range(n-1)]
count=[0]*(n+1)

# 시작지점에서 +1, 끝지점에서 -1
for i in range(m-1):
    if move[i]<move[i+1]:
        count[move[i]]+=1
        count[move[i+1]]-=1
    else:
        count[move[i+1]]+=1
        count[move[i]]-=1
# 앞, 뒤 노드를 더하면 i+1번째 철로를 지나는 횟수를 구할 수 있음
for i in range(1,n):
    count[i]+=count[i-1]

result=0
# 최소 비용 구하기
for i in range(1,n):
    if count[i]:
        result+=min(edges[i-1][2]+count[i]*edges[i-1][1],edges[i-1][0]*count[i])
print(result)