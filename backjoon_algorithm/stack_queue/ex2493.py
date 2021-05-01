#탑
'''
1차 시도, 2차 시도 모두 stack을 이용해 풀었지만
1차 시도 때는 index()를 사용해서 시간 초과가 난 것 같다
2차 시도 때는 index() 사용 대신, stack을 2차원 배열로 선언해서 index 값도 같이 저장 함
'''
# 2차 시도
import sys

n=int(sys.stdin.readline().strip())
tower=list(map(int,sys.stdin.readline().split()))
stack=[]
result=[0]*n

for idx,height in enumerate(tower):
    while stack and stack[-1][1]<height:
        stack.pop()

    if stack and stack[-1][1]>height:
        result[idx]=stack[-1][0]+1

    stack.append([idx,height])
print(*result)


# 1차 시도 => 시간 초과
'''
import sys

n=int(sys.stdin.readline().strip())
building=list(map(int,sys.stdin.readline().split()))
stack=[]
result=[0]*n

for idx,height in enumerate(building):
    if not stack:
        stack.append(height)
        continue

    while stack and stack[-1]<height:
        stack.pop()

    if stack and stack[-1]>height:
        result[idx]=building.index(stack[-1])+1
    stack.append(height)
print(*result)
'''