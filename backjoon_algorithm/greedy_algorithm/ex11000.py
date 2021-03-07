#강의실 배정
'''
[ Point ]
강의 끝나는 시간으로 정렬 하는 것이 아니라, 강의 시작 시간으로 정렬!
강의 시작 시간과 큐에 있는 강의 종료 시간 비교
O(nlogn)
'''
import sys,heapq

n=int(sys.stdin.readline().strip())
subjects=[]
for _ in range(n):
    subjects.append(list(map(int,sys.stdin.readline().split())))
#강의 시작 시간으로 정렬
subjects.sort(key=lambda x:x[0])
q=[]
heapq.heappush(q,subjects[0][1])
for i in range(1,n):
    #가장 빨리 끝나는 강의 시간이 현재 강의 시작 시간보다 뒤라면, 강의실 수 +1
    if q[0]>subjects[i][0]:
        heapq.heappush(q,subjects[i][1])
    else:
        heapq.heappop(q)
        heapq.heappush(q,subjects[i][1])
print(len(q))