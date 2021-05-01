#오큰수
import sys

n=int(sys.stdin.readline().strip())
numbers=list(map(int,sys.stdin.readline().split()))
result,stack=[-1]*n,[]

for idx,num in enumerate(numbers):
    if not stack:
        stack.append(num)
        continue

    top=stack[-1]
    if num>top:
        i=idx
        while stack and stack[-1]<num:
            p=stack.pop()

            while True:
                if result[i - 1] == -1:
                    result[i-1]=num
                    break
                i -= 1
    stack.append(num)
print(*result)