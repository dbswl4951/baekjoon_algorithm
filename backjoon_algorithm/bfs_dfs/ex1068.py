#트리
'''
dfs 사용

1. 부모 노드를 저장 한 리스트(nodes)에 삭제 할 노드 -2로 변경
2. 삭제 한 노드를 부모로 가지고 있는 노드를 조사하기 위해 for문 사용
    => 삭제 한 노드를 부모 노드로 가지고 있다면, dfs 재귀 호출 후 (1) 실행
'''
import sys

def dfs(removeNode,nodes):
    # 삭제 할 노드 -2로 변경
    nodes[removeNode]=-2
    for i in range(n):
        # 삭제 한 노드를 부모 노드로 가지고 있는 노드 재귀 호출
        if removeNode==nodes[i]:
            dfs(i,nodes)

n=int(sys.stdin.readline().strip())
nodes=list(map(int,sys.stdin.readline().split()))
removeNode=int(sys.stdin.readline().strip())

dfs(removeNode,nodes)
reuslt=0
for i in range(n):
    # 삭제 한 노드가 아니고, 부모 노드가 아닌 노드 개수 세기
    if nodes[i]!=-2 and i not in nodes: reuslt+=1
print(reuslt)