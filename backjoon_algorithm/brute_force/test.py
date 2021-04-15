import sys
input = sys.stdin.readline
def check(num):
    num = list(str(num))
    #print("num:",num)
    for i in num:
        #print("i:",i)
        if i in s: return False
    return True
n = int(input())
m = int(input())
s = list(input().strip())
result = abs(n - 100)
for i in range(1000001):
    #print("i:",i)
    if check(i):
        #print(len(str(i)) + abs(i - n))
        result = min(result, len(str(i)) + abs(i - n))
        #print("result:",result)
print(result)