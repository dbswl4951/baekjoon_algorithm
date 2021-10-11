import sys
N=sys.stdin.readline().strip()
arr=list(map(int,sys.stdin.readline().strip().split()))
one={arr[0]:1}
two={arr[0]*2:1}
answer=0
for n in arr[1:]:
    print('n === ',n)
    for i in one:
        if n-i in two:
            answer+=1
            break
    if n not in one:
        one[n]=1

    for i in one:
        if i+n not in two:
            two[i+n]=1
    print('one:',one)
    print('two:',two)
print(answer)