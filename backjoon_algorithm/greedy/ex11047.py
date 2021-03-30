#동전 0
'''
1차 시도 : while + k값에서 coin 빼줌 => 시간 초과
2차 시도 : while문 제거(for문으로만 풀이 가능) + k//coin 사용
 for문으로 가장 큰 coin부터 검사 & k//coin(몫)값을 num에 더해주며 갱신
'''
import sys

n,k=map(int,sys.stdin.readline().split())
coin=[]
for _ in range(n):
    coin.append(int(sys.stdin.readline().strip()))
num=0
for i in range(n-1,-1,-1):
    if k==0:
        break
    if coin[i]>k:
        continue
    num+=k//coin[i]
    k-=(k//coin[i])*coin[i]
print(num)