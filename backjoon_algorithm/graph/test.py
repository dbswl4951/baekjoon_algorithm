import sys
from queue import Queue




def solution(x, n, love):
    q = Queue()
    q.put([x, love])

    while not q.empty():
        head = q.get()
        headNode = head[0]
        headLove = head[1]

        visit[headNode] = x

        for loveItem in headLove:
            if not visit[loveItem]:
                visit[loveItem] = x
                temp = []

                for i in range(1, n + 1):
                    if arr[loveItem][i] == 0:
                        temp.append(i)
                if headLove != temp:
                    return False
                q.put([loveItem, temp])

    return True


if __name__ == "__main__":
    cnt = 0
    n = int(input())
    arr = [[0 for col in range(n + 1)] for row in range(n + 1)]
    visit = [0 for col in range(n+1)]
    ans = []

    for i in range(1, n + 1):
        num = list(map(int, input().split()))
        for j in range(0, len(num)):
            arr[i][j + 1] = num[j]
    print('arr :',arr)

    for i in range(1, n + 1):
        if visit[i] == 0:
            love = []
            for j in range(1, n + 1):
                if arr[i][j] == 0:
                    love.append(j)
            print('love :',love)
            if len(love) == 1:
                print(0)
                sys.exit()
            check = solution(i, n, love)
            if not check:
                print(0)
                sys.exit()
            else:
                ans.append(love)
                cnt += 1

    print(cnt)
    for ansItem in ans:
        for num in ansItem:
            print(num, end=' ')
        print()