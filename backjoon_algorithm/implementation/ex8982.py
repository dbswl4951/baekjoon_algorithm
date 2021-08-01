#수족관 1
import sys

n=(int(sys.stdin.readline().strip())-2)//2    # 수평선분의 개수
sectorNum=dict()
top=[0]*n # 물이 남아있을 수 있는 높이
depth=[0]*n # 수족관 깊이
width=[0]*n

# (0,0)은 건너뛴다
sys.stdin.readline()
# 수평선분 기준으로 입력 받기
for i in range(n):
    sx=int(sys.stdin.readline().split()[0]) # 수평선분 시작 x좌표
    ex,ey=map(int, sys.stdin.readline().split())    # 수평선분 끝 x좌표, 끝 y좌표
    # 시작x ~ 끝x 수평선분에 순서 지정
    sectorNum[(sx,ex)]=i
    depth[i]=ey
    width[i]=ex-sx
sys.stdin.readline()

k=int(sys.stdin.readline())
for i in range(k):
    sx,surface,ex,ey=map(int, sys.stdin.readline().split())
    # 구멍이 몇 번째 수평분선에 있는지
    num=sectorNum[(sx,ex)]

    # 구멍 기준 왼쪽 수평분선부터 검사
    for i in range(num,-1,-1):
        # surface : 수면의 높이
        surface=min(surface,depth[i])
        # 수면의 높이와 현재 물의 높이 중 최대 값으로 갱신 (y의 최대값 = 깊이가 깊은것)
        top[i]=max(surface,top[i])

    # 왼쪽과 다시 비교하기 위해서 원상태로
    surface=depth[num]
    # 구멍 기준 오른쪽 수평분선 검사
    for i in range(num+1,n):
        surface=min(surface,depth[i])
        top[i] = max(surface, top[i])

result=0
# 남아있는 물의 양 구하기
for i in range(n):
    result+=width[i]*(depth[i]-top[i])
print(result)