#신입 사원
'''
1. list[x][0]자리애들 비교
	1-1) 자기보다 숫자 작은 B가 발견 되면 list[a][0]와 list[b][0] 비교
		list[a][0]가 더 작다면 통과
		list[b][0]가 더 작다면 B에 대해 서류심사, 면접심사 점수 둘 다 떨어지는 것이므로
		list[b] = [100001,100001]로 바꿈 (탈락)
	1-2) 자기보다 더 숫자 적은애가 없다면 통과 (1등인 경우)
========> 시간 초과로 실패!!!
'''

import sys

t = int(sys.stdin.readline())
passList=[]
for i in range(t):
    rankList = []
    count = 0
    n = int(sys.stdin.readline())  # 지원자 수
    for j in range(n):
        rankList.append(tuple(map(int, sys.stdin.readline().split())))
    rankList.sort()     #서류순위 1등부터 정렬
    ranking=rankList[0][1]      #서류순위 1등의 면접순위를 최솟값으로 설정
    for j in range(len(rankList)):
        if j==0:
            count+=1    #1등은 무조건 통과
        else:
            if ranking>rankList[j][1]:  #현재 지원자의 면접 순위보다 더 높은 지원자가 있다면 통과
                count+=1
                ranking=rankList[j][1]      #통과 할 순위 재지정
    passList.append(count)
for i in passList:
    print(i)

'''
import sys

t = int(sys.stdin.readline())     #테스트 케이스 수
passNum=0   #선발 인원
result=[]

for i in range(t):
    rankList=[]     #서류 순위,면접순위가 담긴 2차원 리스트
    n = int(sys.stdin.readline())     #지원자 수
    for j in range(n):       #sys.stdin.readline() : 대량의 데이터를 반복적으로 입력받을 때 사용. 속도 향상!!
        rankList.append(list(map(int,sys.stdin.readline().split())))    #서류 순위,면접 순위 입력 후 리스트에 추가
    for rank in rankList:      #rank=[1,2], [2,3]...
        for k in range(len(rankList)):
            if rank[0]>rankList[k][0]:   #현재 지원자의 서류 순위보다 다른 지원자의 서류 순위가 높고
                if rank[1]>rankList[k][1]:    #현재 지원자의 면접 순위보다 다른 지원자의 면접 순위가 높다면
                    rank[0] = 100001
                    rank[1] = 100001
            else:
                continue
    for rank in rankList:
        if rank[0]!=100001:
            passNum+=1
    result.append(passNum)
    passNum=0
for i in result:
    print(i)
'''