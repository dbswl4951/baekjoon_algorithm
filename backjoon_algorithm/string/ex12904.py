#A와 B
import sys

s=sys.stdin.readline().strip()
t=sys.stdin.readline().strip()
tLen,sLen=len(t),len(s)
for _ in range(tLen-sLen):
    temp=t[-1]
    t = t[:-1]
    if temp=='B':
        t=t[::-1]
if t==s: print(1)
else: print(0)