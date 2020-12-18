#모험가 길드
'''
1. 공포도를 오름차순으로 정렬
2. 앞부터 공포도를 확인.
 현재 그룹에 포함된 모험가의 수가
 현재 확인하고 있는 공포도보다 크거나 같다면 이를 그룹으로 설정
'''

n=int(input())
fear = list(map(int,input().split()))
fear.sort()
group=0     #총 그룹의 수
member=0    #현재 그룹에 포함된 모험가의 수

for f in fear:
    member+=1
    if f<=member:   #공포도 크기보다 멤버수가 같거나 많으면
        group+=1    #그룹 결선
        member=0
print(group)