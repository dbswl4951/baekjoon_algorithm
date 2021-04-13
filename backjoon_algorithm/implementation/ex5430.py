#AC
import sys
from collections import deque

t=int(sys.stdin.readline().strip())
for _ in range(t):
    function=list(sys.stdin.readline().strip())
    n=int(sys.stdin.readline().strip())
    arr=sys.stdin.readline().strip()
    cnt,flag=0,0
    if arr=='[]':
        if 'D' in function:
            print('error')
        else:
            print('[]')
    else:
        q=deque(arr[1:len(arr)-1].split(','))
        for f in function:
            if f == 'R':
                cnt += 1
            elif f=='D' and len(q)>0:
                if cnt % 2 == 0:
                    q.popleft()
                else:
                    q.pop()
            else:
                print('error')
                flag=1
                break
        if not flag:
            result=[]
            print('[',end='')
            if cnt % 2 == 1:
                for i in range(len(q)-1,-1,-1):
                    if i ==0:
                        print(int(q[i]), end='')
                    else:
                        print(int(q[i]), end=',')
            else:
                for i in range(len(q)):
                    if i==len(q)-1: print(int(q[i]),end='')
                    else: print(int(q[i]),end=',')
            print(']')
