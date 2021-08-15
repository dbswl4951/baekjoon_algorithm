'''
1. 과세 금액
    : 공급가 액 - 비과세 금액 (부가가치세가 부과되지 않는 금액)
2. 공급대가
    = 공급가액 + 부가가치세
    = 주문 금액 - 봉사료
3. 부가가치세
    : 과세금액의 10%
    소수점 첫째자리 반올림
'''
import math

def solution(orderAmount, taxFreeAmount, serviceFee):
    # orderAmount : 주문금액
    # taxFreeAmount : 비과세금액
    # serviceFee : 봉사료
    result=0
    print(math.ceil(2*0.1))
    # 공급가액
    supplyAmount = orderAmount-serviceFee
    # 과세 금액
    taxAmount = supplyAmount-taxFreeAmount
    if taxAmount>=10:
        result=math.ceil(taxAmount*0.1)
    return result

print(solution(0,0,0))