#구간 곱 구하기
import sys
sys.setrecursionlimit(10 ** 9)

class segTree:
    def __init__(self,n,arr):
        self.tree=[0]*n*4
        self.arr=arr
        # 구간 합 트리 node index는 1부터 해야 편함 (자식노드 계산 시)
        self.init(1,1,n)

    # [left,right] 구간 곱 트리 생성
    def init(self,node,left,right):
        if left==right:
            self.tree[node]=self.arr[left]
        else:
            mid=(left+right)//2
            self.tree[node]=(self.init(node*2,left,mid)*self.init(node*2+1,mid+1,right))%div
        return self.tree[node]

    # [left,right]범위를 줄여가면서 [start,end] 구간 곱 구하기
    def multiple(self,node,left,right,start,end):
        # 범위 밖
        if end<left or right<start:
            return 1
        # 범위 일치
        elif start<=left and right<=end:
            return self.tree[node]
        # 탐색 범위에 걸쳐있는 경우 => 자식 노드로 타고 내려 감
        mid = (left + right) // 2
        return (self.multiple(node*2,left,mid,start,end)*self.multiple(node*2+1,mid+1,right,start,end))%div

    # target 인덱스를 value로 변경
    def update(self,node,left,right,target,value):
        if target<left or target>right:
            return self.tree[node]
        if left==right:
            self.tree[node] = value
            return self.tree[node]
        # 자식노드로 계속 타고 내려가면서 값 변경
        mid=(left+right)//2
        self.tree[node]=(self.update(node*2,left,mid,target,value)*self.update(node*2+1,mid+1,right,target,value))%div
        return self.tree[node]

div=1000000007
n,m,k=map(int,sys.stdin.readline().split())
arr=[0]+[int(sys.stdin.readline().strip()) for _ in range(n)]
f=[list(map(int,sys.stdin.readline().split())) for _ in range(m+k)]
segTree=segTree(n,arr)

for a,b,c in f:
    # b번째 수를 c로 변경
    if a==1:
        segTree.update(1,1,n,b,c)
    # 구간 곱 구하기
    else:
        print(segTree.multiple(1,1,n,b,c))