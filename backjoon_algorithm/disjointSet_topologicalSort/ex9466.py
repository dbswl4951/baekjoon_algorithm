#텀 프로젝트
'''
팀을 구성하기 위해선 : 마지막 학생은 첫 학생을 지목해야 한다
=> 처음과 끝이 이어진 순환 사이클이 되야 함

DFS를 활용 해 사이클 여부 판단
사이클에 포함 되지 않는 학생 수 구하기
'''
import sys
sys.setrecursionlimit(111111)

def dfs(x):
    global result
    visited[x]=1
    cycle.append(x)
    select=students[x]  # select : x가 선택한 학생
    if visited[select]:
        # 사이클을 이루고 있다면
        if select in cycle:
            # x가 지목한 학생(select)부터 팀 구성
            result+=cycle[cycle.index(select):]
        return
    else:
        dfs(select)

t=int(sys.stdin.readline().strip())
for _ in range(t):
    n=int(sys.stdin.readline().strip())
    students=[0]+list(map(int,sys.stdin.readline().split()))
    visited=[0]*(n+1)
    result=[]
    for i in range(1,n+1):
        if not visited[i]:
            cycle=[]
            dfs(i)
    print(n-len(result))