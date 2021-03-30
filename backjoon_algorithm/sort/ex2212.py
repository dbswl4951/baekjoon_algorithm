#센서
'''
1. sensor를 오름차순 정렬
2. 만약 기지국의 수가 센서의 수보다 많거나 같으면 거리는 0
3. sensor[i]-sensor[i-1]의 값을 구해서 가장 큰 값을 기준으로 k-1번 잘라 리스트 분할

아이디어가 떠오르기 까지 시간이 꽤 걸렸다.
max()랑 remove() 때문에 시간초과 나올 거라고 예상 했는데 파이썬으로 바로 통과가 됐다.
'''
import sys

n=int(input())
k=int(input())
sensor=list(map(int,sys.stdin.readline().split()))
sensor.sort()
result=0
dis=[]

if k<n:
    for i in range(1,n):
        dis.append(sensor[i]-sensor[i-1])   #거리 저장
    for i in range(k-1):
        dis.remove(max(dis))
    result=sum(dis)
print(result)