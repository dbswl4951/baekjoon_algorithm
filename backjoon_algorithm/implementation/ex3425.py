#고스택
'''
[ 예외 상황 ]
1. 0으로 나눴을 때
2. 연산 결과의 절댓값이 10^9를 넘을 때

[ 음수 나눗셈 ]
1. 피연산자가 음수 => 절댓값을 씌운 뒤 계산
2. 몫
    1) 음수가 1개 일 경우 음수
    2) 그 외 양수
3. 나머지
    피제수 (나눠지는 숫자, 스택에서 더 윗 부분) 부호와 같음
'''
import sys
from collections import deque

# 연산 결과가 10^9 이하인지 체크
def checkRange(num):
    if abs(num)>1000000000: return 0
    return 1

while True:
    orders = []
    flag = 0
    while True:
        order = sys.stdin.readline().strip()
        if order=='QUIT': flag=1; break
        sOrder = order.split(' ')
        orders.append(sOrder)
        if order == 'END': break
    if flag: break

    n = int(sys.stdin.readline().strip())
    values = [int(sys.stdin.readline().strip()) for _ in range(n)]
    temp = sys.stdin.readline().strip()

    for value in values:
        q = deque()
        q.append(value)

        resultFlag = 0  # 결과값이 10^9승이 넘는지 확인
        # 프로그램 명령 실행
        for order in orders:
            if order[0]=='END': break

            if len(order)==1:
                if order[0]=='POP' and q: q.popleft()
                elif order[0]== 'INV' and q:
                    q.appendleft(-q.popleft())
                elif order[0]== 'DUP' and q:
                    q.appendleft(q[0])
                elif order[0]=='SWP' and len(q)>1:
                    q[0],q[1] = q[1],q[0]
                else:
                    if len(q)<2: resultFlag=1; break
                    val1 = q.popleft()
                    val2 = q.popleft()
                    if order[0]=='ADD':
                        if checkRange(val1 + val2): q.appendleft(val1 + val2)
                        else: resultFlag=1; break
                    elif order[0]=='SUB':
                        if checkRange(val2 - val1): q.appendleft(val2 - val1)
                        else: resultFlag=1; break
                    elif order[0]=='MUL':
                        if checkRange(val1 * val2): q.appendleft(val1 * val2)
                        else : resultFlag=1; break
                    elif order[0] == 'DIV':
                        if val1==0: resultFlag=1; break
                        val3 = int(abs(val2)/abs(val1))
                        if (val1<0 and val2>0) or (val1>0 and val2<0): q.appendleft(-val3)
                        else: q.appendleft(val3)
                    elif order[0] == 'MOD':
                        if val1 == 0: resultFlag = 1; break
                        val3 = abs(val2)%abs(val1)
                        if val2 < 0: q.appendleft(-val3)
                        else: q.appendleft(val3)
            # NUM X
            else:
                if checkRange(int(order[1])): q.appendleft(int(order[1]))
                else: resultFlag=1; break
        if len(q)!=1 or resultFlag: print('ERROR')
        else: print(q[0])
    print()