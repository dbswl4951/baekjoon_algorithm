'''
1. 0~9 or , 로 구성
2. 0원을 제외하고, 0이 왼쪽에 올 수 X
3. ,를 포함하거나 아예 안포함
4. ,는 오른쪽부터 3개씩
5. ,는 맨 앞, 맨 뒤에 있지 않음
'''

def solution(amountText):
    contain=0
    if len(amountText)==1 and amountText=='0': return True
    if ',' in amountText: contain=1

    for idx,at in enumerate(reversed(amountText)):
        #print("idx, at:",idx,at)
        # 조건 1
        if not at.isdigit() and at!=',': return False
        # 조건 2
        if idx==len(amountText)-1 and at=='0': return False
        # 조건 3
        if not contain and at==',': return False
        # 조건 4
        if contain:
            if idx%4==3 and at!=',': return False
            elif idx==0 and at==',': return False
            # 조건 5
            elif idx==len(amountText)-1 and at==',': return False
    return True

#print(solution('1,000'))
#print(solution('011'))
#print(solution('25,000,123'))
#print(solution('24,999,99'))
#print(solution(',999,000'))
#print(solution('99,000,'))
#print(solution(',300'))
#print(solution('1101,010'))
#print(solution('1,'))
print(solution('71,872,534'))