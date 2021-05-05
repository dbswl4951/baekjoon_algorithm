#문자열 폭발
import sys

# 2차 시도 (stack 사용)
string=sys.stdin.readline().strip()
explore=sys.stdin.readline().strip()
eLen=len(explore)
stack=[]

for s in string:
    stack.append(s)
    if ''.join(stack[-eLen:len(stack)])==explore:
        while True:
            top=stack.pop()
            if top==explore[0]: break

if stack: print(''.join(stack))
else: print('FRULA')


# 1차 시도 (투 포인터 + 슬라이싱 사용)
# => 시간 초과
'''
string=sys.stdin.readline().strip()
explore=sys.stdin.readline().strip()
eLen=len(explore)

start,end=0,eLen
while start<=end and end<len(string):
    temp=string[start:end]
    if explore==temp:
        string=string[:start]+string[end:]
        start,end=0,eLen
        continue
    start+=1
    end+=1
    if end==len(string):
        start+=1
        end=start+eLen

if string[-eLen:len(string)]==explore:
    string=string[:-eLen]
if string: print(string)
else: print('FRULA')
'''