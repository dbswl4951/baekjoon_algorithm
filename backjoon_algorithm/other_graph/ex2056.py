#작업
'''
DP사용
'''
import sys

n=int(sys.stdin.readline().strip())
times=[0]*(n+1)
graph={}
#각 노드 전에 선행 되야 하는 노드들을 graph에 저장
for i in range(1,n+1):
    li=list(map(int,sys.stdin.readline().split()))
    times[i]=li[0]
    if li[1]==0: continue
    for j in li[2:]:
        if i in graph:
            graph[i].append(j)
        else:
            graph[i]=[j]
for i in range(1,n+1):
    if i in graph:
        time=0
        #i번째 노드 전에 선행 되야 하는 노드들 중 최대 시간으로 times[i] 업데이트
        #times[i]는 i번째 노드까지 걸리는 실행 시간
        for j in graph[i]:
            time=max(time,times[j])
        times[i]+=time
print(max(times))