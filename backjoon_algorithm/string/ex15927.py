#회문은 회문아니야!!
'''
1. 모든 문자가 동일하면 result = -1
2. 팰린드롬인지 검사
    1) 팰린드롬이라면 result = 문자열 길이 -1
    2) 아니라면 문자열 길이

문자열 문제라기보단 그리디 문제 같다
'''
import sys

string = sys.stdin.readline().strip()
if len(set(string))==1:
    print(-1)
    sys.exit(0)
sLen = len(string)
for i in range(sLen//2):
    j=sLen-1-i
    # 팰린드롬이 아님
    if string[i]!=string[j]:
        print(sLen)
        sys.exit(0)
# 팰린드롬
print(sLen-1)
