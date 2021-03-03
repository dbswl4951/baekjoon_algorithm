#내려가기
'''
메모리 제한 : 4MB이기 때문에 n크기에 비례해 리스트를 생성하면 메모리 초과
따라서 1X3 리스트 2개 (minDP,maxDP)만들고 계속 갱신 해줘야 함
'''
import sys

n=int(sys.stdin.readline().strip())
board=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
minDP=board[0]
maxDP=board[0]
for i in range(1,n):
    minDP=[min(minDP[0],minDP[1])+board[i][0],
           min(minDP[0],minDP[1],minDP[2])+board[i][1],
           min(minDP[1],minDP[2])+board[i][2]]
    maxDP=[max(maxDP[0],maxDP[1])+board[i][0],
           max(maxDP[0],maxDP[1],maxDP[2])+board[i][1],
           max(maxDP[1],maxDP[2])+board[i][2]]
print(max(maxDP),min(minDP))