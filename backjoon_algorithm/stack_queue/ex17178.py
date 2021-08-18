#줄서기
import sys
from collections import deque

n=int(sys.stdin.readline().strip())
arr,order,orderAlpa=deque(),dict(),[]
waiting=deque()
for _ in range(n):
    temp=sys.stdin.readline().split()
    for t in temp:
        arr.append(t)
        alpa,num=t.split('-')
        if alpa in order:
            order[alpa].append(int(num))
            order[alpa].sort()
        else:
            order[alpa]=[int(num)]
        orderAlpa.append(alpa)
orderAlpa.sort(reverse=True)

rowIdx,idx=0,0
while orderAlpa:
    alpa=orderAlpa.pop()
    num=order[alpa][0]
    # 해당 순서가 아니면 대기실로 이동
    while arr or waiting:
        if waiting and waiting[-1] == alpa + '-' + str(num):
            waiting.pop()
            break
        elif arr:
            tiket = arr.popleft()
            if tiket!=alpa+'-'+str(num):
                waiting.append(tiket)
            else: break
        else: break
    del order[alpa][0]

if not arr and not waiting: print('GOOD')
else: print('BAD')