import sys
input = sys.stdin.readline

def combination(ind,len_string,combi):
    print("combi====idx,combi::",ind,combi)
    if ind == len_string:
        print("result:",combi)
    else:
        for k in range(len_string):
            if visited[k]:
                print("idx,combi,k:",ind,combi,k)
                print("visited:", visited)
                temp = combi+string_list[k]
                if temp not in record:
                    visited[k] = 0
                    record.add(temp)
                    combination(ind+1,len_string,temp)
                    visited[k] = 1
                    print("back===visited:",visited)
                else:
                    print("temp,record:",temp,record)

N = int(input())

for _ in range(N):
    string_list = list(input().strip())
    visited = {}
    string_list.sort()
    len_string = len(string_list)
    visited = [1]*(len(string_list))
    record = set()
    combination(0,len_string,'')