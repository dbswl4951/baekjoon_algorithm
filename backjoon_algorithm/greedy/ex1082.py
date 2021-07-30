#방 번호
'''
1. 가장 비용 적은 숫자로 만들 수 있는 최대 자리수 구하기 (pick 리스트)
2. pick 리스트 뒤(가장 자리수 큰 애)부터 큰 숫자로 바꿀 수 있는지 차액 확인
3. 바꿀 수 있다면 변경 후, 다음 실행으로

if) 시작 숫자가 0이라면 0000..이 될 수 있음
 따라서 이 경우, 0을 환불 후, 돈을 다시 받고 0 이외의 수를 구매
if) 0을 다 팔았는데도 다른 숫자를 살 수 없으면 종료
'''
import sys

def check(remainMoney,digit):   # (남은 돈, 자리수)
    # 가장 자리수가 큰 오른쪽부터 큰 숫자 넣어보기
    for i in range(digit,-1,-1):
        # 현재 자리수가 가장 큰 수가 아니라면
        if pick[i]!=n-1:
            # 가장 큰 수부터 현재 수 전까지 넣어보기
            for j in range(n-1,pick[i],-1):
                newCost=cost[j]-cost[pick[i]]
                # 남은 돈으로 수 변경 할 수 있다면 변경
                if newCost<=remainMoney:
                    pick[i]=j
                    check(remainMoney-newCost,digit-1)
                    return

    # 모두 다 0이면 0팔고 다른 수 사기
    if not any(pick):
        if not pick:
            print(0)
            sys.exit(0)
        pick.pop()
        check(remainMoney+cost[0],digit-1)

n=int(sys.stdin.readline().strip())
cost=list(map(int,sys.stdin.readline().split()))
money=int(sys.stdin.readline().strip())
if n==1:
    print(0)
    sys.exit(0)

minCost=min(cost)
minNum=cost.index(minCost)
num=money//minCost  # 만들 수 있는 최대 자리수
pick=[minNum for i in range(num)]
allCost=num*minCost
check(money-allCost,num-1)

result=0
for i in range(len(pick)):
    result+=(10**i)*pick[i]
print(result)