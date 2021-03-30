#곱하기 혹은 더하기
'''
<핵심 아이디어>
두 수에 대하여 연산을 수행 할 때, 두 수 중 하나라도 1이하인 경우는 더하고,
두 수가 모두 2이상인 경우 곱한다
'''

str = list(map(int,input()))
maxNum=str[0]
for i in range(1,len(str)):
    if maxNum<2 or str[i]<2:
        maxNum+=str[i]
    else:
        maxNum*=str[i]
print(maxNum)