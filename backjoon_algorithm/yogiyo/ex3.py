'''
N보다 큰 가장 작은 정수 구하기 (동일한 연속된 숫자가 있는 정수 빼고)
'''
def solution(N):
    while True:
        N+=1
        N=str(N)
        for i in range(1,len(N)):
            if N[i-1]==N[i]:
                n=int(N[i]) + 1
                if n==10: N[i-1].replace(int(N[i-1])+1)
                else:N[i].replace(N[i],str(n))
        else: break
    print(N)

print(solution(55))
print(solution(1765))
print(solution(98))
print(solution(44432))
