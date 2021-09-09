#단어 맞추기
'''
단순 순열로 풀면 시간초과가 난다.
next_permutation 함수를 구현 해서 풀어야 함

[ next_permutation ]
1. 끝-1부터 시작해서 앞에것이 더 작은 곳을 i로 정함
2. 끝부터 시작해서 i보다 큰 것을 j로 정함
3. i, j값을 바꿈
4. i뒤에 있는 것들을 reverse 해 줌
'''
import sys

def nextPermutation(word):
    i = len(word)-2
    # 수 적은애, 큰애 순으로 나오는 idx 찾기
    while i>=0 and word[i]>=word[i+1]: i-=1
    # 주어진 단어가 마지막 단어일 때
    if i==-1: return False

    j = len(word)-1
    # i보다 큰 j 찾기
    while word[i]>=word[j]: j-=1

    word[i],word[j] = word[j],word[i]
    result = word[:i+1]
    result.extend(reversed(word[i+1:]))
    return ''.join(result)

t = int(sys.stdin.readline().strip())
for _ in range(t):
    word = list(sys.stdin.readline().strip())
    result = nextPermutation(word)
    if result: print(result)
    else: print(''.join(word))