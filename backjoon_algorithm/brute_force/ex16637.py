#괄호 추가하기
'''
브루트포스 + dfs

조합+문자열 문제인줄 알았는데 dfs 문제였다
del,insert를 사용하지 않고 index를 이용 해 요소에 접근 후, 계산 누적
'''
import sys

def dfs(idx,total):
    global result
    if idx==len(operation):
        result=max(result,int(total))
        return
    #앞 부터 계산
    first=str(eval(total+operation[idx]+numbers[idx+1]))
    dfs(idx+1,first)
    #뒤 부터 계산
    if idx+1<len(operation):
        second=str(eval(numbers[idx+1]+operation[idx+1]+numbers[idx+2]))
        second=str(eval(total+operation[idx]+second))
        #operation을 2개 사용했으므로 idx+2
        dfs(idx+2,second)

n=int(sys.stdin.readline().strip())
expression=list(sys.stdin.readline().strip())
result=-int(1e9)
numbers,operation=[],[]
for ex in expression:
    numbers.append(ex) if ex.isdigit() else operation.append(ex)
dfs(0,numbers[0])
print(result)