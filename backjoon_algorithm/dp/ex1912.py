#연속합
import sys

#다른 사람의 DP 풀이
#자기 자신, 자신과 자신 앞의 수를 더했을 때의 수 중에서 더 큰 수를 dp에 저장
n=int(sys.stdin.readline().strip())
numbers=list(map(int,sys.stdin.readline().split()))
dp=[0]*n
dp[0]=numbers[0]
for i in range(1,n):
    dp[i]=max(numbers[i],numbers[i]+dp[i-1])
print(max(dp))


#내 풀이
'''
n=int(sys.stdin.readline().strip())
numbers=list(map(int,sys.stdin.readline().split()))
dp=[]
if max(numbers)>=0:
    val=0
    for i in numbers:
        val+=i
        if val<0:
            val=0
        else:
            dp.append(val)
    print(max(dp))
else:
    print(max(numbers))
'''