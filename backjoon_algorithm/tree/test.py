import sys
import math
input = sys.stdin.readline

def createSegmentTree(start, end, node, arr, tree):
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    mid = (start+end)//2
    tree[node] = createSegmentTree(start, mid, node * 2, arr, tree) + createSegmentTree(mid+1, end, node*2+1, arr, tree)
    return tree[node]

def calcIntervalSum(start, end, left, right, node, tree):
    if start > right or end < left:
        return 0
    elif start >= left and end <= right:
        return tree[node]
    else:
        mid = (start+end)//2
        return calcIntervalSum(start, mid, left, right, node*2, tree) + calcIntervalSum(mid+1, end, left, right, node*2+1, tree)

def changeValue(start, end, node, idx, dis, tree):
    if idx < start or idx > end:
        return
    mid = (start+end)//2

    tree[node] += dis
    if start != end:
        changeValue(start, mid, node*2, idx, dis, tree)
        changeValue(mid+1, end, node*2 + 1, idx, dis, tree)

if __name__ == "__main__":
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    high = math.ceil(math.log2(n))
    size = 2 ** (high + 1)
    tree = [0] * size
    createSegmentTree(0, n-1, 1, arr, tree)

    for _ in range(q):
        x, y, changeNode, changeVal = map(int, input().split())
        if x > y:
            x, y = y, x
        ans = calcIntervalSum(0, n-1, x-1, y-1, 1, tree)
        print(ans)
        dis = changeVal - arr[changeNode-1]
        arr[changeNode-1] += dis
        changeValue(0, n-1, 1, changeNode-1, dis, tree)