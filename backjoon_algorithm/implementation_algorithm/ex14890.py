#경사로
import sys

# 지나 갈 수 있는 길인지 검사
def check(b):
    # 경사로 놓였으면 1, 아니면 0
    ch=[0 for _ in range(n)]
    for i in range(n-1):
        if abs(b[i]-b[i+1])>1:
            return False
        if b[i]==b[i+1]:
            continue

        # 내리막길 경사로
        if b[i]>b[i+1]:
            temp=b[i+1]
            for j in range(i+1,i+1+l):
                if 0<=j<n:
                    # 경사로를 설치 할 길이 같은 높이가 아닐 경우
                    if b[j]!=temp: return False
                    # 이미 경사로 설치 한 경우
                    if ch[j]==1: return False
                    # 경사로 설치
                    ch[j]=1
                else: return False
        # 오르막길 경사로
        else:
            temp=b[i]
            for j in range(i,i-l,-1):
                if 0 <= j < n:
                    # 경사로를 설치 할 길이 같은 높이가 아닐 경우
                    if b[j] != temp: return False
                    # 이미 경사로 설치 한 경우
                    if ch[j] == 1: return False
                    # 경사로 설치
                    ch[j] = 1
                else:
                    return False
    return True

n,l=map(int,sys.stdin.readline().split())
board=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
result=0
for b in board:
    if check(b): result+=1
for b in list(map(list,zip(*board))):
    if check(b): result+=1
print(result)