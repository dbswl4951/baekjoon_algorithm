#내려가기
import sys,copy

n=int(sys.stdin.readline().strip())
arr=list(map(int,sys.stdin.readline().split()))
minArr,maxArr=copy.deepcopy(arr),copy.deepcopy(arr)

for i in range(1,n):
    temp=list(map(int,sys.stdin.readline().split()))
    minArr=[temp[0]+min(minArr[0],minArr[1]),temp[1]+min(minArr[0],minArr[1],minArr[2]),temp[2]+min(minArr[1],minArr[2])]
    maxArr=[temp[0]+max(maxArr[0],maxArr[1]),temp[1]+max(maxArr[0],maxArr[1],maxArr[2]),temp[2]+max(maxArr[1],maxArr[2])]
print(max(maxArr),min(minArr))