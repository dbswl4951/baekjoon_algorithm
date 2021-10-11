#카드 섞기
'''
종료 조건이 중요. 종료 조건을 잘못 생각하면 시간초과 나는 문제였음.

[ 종료 조건 ]
계속 섞다보면 사이클이 형성 됨
처음 배열과 카드 섞은 뒤의 배열이 같다면 종료
'''
import sys,copy

n = int(sys.stdin.readline().strip())
p = list(map(int,sys.stdin.readline().split()))
origin = copy.deepcopy(p)
s = list(map(int,sys.stdin.readline().split()))
goal = [0,1,2] * (n//3)
result,flag = 0,0

while p!=goal:
    mix = [0] * n
    for i in range(n):
        mix[s[i]] = p[i]
    result += 1
    # 여기선 copy()를 사용하지 않아도 됨 (copy 사용 시, 시간이 4배 정도 더 걸림)
    p = mix

    # 맨 처음 카드 순서와 섞은 뒤의 순서가 같다면 종료
    if p==origin:
        result = -1
        break
print(result)