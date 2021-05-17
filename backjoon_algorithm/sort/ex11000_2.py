#강의실 배정
import sys,heapq

n=int(sys.stdin.readline().strip())
arr=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
# 끝나는 시간으로 정렬
arr.sort(key=lambda x:(-x[1],-x[0]))
result=1
q=[]
# 최대힙처럼 사용하기 위해서 음수로 저장
heapq.heappush(q,-arr[0][0])
for i in range(1,n):
    s,e=arr[i]
    num=abs(heapq.heappop(q))
    if num<e:
        result+=1
        heapq.heappush(q,-num)
    heapq.heappush(q,-s)
print(result)