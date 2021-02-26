#문자열 폭발
'''
단순 문자열 문제라고 생각했는데, stack을 활용하는 문제였음!
stack에 넣은 문자열을 앞에서부터 비교 할려고 했던게 miss..
뒤에서부터 비교하면 더 쉽게 가능하다!
'''
import sys

st=sys.stdin.readline().strip()
boom=sys.stdin.readline().strip()
boomLast=boom[-1]
bLen = len(boom)
stack=[]
for s in st:
    stack.append(s)
    if s==boomLast and ''.join(stack[-bLen:])==boom:
        #del과 슬라이스를 사용해서 한꺼번에 요소 삭제 가능!!
        del stack[-bLen:]
result=''.join(stack)
if result=='':
    print("FRULA")
else:
    print(result)