#가르침
'''
브루트포스 + 백트레킹 + dfs
'''
import sys

def dfs(idx,cnt):   #(알파벳 idx,남은k)
    global result
    #cnt: fixed 문자말고 추가로 더 배운 문자 수, k-5: 추가로 배울 수 있는 문자 수
    if cnt==k-5:
        readCnt=0
        for word in words:
            #for~else문 : for문이 break없이 완전하게 수행 되면, else문도 실행
            for w in word:
                if not learn[ord(w)-ord('a')]: break
            else:
                readCnt+=1
        result=max(result,readCnt)
        return
    #배울 수 있는 모든 알파벳을 하나씩 검사
    for i in range(idx,26):
        if not learn[i]:
            learn[i]=1
            dfs(i,cnt+1)
            learn[i]=0

n,k = map(int,sys.stdin.readline().split())
if k<5 or k==26:
    print(0 if k<5 else n)
    sys.exit(0)
words=[set(sys.stdin.readline().strip()) for _ in range(n)]
fixed=['a','n','t','i','c']
learn=[0]*26
result=0
for f in fixed:
    learn[ord(f)-ord('a')]=1
dfs(0,0)
print(result)