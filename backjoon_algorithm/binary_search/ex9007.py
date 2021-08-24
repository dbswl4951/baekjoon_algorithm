#카누 선수
'''
O(N^2)으로 해결해야 하는 문제

[ 문제 아이디어 ]
class의 개수는 4개로 지정되어있다.
2개씩 나눠서 그 2개의 list에서 나올 수 있는 (O(N^2)) 모든 값을 각각 저장한다.
리스트 한 개는 오름차순, 나머지는 내림차순으로 정렬
이분 탐색을 이용 해 근사한 값 찾기

우선순위 큐로 접근했다가 실패한 문제
정렬 + 이분탐색 문제였음..
class를 2개로 나눠서 더하고, 정렬 한다는 아이디어가 어려웠던 문제.
'''
import sys

t=int(sys.stdin.readline().strip())
for _ in range(t):
    k,n=map(int,sys.stdin.readline().split())
    classes, upClass, downClass = [], [], []
    for _ in range(4):
        temp = list(map(int,sys.stdin.readline().split()))
        classes.append(sorted(temp))

    # 2개씩의 리스트를 묶어서 나올 수 있는 모든 수를 upClass, downClass에 저장 => O(n^2)
    for i in range(n):
        for j in range(n):
            upClass.append(classes[0][i]+classes[1][j])
            downClass.append(classes[2][i]+classes[3][j])
    upClass.sort()
    downClass.sort(reverse=True)

    result=float('inf')
    first,second,length = 0,0,n*n
    while first<length and second<length:
        total = upClass[first] + downClass[second]

        if abs(result-k)>abs(total-k):
            result=total
        elif abs(result-k)==abs(total-k):
            result=min(result,total)

        if k<=total: second+=1
        else: first+=1
    print(result)