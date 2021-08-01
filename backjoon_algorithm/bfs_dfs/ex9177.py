#단어 섞기
'''
dfs 사용

맨 처음에 시간 초과
코드에 (1) : return, (2) : sorted를 추가시켰더니 통과
sorted를 사용하면 더 시간복잡도가 클 줄 알았는데 아니였음!
=> sorted를 사용 해 str1, str2로 word를 만들 수 있는지 check
=> 만들 수 없으면 아예 dfs를 시작하지 않는다 (시간복잡도 줄이기)
'''
import sys

def dfs(str1,str2,word):
    global flag
    if not word: flag=1
    # (1) : 만약 이미 단어를 만들었다면 바로 return
    if flag: return

    if str1 and word[0]==str1[0]:
        temp1=str1[0]
        str1=str1[1:]
        dfs(str1,str2,word[1:])
        str1=temp1+str1
    if str2 and word[0]==str2[0]:
        temp1= str2[0]
        str2 = str2[1:]
        dfs(str1, str2, word[1:])
        str2 = temp1 + str2

n=int(sys.stdin.readline().strip())
for i in range(1,n+1):
    flag=0
    str1,str2,word=sys.stdin.readline().split()
    print('Data set', i, end='')
    print(':', end=' ')
    # (2) : str1, str2로 word를 만들 수 없으면 dfs를 아예 시작하지 X
    if sorted(str1+str2)==sorted(word):
        dfs(str1,str2,word)
    if flag: print('yes')
    else: print('no')