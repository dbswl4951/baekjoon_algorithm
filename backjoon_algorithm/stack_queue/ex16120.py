#PPAP
import sys

string=sys.stdin.readline().strip()
stack=[]
for idx,s in enumerate(string):
    stack.append(s)
    if stack[-4:]==['P','P','A','P']:
        for i in range(3): stack.pop()
if stack==['P']: print('PPAP')
else: print('NP')