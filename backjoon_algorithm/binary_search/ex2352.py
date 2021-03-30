#반도체 설계
'''
<LIS(Longest increasing Subsequence)> 문제
:최장 증가 수열

1. O(n2)인 DP 이용
 dp[i] = i보다 앞에 있는 작은 수 중 가장 긴 dp[j]+1
    ex) 5 1 4 2 7 6 3 9 2의 가장 긴 LIS는 1 2 3 9
    5에선 5가 가장 길고 [1]
    1에선 1이 가장 길고 [1 1]
    4에선 1이 자기보다 작으니 1 4 이렇게 붙일 수 있고 [1 1 2]
    2에선 1이 자기보다 작으니 1 2 이렇게 붙일수 있고 [1 1 2 2]
    7에선 4와 2가 자기보다 작으니 1 2 7, 1 4 7[1 1 2 2 3]...
    =>O(N^2)
2. O(nlgn)인 이진탐색 이용
 1) 현재 만든 시퀀스에서 크거나 같은 가장 작은 수를 찾아주고 그 위치에 해당 수로 바꿈
 2) 만약 그러한 수가 없다면 가장 뒤에 추가
    ex)1회에서 가장 처음에 아무수도 없으니 5가 LIS에 추가 [5]
    2회에선 1보다 크거나 같은수는 5니까 5를 1로 바꿈 [1]
    3회에선 4보다 크거나 같은 수가 없으니 가장 뒤에 붙임 [1 4]
    4회에선 4를 2로 대체가능하니 바꿈 [1 2]
    5회에선 7보다 크거나 같은수가 없으니 7을 뒤에 붙임 [1 2 7]...

참고:https://m.blog.naver.com/PostView.nhn?blogId=jh20s&logNo=221310955726&proxyReferer=https:%2F%2Fwww.google.com%2F

<bisect 함수>
bisect(a, x) == bisect_right(a, x)
'''
from bisect import bisect
import sys

n=int(sys.stdin.readline().strip())
port=list(map(int,sys.stdin.readline().split()))
dpLIS=[port[0]]
for i in range(1,n):
    if dpLIS[-1]<port[i]:   #만약 dpLIS에 있는 최댓값보다 큰 값이 오면 뒤에 붙여 줌
        dpLIS.append(port[i])
    else:   #아니라면 bisect(a,x)함수 사용 => 최솟값으로 대체
        #print(bisect(dpLIS,port[i]))
        dpLIS[bisect(dpLIS,port[i])]=port[i]    #연결 할 포트 번호 삽입
    #print(dpLIS)
print(len(dpLIS))