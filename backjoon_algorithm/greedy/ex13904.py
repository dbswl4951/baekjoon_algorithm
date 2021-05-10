#과제
import sys

n=int(sys.stdin.readline().strip())
homework=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
homework.sort(key=lambda x:(-x[1],x[0]))
day=[]
result=0
for d,s in homework:
    while d>0:
        if d not in day:
            day.append(d)
            result+=s
            break
        d-=1
print(result)