#좋은 친구
import sys

n,k=map(int,sys.stdin.readline().split())
studentLen=[0]*n   # 학생 이름 길이 저장
lenCount=[0]*21     # 학생 이름의 길이 개수 저장
result=0

for rank in range(n):
    sLen=len(sys.stdin.readline().strip())
    studentLen[rank]=sLen
    if rank>k:
        lenCount[studentLen[rank-k-1]]-=1
    result+=lenCount[sLen]
    lenCount[sLen]+=1
print(result)