import sys

n = (int(input()) - 2) // 2
sector_no = dict()
top = [0] * n
bottom = [0] * n
width = [0] * n
sys.stdin.readline()
for i in range(n):
    start = int(sys.stdin.readline().split()[0])
    end, bot = map(int, sys.stdin.readline().split())
    sector_no[(start, end)] = i
    bottom[i] = bot
    width[i] = end - start
sys.stdin.readline()

k = int(sys.stdin.readline())
holes = [0] * k
for i in range(k):
    start, surface, end, temp2 = map(int, sys.stdin.readline().split())
    no = sector_no[(start, end)]
    for left in range(no, -1, -1):
        surface = min(surface, bottom[left])
        top[left] = max(surface, top[left])
    print("top:", top)
    surface = bottom[no]
    for right in range(no + 1, n):
        surface = min(surface, bottom[right])
        top[right] = max(surface, top[right])
    print("top22:",top)

ans = 0
for no in range(n):
    ans += width[no] * (bottom[no] - top[no])
print(ans)