#음료수 얼려 먹기
'''
dfs(깊이 탐색)사용
1. 특정 지점의 상,하,좌,우를 살펴 본 다음 주변 지점 중에서 값이 '0'이면서
아직 방문하지 않은 지점이 있다면 해당 지점 방문
2. 방문한 지점에서 다시 상,하,좌,우를 보면서 방문 과정 반복
=> 연결된 모든 지점을 방문 하게 됨
3. 모든 노드에 대해 1~2 과정 반복 후, 방문하지 않은 지점의 수를 카운트 함
'''

n,m=map(int,input().split()) #가로,세로
frame=[]
for i in range(n):
    frame.append(list(map(int,input())))

def dfs(x,y):
    if x>=n or x<=-1 or y<=-1 or y>=m:
        return False
    if frame[x][y]==0:
        frame[x][y]=1   #해당 좌표 방문 처리
        #상,하,좌,우 위치들을 모두 재귀적으로 호출
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

result=0
#모든 위치에 대해 수행
for i in range(n):
    for j in range(m):
        #현재 위치에서 dfs 실행
        if dfs(i,j)==True:
            result+=1 
print(result)
