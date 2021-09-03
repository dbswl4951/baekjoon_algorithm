#당근 훔쳐 먹기
'''
w<=p조건이기 때문에 항상 t-n일까지 기다리다 작은 맛부터 먹는게 이득
'''
import sys

n,t = map(int,sys.stdin.readline().split())
carrot = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
carrot.sort(key=lambda x:x[1])
result,day=0,t-n
for w,p in carrot:
    result+=w+p*day
    day+=1
print(result)