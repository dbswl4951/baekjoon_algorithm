#감소하는 수
import sys

def solve(n):
    cnt,num=0,1
    while True:
        strNum=str(num)
        flag=0
        if len(strNum)!=1:
            for i in range(1,len(strNum)):
                # i번째 숫자가 i-1번째 숫자보다 크거나 같으면, 다른 수 탐색
                if strNum[i]>=strNum[i-1]:
                    start=strNum[:i-1]
                    mid=str(int(strNum[i-1])+1)
                    end='0'+strNum[i+1:]
                    num=int(start+mid+end)
                    flag=1
                    break
        if not flag:
            cnt+=1
            if cnt==n: return num
            num+=1

n=int(sys.stdin.readline().strip())
if n>=1023: print(-1)
elif n==0: print(0)
else: print(solve(n))