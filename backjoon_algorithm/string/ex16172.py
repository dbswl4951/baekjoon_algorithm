#나는 친구가 적다 (Large)
import sys,re

string=sys.stdin.readline().strip()
keyword=sys.stdin.readline().strip()
alpabet=''
for s in string:
    if s.isalpha(): alpabet+=s
if len(keyword)>len(alpabet): print(0)
else:
    alp=re.findall(keyword,alpabet)
    if not alp: print(0)
    else: print(1)