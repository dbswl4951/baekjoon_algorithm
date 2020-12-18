#회의실 배정
'''
n의 범위가 10만 => 2중포문 써서 O(n**2)의 알고리즘을 사용하면 시간초과!
따라서 끝나는 시간을 기준으로 정렬한 뒤, 가장 빨리 끝나는것부터 끝낼 수 있는지 확인 => O(n)으로 가능
'''
import sys

n=int(input())
table=[]
for i in range(n):
    table.append(tuple(map(int,sys.stdin.readline().split())))
table.sort(key=lambda x:(x[1],x[0]))
result=1
finish=table[0][1]
for i in range(1,len(table)):
    if table[i][0]>=finish:
        finish=table[i][1]
        result+=1
print(result)