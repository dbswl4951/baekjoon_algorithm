#같은 수로 만들기
import sys

n = int(sys.stdin.readline().strip())
arr = []
for i in range(n):
    num = int(sys.stdin.readline().strip())
    if i==0 or (i>0 and num!=arr[-1]): arr.append(num)
if n==1:
    print(0)
    sys.exit(0)

result = 0
minVal = min(arr)
minIdx = arr.index(minVal)
while len(arr)>1:
    left,right = float('inf'),float('inf')
    if minIdx>0:
        left = arr[minIdx-1]
    if minIdx<len(arr)-1:
        right = arr[minIdx+1]

    arr.pop(minIdx)
    if left<right:
        goal = left
    elif left>right:
        goal = right
    else:
        goal = left
        arr.pop(minIdx)

    result += goal-minVal
    minVal = min(arr)
    minIdx = arr.index(minVal)
print(result)