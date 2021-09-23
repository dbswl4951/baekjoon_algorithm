#연산자 끼워넣기 (3)
import sys

def dfs(string,idx,operation):
    global maxVal,minVal

    if sum(operation)==0:
        value = eval(string)
        maxVal = max(maxVal,value)
        minVal = min(minVal,value)
        return

    for i in range(4):
        if operation[i]:
            operation[i] -= 1
            if i==0:
                dfs(string+'+'+arr[idx],idx+1,operation)
            elif i==1:
                dfs(string+'-'+arr[idx], idx + 1, operation)
            elif i==2:
                dfs(string+'*'+arr[idx], idx + 1, operation)
            else:
                dfs(string+'//'+arr[idx], idx + 1, operation)
            operation[i] += 1

n = int(sys.stdin.readline().strip())
arr = list(sys.stdin.readline().split())
oper = list(map(int,sys.stdin.readline().split()))
maxVal,minVal = -float('inf'), float('inf')

for i in range(4):
    if oper[i]:
        oper[i] -= 1
        if i==0:
            dfs(arr[0]+'+'+arr[1],2,oper)
        elif i==1:
            dfs(arr[0]+'-'+arr[1],2,oper)
        elif i==2:
            dfs(arr[0]+'*'+arr[1],2,oper)
        elif i==3:
            dfs(arr[0]+'//'+arr[1],2,oper)
        oper[i] += 1
print(maxVal)
print(minVal)