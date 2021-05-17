#추월
import sys

n=int(sys.stdin.readline().strip())
q=[sys.stdin.readline().strip() for _ in range(n)]
result=0
for i in range(n):
    num=sys.stdin.readline().strip()
    if q[0]!=num:
        result+=1
    q.remove(num)
print(result)