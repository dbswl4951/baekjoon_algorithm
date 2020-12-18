#왕실의 나이트

location = input()
x=int(location[1])
y=ord(location[0])-96     #a=1,b=2...로 변환
#말을 움직일 수 있는 방법 : 8가지
move=[[-1,-2],[1,-2],[-2,-1],[-2,1],[-1,2],[1,2],[2,-1],[2,1]]
count=0

for m in move:
    if 1<=x+m[0]<=8 and 1<=y+m[1]<=8:
        count+=1
print(count)