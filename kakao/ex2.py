'''
0P0
P0
0P
P
- P는 0 포함 X
- P는 소수
'''
import string,math
tmp = string.digits+string.ascii_lowercase

# k진수로 변환
def convert(num, base) :
    q, r = divmod(num, base)
    if q == 0 :
        return tmp[r]
    else :
        return convert(q, base) + tmp[r]

# 소수 판별 (2이상의 자연수에 대하여)
def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임

def solution(n, k):
    num = convert(n,k)
    ableP= num.split('0')
    result=0
    for ap in ableP:
        if not ap or ap=='1': continue
        ap = int(ap)
        if is_prime_number(ap): result+=1
    return result

#print(solution(437674,3))
print(solution(110011,10))