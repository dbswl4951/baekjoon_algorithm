#택배
'''
시작지점이 아닌 도착지점순으로 정렬 하는 것이 POINT!
'''
import sys

n,c=map(int,sys.stdin.readline().split())
m=int(sys.stdin.readline().strip())
delivery=[list(map(int, sys.stdin.readline().split())) for _ in range(m)]
#도착지 순으로 정렬
delivery.sort(key=lambda x:x[1])
result=0
remain=[c]*(n+1)  #i번째 마을에서 트럭에 실을 수 있는 짐 (남은 공간)
for i in range(m):
    minNum=c
    #도착지까지 거쳐가는 마을에서의 남아있는 트럭 공간 검사하면서, 가장 작은 공간 저장
    for j in range(delivery[i][0],delivery[i][1]):
        minNum=min(minNum,remain[j])
    #트럭 남은 공간, 짐의 무게 중 더 작은 값 선택 (남은 공간 < 짐의 무게 : 남은 공간만큼만 저장 가능)
    minNum=min(minNum,delivery[i][2])
    #시작점의 남은 트럭 공간 갱신
    for j in range(delivery[i][0],delivery[i][1]):
        remain[j]-=minNum
    result+=minNum
print(result)