#톱니바퀴
'''
1. 톱니 바퀴를 돌리기 전, 맞닿은 곳의 전극이 같은지 / 다른지 확인
 1) 같다면 해당 톱니 바퀴만 회전
 2) 다르다면 해당 톱니 바퀴 회전 + 맞닿은 톱니 바퀴는 반대 방향으로 회전
'''
import sys,copy
from collections import deque

#바퀴 하나 회전
def rotation(tempWheel,num,d):
    if d==1:    #시계 방향 회전
        tempWheel[num]=tempWheel[num][-1]+tempWheel[num][:len(wheel[num])-1]
    else:   #반시계 방향 회전
        tempWheel[num]=tempWheel[num][1:]+tempWheel[num][0]

def start():
    global wheel,tempWheel
    while way:
        num,d=way.popleft()
        if num==1:  #첫 번째 바퀴 회전
            rotation(tempWheel,1, d)
            if wheel[1][2]!=wheel[2][6]:    #전극이 다르면 둘 다 회전
                rotation(tempWheel,2,-d)
                if wheel[2][2]!=wheel[3][6]:    #회전 후, 옆의 바퀴와 전극이 다르다면 옆 바퀴 회전
                    rotation(tempWheel,3,d)
                    if wheel[3][2]!=wheel[4][6]:
                        rotation(tempWheel,4,-d)
        elif num==2:    #두 번 째 바퀴 회전
            rotation(tempWheel,2, d)
            if wheel[2][6]!=wheel[1][2]:
                rotation(tempWheel,1,-d)
            if wheel[2][2]!=wheel[3][6]:
                rotation(tempWheel,3,-d)
                if wheel[3][2]!=wheel[4][6]:
                    rotation(tempWheel,4,d)
        elif num==3:    #세 번째 바퀴 회전
            rotation(tempWheel,3,d)
            if wheel[3][2]!=wheel[4][6]:
                rotation(tempWheel,4,-d)
            if wheel[3][6]!=wheel[2][2]:
                rotation(tempWheel,2,-d)
                if wheel[2][6]!=wheel[1][2]:
                    rotation(tempWheel,1,d)
        else:
            rotation(tempWheel,4,d)
            if wheel[4][6]!=wheel[3][2]:
                rotation(tempWheel,3,-d)
                if wheel[3][6]!=wheel[2][2]:
                    rotation(tempWheel,2,d)
                    if wheel[2][6]!=wheel[1][2]:
                        rotation(tempWheel,1,-d)
        wheel=copy.deepcopy(tempWheel)

wheel=['0']
for _ in range(4):
    wheel.append(sys.stdin.readline().strip())
m=int(sys.stdin.readline().strip())
way=deque()
for _ in range(m):
    way.append(list(map(int,sys.stdin.readline().split())))
tempWheel = copy.deepcopy(wheel)
start()
result=0
for i in range(1,5):
    if wheel[i][0]=='1':
        if i==1: result+=1
        elif i==2: result+=2
        elif i==3: result+=4
        else: result+=8
print(result)
