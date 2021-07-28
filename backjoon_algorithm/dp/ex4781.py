#사탕 가게
'''
배낭 문제
'''
import sys

while True:
    n,m=map(float,sys.stdin.readline().split())
    n,m=int(n),int(m*100+0.5)
    if n==0 and m==0: break

    # 2차원 배열이 아닌, 1차원 배열로 구현도 가능하다!
    dp =[0]*(m+1)
    for _ in range(n):
        c,p=map(float,sys.stdin.readline().split())
        c,p=int(c),int(p*100+0.5)
        for i in range(p,m+1):
            dp[i]=max(dp[i],c+dp[i-p])
    print(dp[m])