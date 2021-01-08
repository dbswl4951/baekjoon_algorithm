#정수 삼각형
'''
1. 맨 왼쪽 노드, 맨 오른쪽 노드 인덱스 점화식 구함
 왼쪽, 오른쪽 노드는 답이 1개 뿐이므로, dp[i]에 모든 왼쪽 값 더한 값, 모든 오른쪽 값 더한 값을 넣어 줌
2. 맨 왼쪽~맨 오른쪽 노드 사이에 있는 노드들은 부모가 2명이므로,
 dp[i]=max(해당 dp[왼쪽부모], dp[오른쪽부모])+현재 노드 값으로 갱신
3. dp는 누적 합을 담고 있으므로, dp에서 가장 큰 값을 출력

풀이 방법은 바로 떠올랐지만.. 점화식을 구하고 반례를 찾는 것에서 시간이 많이 소요 됐다.
'''
import sys

n=int(sys.stdin.readline().strip())
triangle=[]
for _ in range(n):
    temp=list(map(int,sys.stdin.readline().split()))
    for t in temp:
        triangle.append(t)
dp=[0]*len(triangle)
dp[0]=triangle[0]
leftSeq,rightSeq=[0],[0]
leftIdx,rightIdx=0,0
for i in range(1,n+1):
    leftSeq.append(leftSeq[i-1]+i)
    rightSeq.append(rightSeq[i-1]+i+1)
cnt=0
for i in range(1, len(dp)):
    if i in leftSeq:    #왼쪽 부모
        dp[i]=dp[leftSeq[leftIdx]]+triangle[i]
        leftIdx+=1
        cnt =0
    elif i in rightSeq: #오른쪽 부모
        dp[i]=dp[rightSeq[rightIdx]]+triangle[i]
        rightIdx+=1
    else:   #왼쪽, 오른쪽 부모 중 max값으로 대체
        dp[i]=max(dp[leftSeq[leftIdx-1]+cnt],dp[leftSeq[leftIdx-1]+cnt+1])+triangle[i]
        cnt+=1
print(max(dp))