#트리
'''
트리 구조 사용
'''
import sys

class Node:
    def __init__(self,data):
        self.data=data
        self.child=[]

class Tree:
    def __init__(self):
        self.root=None

    # 노드 삽입
    def insertNode(self,node,data):
        node.child.append(data)

    # 노드 제거
    def removeNode(self):
        # 부모 노드에서 삭제 할 노드 삭제
        nodeDic[arr[removeNode]].child.remove(nodeDic[removeNode])

    # 리프 노드 세기
    def countLeafNode(self,node):
        count=0
        if not node.child: return 1
        for c in node.child:
            # 자식 노드가 있으면, 재귀로 자식 노드 호출
            count+=self.countLeafNode(c)
        return count

n=int(sys.stdin.readline().strip())
arr=list(map(int,sys.stdin.readline().split()))
removeNode=int(sys.stdin.readline().strip())
result=0
tree=Tree()
nodeDic={}      # 노드 정보 저장

for i in range(n): nodeDic[i]=Node(i)

# 트리의 root 정의
tree.root=nodeDic[arr.index(-1)]

# 트리 만들기
for i in range(n):
    if arr[i]!=-1:
        tree.insertNode(nodeDic[arr[i]],nodeDic[i])

# n=1이거나 루트 노드를 삭제하면 0 출력
if n==1 or tree.root.data==removeNode: print(0)
else:
    tree.removeNode()
    result+=tree.countLeafNode(tree.root)
    print(result)