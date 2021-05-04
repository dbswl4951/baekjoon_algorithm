#후위 표기식
'''
1. 피연산자는 바로 result에 더하기
2. 괄호
    1) '(' : ')'만나기 전까지의 연산자를 저장해야 하므로, 시작을 알기 위해 '(' stack에 저장
    2) ')' : '('만날 때까지 pop() 수행 => 그 동안의 () 연산 모두 result에 더하기
3. 연산자는 우선순위를 나눠서 생각 해야 함
    우선 순위가 높은 애가 stack에 저장 되어 있으면, stack.pop()해서 먼저 처리
    아니라면 연산자 stack에 저장
'''
import sys

operation=sys.stdin.readline().strip()
stack=[]
priority={'*':2,'/':2,'+':1,'-':1,'(':0,')':0}

for oper in operation:
    # 피연산자 (알파벳)
    if oper.isalpha():
        print(oper,end='')
    elif oper=='(':
        stack.append(oper)
    elif oper==')':
        while stack:
            top=stack.pop()
            if top=='(': break
            print(top,end='')
    else:
        # stack에 저장 된 연산자의 우선 순위가 현재 연산자보다 높다면, stack 연산자부터 처리
        while stack and priority[stack[-1]]>=priority[oper]:
            print(stack.pop(),end='')
        stack.append(oper)

# 나머지 연산자 처리
while stack:
    print(stack.pop(),end='')