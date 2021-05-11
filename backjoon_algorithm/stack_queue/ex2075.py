#N번째 큰 수
'''
우선순위 큐

메모리 제한이 12MB이기 때문에, 큐의 길이를 고정시켜 줘야 함 (push,pop 계속 사용)
'''
import sys,heapq

n=int(sys.stdin.readline().strip())
q=[]
for a in map(int,sys.stdin.readline().split()):
    heapq.heappush(q,a)
# 두번째 입력부터 큐의 길이 고정 유지하면서 push,pop 수행
for _ in range(1,n):
    for a in map(int,sys.stdin.readline().split()):
        heapq.heappush(q,a)
        # pop()은 n*n-n번 수행 됨
        heapq.heappop(q)
# 모든 연산이 수행되고 난 뒤 => n~1번째 큰 수 남아있음
print(heapq.heappop(q))