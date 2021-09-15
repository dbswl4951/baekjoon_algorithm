#제곱수 찾기
'''
id, jd 범위가 왜 -n+1, -m+1부터 시작하면 틀리는지 의문
nXm의 배열 끝 원소는 (n-1,m-1)이고 (n-1)+(-n+1)=0이니까 0부터 시작하게 하면 되는것 아닌가?

** 좀 더 생각해보기
'''
import sys,math

n,m = map(int,sys.stdin.readline().split())
board = [list(map(int,sys.stdin.readline().strip())) for _ in range(n)]
result = -1

# 1. 등차를 시작할 좌표 (i,j) 선택
for i in range(n):
    for j in range(m):
        # 2. (i,j)의 등차 id, jd 선택
        for id in range(-n,n):
            for jd in range(-m,m):
                if id==0 and jd==0: continue
                string=''
                # (i,j) 좌표부터 등차 시작
                x,y = i,j

                # 3. 범위안에서 계속 등차를 더하며 해당 수를 붙여줌
                while 0<=x<n and 0<=y<m:
                    string+=str(board[x][y])
                    val = math.sqrt(int(string))
                    # 4. 만약 제곱수이면 result값을 최대값으로 갱신
                    if val-int(val)==0:
                        result=max(result,int(val)**2)

                    # 5. 등차만큼 이동
                    x+=id
                    y+=jd
print(result)