#문자열 화폐
'''
dfs ->메모리 초과
'''
import sys

n,x=map(int,sys.stdin.readline().split())
result,num='',26
if n*26<x or x<n: print('!')
else:
    # 문자열을 다 A로 설정 한 다음, 남은 가치(x)만큼 알파벳을 변경
    strList = ['A']*n
    x-=n
    idx=n-1
    while x>0:
        if x>=25:
            strList[idx]='Z'
            idx-=1
            x-=25
        else:
            strList[idx]=chr(x+65)
            break
    print(''.join(strList))