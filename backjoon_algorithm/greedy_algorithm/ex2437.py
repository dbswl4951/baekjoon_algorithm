#저울
'''
< 답안 풀이 >
1. 입력 값 오름차순 정렬
2. 다음에 등장하는 숫자가 (누적합 + 1) 이하라면
 누적합 + 1까지의 숫자들은 기존의 숫자들의 조합으로 모두 표현 가능 (초기에 1을 더했으므로 누적합 + 1)
3. 하지만, 다음에 등장하는 숫자가 (누적합 + 2) 이상이라면
 기존의 숫자들의 조합으로 (누적합 + 1) 표현이 불가능하므로 (누적합 + 1)을 출력
'''

n = int(input())
weight= list(map(int, input().split()))
weight.sort()
sum=0   #저울추의 무게 합
for i in range(n):
    if sum+1>=weight[i]:
        sum+=weight[i]
    else:
        break
print(sum+1)