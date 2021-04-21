import sys
input = sys.stdin.readline
n, k = map(int, input().split())
s = list(input().strip())
t, tk = [], k
print(s)
for i in range(n):
    print("s[i]===",s[i])
    while tk > 0 and t and t[-1] < s[i]:
        print("tk,t::",tk,t)
        del t[-1]
        tk -= 1
    t.append(s[i])
print(''.join(t[:n - k]))