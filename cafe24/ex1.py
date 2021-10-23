def solution(n):
    dp = [0]*1002
    dp[1],dp[2] = 1,3
    d = 2

    for i in range(3,1002):
        d += 4
        dp[i] = dp[i-1]+d
    result = (dp[n+1]-2)+(dp[n+1]-4)+(dp[n+1]-6)

    return result

print(solution(5))