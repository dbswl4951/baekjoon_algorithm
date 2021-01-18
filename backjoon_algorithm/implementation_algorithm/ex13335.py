#트럭
import sys
from collections import deque

n,w,l = map(int,sys.stdin.readline().split())   #트럭 수, 다리 길이, 다리의 최대 하중
truck=deque(map(int,sys.stdin.readline().split()))
bridge=[]  #다리를 건너고 있는 트럭들 저장
weight,time=truck[0],1 #다리를 건너는 트럭들 무게 합,시간
bridge.append((truck.popleft(),1,1+w))
while truck:
    time += 1
    temp=0
    for b in bridge:
        x,y,z=b
        if time==z:
            bridge.pop(0)
    for i in range(len(bridge)):
        temp+=bridge[i][0]
    if temp+truck[0]<=l:
        bridge.append((truck.popleft(),time,time+w))  #(트럭무게, 시작시간, 도착시간)
print(bridge[-1][2])