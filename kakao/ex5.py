'''
- 0 : 양
- 1 : 늑대

dfs 순회
(11/18)개만 통과
'''
result=1

def dfs(info,graph,x,sheep,wolf,visited):
    global result

    if sheep<=wolf:
        return None,None,None
    visited[x]=1
    print("x,sheep,wolf:",x,sheep,wolf)

    for i in graph[x]:
        if not visited[i]:
            print("i:",i)
            # 양 만남
            if info[i]==0:
                result+=1
                print("result:",result)
                dfs(info,graph,i,sheep+1,wolf,visited)
            # 늑대 만남
            else:
                dfs(info, graph, i, sheep,wolf+1, visited)
    return result,wolf,visited

def solution(info, edges):
    graph = [[] for _ in range(len(info))]
    parent = [0]*len(info)
    for a,b in edges:
        graph[a].append(b)
        graph[b].append(a)
        parent[b]=a
    visited = [0]*len(info)
    visited[0]=1
    sheep, wolf, visited = dfs(info,graph,0,1,0,visited)
    for i in range(len(info)):
        if not visited[i]:
            dfs(info,graph,parent[i],sheep,wolf,visited)
    return result

#print(solution([0,0,1,1,1,0,1,0,1,0,1,1],[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))
print(solution([0,1,0,1,1,0,1,0,0,1,0],[[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]))
#print(solution([0,1,1,0,0,0,1,1,0],[[0,1],[0,5],[1,3],[5,7],[5,2],[2,4],[2,6],[4,8]]))
#print(solution([0,1,0,1,1,1,1,0,1,1,0],[[0,4],[0,2],[4,7],[7,1],[4,1],[2,5],[2,8],[5,6],[5,9],[6,10]]))