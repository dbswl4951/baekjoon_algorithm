#커피숍2
import sys

class segTree:
    def __init__(self,arr,n):
        self.arr=arr
        self.tree=[0]*n*4
        self.init(1,1,n)

    # [left,right]범위 구간 합 트리 생성
    def init(self,node,left,right):
        # leaf node
        if left==right:
            self.tree[node]=self.arr[left]
        else:
            mid=(left+right)//2
            self.tree[node]=self.init(node*2,left,mid)+self.init(node*2+1,mid+1,right)
        return self.tree[node]

    # [left,right] 범위를 좁히며, 구하는 범위 합 [start,end] 구하기
    def sum(self,node,left,right,start,end):
        if left>end or right<start:
            return 0
        elif start<=left and end>=right:
            return self.tree[node]
        mid=(left+right)//2
        return self.sum(node*2,left,mid,start,end)+self.sum(node*2+1,mid+1,right,start,end)

    # target번째 수 value로 변경
    def update(self,node,left,right,target,value):
        # 범위 밖
        if target<left or target>right:
            return self.tree[node]
        # leaf node
        if left==right:
            self.tree[node]=value
            return self.tree[node]
        mid = (left + right) // 2
        self.tree[node]=self.update(node*2,left,mid,target,value)+self.update(node*2+1,mid+1,right,target,value)
        return self.tree[node]

n,q=map(int,sys.stdin.readline().split())
arr=[0]+list(map(int,sys.stdin.readline().split()))
segTree=segTree(arr,n)
for _ in range(q):
    x,y,a,b=map(int,sys.stdin.readline().split())
    if x>y: x,y=y,x
    print(segTree.sum(1,1,n,x,y))
    segTree.update(1,1,n,a,b)