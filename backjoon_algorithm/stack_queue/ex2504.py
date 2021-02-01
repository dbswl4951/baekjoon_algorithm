#괄호의 값
'''
1. 입력받은 문자 순서대로 검사
 1) 괄호를 여는 기호 => stack_queue 리스트에 append(push)
 2) 괄호를 닫는 기호 => 자신에게 맞는 알맞는 괄호 여는 기호 만날 때 까지 pop
2. pop 후 연산 결과를 stack_queue 리스트에 append(push)
3. 만약 연산이 곱해져야 할 상황이라면 (괄호 안에 괄호가 있는 경우)
 기존에 저장되어있던 값 모두 더해주고, 괄호에 맞는 곱셈 실행 후, stack에 다시 저장
4. 자신에게 맞지 않는 닫는 기호 만날 경우 0출력 후 종료 (잘못된 입력)

예전에 비슷한 문제를 풀어 본 기억이 있는데 다시 풀려니까 잘 못 풀겠어서 다른 사람 풀이 참조..
**괄호 문제는 stack_queue 문제임을 명시!!
**push와 pop을 알맞게 사용하자!!
'''
import sys

s=list(sys.stdin.readline().strip())
stack=[]
#여는 괄호는 append. 닫는 괄호는 연산 수행
for i in s:
    if i==')':
        temp=0  #앞에 괄호가 아니라 숫자가 있다면, 그 숫자를 담는 변수
        while stack:
            top=stack.pop() #맨 뒤에 있는 원소 pop
            if top=='(':
                if temp==0:
                    stack.append(2)
                else:
                    stack.append(2*temp)
                break
            elif top=='[':  #잘못된 괄호
                print('0')
                sys.exit(0)
            else:   #stack에서 꺼낸게 괄호가 아니라 숫자라면 연산 필요
                if temp==0:
                    temp=int(top)
                else:
                    temp=temp+int(top)  #이미 숫자를 꺼냈고, 현재 꺼낸 것도 숫자라면 더하기 연산 수행
    elif i==']':
        temp=0
        while stack:
            top=stack.pop()
            if top=='[':
                if temp==0:
                    stack.append(3)
                else:
                    stack.append(3*temp)
                break
            elif top=='(':
                print('0')
                sys.exit(0)
            else:   #꺼낸게 숫자라면
                if temp==0:
                    temp=int(top)
                else:
                    temp=temp+int(top)
    else: stack.append(i)
result=0
for i in stack:
    if i=='(' or i=='[':
        print('0')
        sys.exit(0)
    else: result+=i
print(result)