#책 나눠주기
import sys

t=int(sys.stdin.readline().strip())
for _ in range(t):
    n,m=map(int,sys.stdin.readline().split())
    number=[]
    for _ in range(m):
        number.append(list(map(int,sys.stdin.readline().split())))
    number.sort(key=lambda x:x[1])
    book=[0]*(n+1)
    count=0

    for start,end in number:
        for i in range(start,end+1):
            if not book[i]:
                book[i]=1
                count+=1
                break
    print(count)