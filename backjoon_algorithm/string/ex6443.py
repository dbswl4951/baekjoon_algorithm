#애너그램
import sys

def dfs(idx,end,s):
    if idx==end:
        print(s)

    for i in range(end):
        if not visited[i]:
            temp=s+string[i]
            # string을 sort()해줬기 때문에, 무조건 알파벳 순서대로 문자열을 생성하게 된다
            # 만약 temp값이 이미 있다면, 그에 관련된 문자는 다 처리 된 것이므로 건너뛴다
            if temp not in record:
                visited[i]=1
                record.add(temp)
                dfs(idx+1,end,temp)
                visited[i]=0

n=int(sys.stdin.readline().strip())
for _ in range(n):
    string=list(sys.stdin.readline().strip())
    string.sort()
    visited=[0]*len(string)
    record=set()
    dfs(0,len(string),'')