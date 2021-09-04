#고냥이
import sys

n=int(sys.stdin.readline().strip())
string = sys.stdin.readline().strip()
start,end,result=0,0,0
dic={}
while len(string) > end >= start:
    if string[end] not in dic:
        dic[string[end]]=1
    else:
        dic[string[end]]+=1

    # n개보다 많은 문자열이 들어갔다면 문자 빼주기
    while len(dic)>n and start<=end:
        if dic[string[start]]==1:
            dic.pop(string[start])
        else:
            dic[string[start]]-=1
        start+=1

    if len(dic)<=n and end-start+1>result:
        result=max(result,end-start+1)
    end+=1
print(result)