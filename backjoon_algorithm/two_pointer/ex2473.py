#세 용액
'''
1. 오름차순 정렬
2. i는 고정 시킨 후 투 포인터 사용(left,right)
'''
import sys

n=int(input())
solution=list(map(int,sys.stdin.readline().split()))
solution.sort()
val=float('inf')
idx=[0]*3

for i in range(n-2):
    if i>0 and solution[i]==solution[i-1]:
        continue

    left,right=i+1,n-1
    while left<right:
        sum = solution[i]+solution[left]+solution[right]
        if abs(sum)<abs(val):
            idx[0]=solution[i]
            idx[1] = solution[left]
            idx[2] = solution[right]
            val=sum
        if sum>0:
            right-=1
        elif sum<0:
            left+=1
        else:
            print(solution[i],solution[left],solution[right])
            sys.exit(0)

for i in idx:
    print(i,end=' ')