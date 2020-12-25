#전화번호 목록
'''
처음엔 하나하나 다 비교해서 풀었음 => 당연히 시간초과
그 다음엔 정렬 후 풀이 => 통과
'''
import sys

t=int(input())
result=[]
for _ in range(t):
    n=int(input())
    number=[]
    r=0
    for _ in range(n):
        number.append(sys.stdin.readline().strip())
    number.sort()
    for i in range(len(number)-1):
        num=number[i]
        if num==number[i+1][:len(num)]:
            r=1
            break
    if r==0:
        result.append("YES")
    else:
        result.append("NO")
for i in result:
    print(i)