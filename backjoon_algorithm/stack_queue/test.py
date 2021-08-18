import sys
input=sys.stdin.readline
mii=lambda:map(int,input().split())
print("mii:",mii)

n=int(input())

li=[]
q=[]

for _ in range(n):
    for person in input().split():
        a,b=person.split("-")
        li.append((a,int(b)))
        print("li:",li)

want=sorted(li)
li=li[::-1]
print("want:",want)
print("li:",li)