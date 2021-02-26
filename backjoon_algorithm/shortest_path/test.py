import sys
from collections import deque

if __name__ == '__main__':
    N, K = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))

    ans = sys.maxsize
    left, right = 0, 0
    cnt = 0
    q = deque()
    for start in range(N):
        print(start,"======")
        while right < N and cnt < K:
            q.append(arr[right])
            if arr[right] == 1: cnt += 1
            right += 1
            print(q)
            print("left,right::",left,right)
        if cnt == K:
            ans = min(len(q), ans)
            if arr[left] == 1: cnt -= 1
            left += 1
            q.popleft()
        print("ans::",ans)
    print(ans if ans != sys.maxsize else -1)