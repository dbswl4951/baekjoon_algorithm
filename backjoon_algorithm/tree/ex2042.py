#구간 합 구하기
'''
세그먼트 트리 사용

숫자 배열 인덱스는 0부터 시작, 구간합 트리 (segTree)는 인덱스 1부터 시작함!
    => 현재 인덱스*2 = 왼쪽 자식노드로 만들기 위해서
'''
import sys

class SegTree:
    # 구간합 tree 배열 선언, init() 호출로 구간 합 트리 생성
    def __init__(self,n,arr):
        self.arr=arr
        self.tree=[0]*4*n
        # 구간 합 트리 생성
        self.init(1,0,n)

    # 구간 합 트리 만들기
    def init(self,node,left,right):
        # node가 leaf 노드일 때, tree[node] 값 저장
        if left+1==right:
            self.tree[node]=self.arr[left]
        # leaf node가 아닌 경우, 데이터를 반씩 분할하며 재귀함수 호출
        else:
            mid=(left+right)//2
            self.tree[node]=self.init(node*2,left,mid)+self.init(node*2+1,mid,right)
        return self.tree[node]

    # start~end까지의 구간 합 구하기
    def sum(self,node,left,right,start,end):
        # 현재 노드 범위 (left~right)가 구할 구간 합 범위에 완전히 포함되는 경우 (start~end)
        if start<=left and right<=end:
            return self.tree[node]
        # 아예 포함되지 않는 경우 (고려 X)
        if right<=start or end<=left:
            return 0

        # 현재 노드범위, 구할 구간 합 범위가 부분만 일치 하는 경우 => 2가지 범위로 나눠서 재귀 호출로 합 구하기
        mid=(left+right)//2
        return self.sum(node*2,left,mid,start,end)+self.sum(node*2+1,mid,right,start,end)

    # target번째를 value만큼 변경
    def update(self,node,left,right,target,value):
        if left<=target<right:
            self.tree[node]+=value
            # leaf node까지 내려온 경우 끝
            if left+1==right: return

            # 자식 노드로 계속 타고 내려가면서 구간 합 값 변경
            mid=(left+right)//2
            self.update(node*2,left,mid,target,value)
            self.update(node*2+1,mid,right,target,value)

n,m,k=map(int,sys.stdin.readline().split())
arr=[int(sys.stdin.readline().strip()) for _ in range(n)]
f=[list(map(int,sys.stdin.readline().split())) for _ in range(m+k)]

tree=SegTree(n,arr)
for a,b,c in f:
    b-=1
    # 수 변경
    if a==1:
        tree.update(1,0,n,b,c-tree.arr[b])
        tree.arr[b]=c
    # 구간 합 구하기
    else:
        print(tree.sum(1,0,n,b,c))