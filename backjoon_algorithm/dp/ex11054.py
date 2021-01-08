#가장 긴 바이토닉 부분 수열
'''
DP사용한 LIS 문제
1. 왼쪽에서 최대 증가 수열 dp 만들고
2. 오른쪽에서 최대 증가 수열 dp 만들고
3. 둘이 합치고 1 빼기

코드는 90% 유사했지만.. 반례때문에 시간을 많이 잡아먹어서 다른 사람 풀이 찾아 봄
=> rightDp.reverse() 해줬어야 함!!!
'''
import sys

def getLIS(dp):
    for i in range(n):
        for j in range(i):
            if numbers[i] > numbers[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp

n=int(sys.stdin.readline().strip())
numbers=list(map(int,sys.stdin.readline().split()))
leftDp,rightDp=[1]*n,[1]*n
leftDp=getLIS(leftDp)
numbers.reverse()
rightDp=getLIS(rightDp)
rightDp.reverse()
dp = [leftDp[i] + rightDp[i] for i in range(n)]
print(max(dp) - 1)


'''
def getLIS(numbers,n):
    dp=[1]*n
    #print("numbers,n,dp===",numbers,n,dp)
    for i in range(1, n):
        for j in range(i):
            #print("i,j:::", i,j)
            if numbers[i] > numbers[j]:
                dp[i] = max(dp[i], dp[j] + 1)
        #print("dp:::",dp)
    return max(dp),dp.index(max(dp))

n=int(sys.stdin.readline().strip())
numbers=list(map(int,sys.stdin.readline().split()))
#(1) 경우
count1,idx1=getLIS(numbers,n)
reverseNumbers=list(reversed(numbers))
count2,idx2=getLIS(reverseNumbers,n-idx1)
result1=count1+count2-1
#(2) 경우
count1,idx1=getLIS(reverseNumbers,n)
count2,idx2=getLIS(numbers,n-idx1)
result2=count1+count2-1

print(max(result1,result2))
'''