#결혼식

n=int(input())  #동기의 수
m=int(input())  #리스트의 길이
friend=dict()

for i in range(1,n+1):  #학번 1~n까지 동기들 딕셔너리 생성
    friend[i]=[]    #Key : 학번, Value : 친구들의 학번들
for _ in range(m):
    a,b = map(int,input().split())
    friend[a].append(b)
    friend[b].append(a)
invited=set(friend[1])  #상근(자기자신)의 친구들 초대
for i in friend[1]: #상근이의 친구들의 친구들 확인
    invited.update(friend[i])   #초대 할 사람 추가
print(len(invited)-1)   #자기 자신 제외