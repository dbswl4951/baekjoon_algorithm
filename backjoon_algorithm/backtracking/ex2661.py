#좋은 수열
'''
DFS + 백트레킹 문제
1,2,3으로 작은 수부터 n자리수 만들면서, 1~n//2 길이의 수열 체크 (나쁜 수열인지 좋은 수열인지)
'''
import sys

def backtraking(idx):
    # 좋은 순열인지, 나쁜 순열인지 check (현재 자리수=idx의 절반 만큼 반복해서 체크)
    for i in range(1,(idx//2)+1):
        if result[-i:]==result[-i*2:-i]: return -1
    if idx==n:
        return 0
    for i in range(1,4):
        # 1,2,3 중 하나 지정 후 재귀함수 호출
        result.append(i)
        if backtraking(idx+1)==0:
            return 0
        result.pop()

n=int(sys.stdin.readline().strip())
result=[]
backtraking(0)
for r in result:
    print(r,end='')