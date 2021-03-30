#한 줄로 서기
'''
1. 키가 1인 사람부터 차례대로 세움
2. 주어진 입력에 따라서 자신보다 키가 큰 인원의 수만큼 왼쪽에 빈자리를 놔두고 자리 잡기
아이디어가 생각이 안나서 힌트를 봤다ㅜ
'''
n = int(input())
people = list(map(int,input().split()))
result=[0]*n
for i in range(1,n+1):
    count=0
    t=people[i-1]
    for j in range(n):
        if count==t and result[j]==0:
            result[j]=i
            break
        elif result[j]==0:
            count+=1
# * : Unpacking 역할!! *을 앞에 붙여주면 양 옆에 괄호를 벗겨낸다. (튜플,리스트등 사용 가능)
print(*result)