#가르침
'''
딕셔너리 + combinations 이용

1. 가르칠 수 있는 수가 k개보다 적으면 0 리턴 ('a','n','t','i','c'는 꼭 필수로 가르쳐야 한다)
2. 딕셔너리를 이용해서 각 단어의 알파벳 수 카운트 (단, 한 단어에 동일 한 알파벳은 카운트 1만 해줌)
3. 가르칠 수 있는 k-5개보다 가르쳐야 할 알파벳 수가 적으면, 모두 단어 읽을 수 있으므로 단어 수만큼 return
4. (3)가 아니라면 for문으로 단어 돌면서 그 단어를 읽을 수 있는지 check + result를 가장 큰 값으로 갱신
'''
import sys,copy
from itertools import combinations

n,k=map(int,sys.stdin.readline().split())
words=[list(sys.stdin.readline()) for _ in range(n)]
if k<5:
    print(0)
    sys.exit(0)

k-=5
word={'a','n','t','i','c'}
dic={}
for w in words:
    temp=[]
    for i in range(4,len(w)-4):
        if w[i] not in word and w[i] not in temp:
            temp.append(w[i])
            if w[i] not in dic.keys():
                dic[w[i]]=1
            else:
                dic[w[i]]+=1

result=0
if len(dic)<k:
    print(len(words))
    sys.exit(0)

for case in combinations(dic,k):
    cWord=copy.deepcopy(word)
    cnt=0
    for c in case:
        cWord.add(c[0])
    for w in words:
        for i in range(4, len(w)-4):
            if w[i] not in cWord: break
        else: cnt+=1
    result=max(result,cnt)
print(result)
