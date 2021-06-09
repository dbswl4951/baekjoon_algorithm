#최솟값
import sys

class SegTree:
    def __init__(self,n,numbers):
        self.tree=[0]*4*n
        self.numbers=numbers
        self.init(1,0,n-1)    # (node,left,right)

    # [left,right) 범위 내 최솟값 트리 생성
    def init(self,node,left,right):
        # leaf node
        if left==right:
            self.tree[node]=self.numbers[left]
        else:
            mid=(left+right)//2
            self.tree[node]=min(self.init(node*2,left,mid),self.init(node*2+1,mid+1,right))
        return self.tree[node]

    # 최솟값 구하기
    def search(self,node,left,right,start,end):
        # 탐색 범위에 현재 인덱스들이 포함되는 경우
        if start<=left and right<=end:
            return self.tree[node]
        # 범위에 포함 되지 않는 경우
        elif right<start or end<left:
            return float('inf')
        # 탐색 범위에 걸쳐있는 경우 => 자식 노드로 타고 내려 감
        mid=(left+right)//2
        return min(self.search(node*2,left,mid,start,end),self.search(node*2+1,mid+1,right,start,end))

n,m=map(int,sys.stdin.readline().split())
numbers=[int(sys.stdin.readline().strip()) for _ in range(n)]
lines=[list(map(int,sys.stdin.readline().split())) for _ in range(m)]
tree=SegTree(n,numbers)
for start,end in lines:
    print(tree.search(1,0,n-1,start-1,end-1))


#1차 시도 => 시간 초과
'''
import sys,heapq

n,m=map(int,sys.stdin.readline().split())
numbers=[int(sys.stdin.readline().strip()) for _ in range(n)]
lines=[list(map(int,sys.stdin.readline().split())) for _ in range(m)]
for li in lines:
    q=[]
    for i in range(li[0]-1,li[1]):
        heapq.heappush(q,numbers[i])
    print(heapq.heappop(q))
'''