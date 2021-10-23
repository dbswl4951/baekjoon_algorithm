'''
삼각형 성립 조건 : 가장 긴 변의 길이 < 다른 두 변의 길이 합
'''
def solution(size):
    result = []
    for a in range(1,size//2):
        for b in range((size-a)//2,a-1,-1):
            c = size-a-b
            if c<a+b:
                temp = sorted([a,b,c])
                if temp not in result: result.append(temp)
    return len(result)

print(solution(9))