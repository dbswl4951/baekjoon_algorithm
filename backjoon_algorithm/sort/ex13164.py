#행복 유치원
import sys

n,k = map(int,sys.stdin.readline().split())
height = list(map(int,sys.stdin.readline().split()))
diff=[]
for i in range(n-1):
    diff.append(height[i+1]-height[i])
diff.sort()
result=0
# 조로 만들 n-k개의 키 차이 더하기
# diff 뒤에 있는 애들은 키 차이가 크기 때문에 선택되지 않음 => 따로 조 편성 (무시)
for i in range(n-k):
    result+=diff[i]
print(result)