import sys

input = sys.stdin.readline
INF = int(1e9)

t = int(input())

for _ in range(t):
    k, n = map(int, input().split())
    classes = []
    upClass = []
    downClass = []

    for _ in range(4):
        data = list(map(int, input().split()))
        classes.append(sorted(data))

    for i in range(n):
        for j in range(n):
            upClass.append(classes[0][i] + classes[1][j])
            downClass.append(classes[2][i] + classes[3][j])

    upClass.sort()
    downClass.sort(reverse=True)
    print('upClass2:', upClass)
    print('downClass2:', downClass)

    result = INF
    first, second = 0, 0
    length = n * n
    while first < length and second < length:
        total = upClass[first] + downClass[second]
        print('first, second, total : ',first, second,total)

        if abs(result - k) > abs(total - k):
            result = total
        elif abs(result - k) == abs(total - k):
            result = min(result, total)
        print('result:',result)
        if total >= k:
            second += 1
        else:
            first += 1

    print(result)