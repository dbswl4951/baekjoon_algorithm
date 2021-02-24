#우체국
import sys

n=int(sys.stdin.readline().strip())
town=[]
for _ in range(n):
    town.append(list(map(int,sys.stdin.readline().split())))
town.sort(key=lambda x:x[0])
s=0
for t in town:
    s+=t[1]
#평균 값 구하기
s=(s+1)//2
s2=0
#왼쪽->오른쪽으로 이동하면서 확인
for t in town:
    s2+=t[1]
    #왼쪽편 사람들과 오른쪽편 사람들의 인구수가 비슷해지는 곳의 위치 구함 (중간값)
    if s2>=s:
        print(t[0])
        break