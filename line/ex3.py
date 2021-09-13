'''
- 분류 작업을 마칠 때까지 작업 처리
- 같은 분류의 작업이 새로 요청되면, 새로운 작업도 이어서 처리
- 한 분류의 모든 작업 끝 => 다른 분류 중 중요도 합이 높은 분류 선택 후 처리
    만약 중요도 합이 같은게 여러개 => 분류 번호가 낮은 거 선택 후 처리

처리한 분류 번호를 시간 순대로 return
'''
from collections import deque

def solution(jobs):
    q=deque()
    wating=[[] for _ in range(len(jobs))]
    time,idx=1,0

    while True:
        if jobs[idx][0]==time:
            r,t,num,p = jobs[idx]
            if not q and not wating:
                q.append([t,num,p])
            if q:
                q[0][0]-=1
                if q[0][0]==0:
                    q.popleft()
                    wating[num]