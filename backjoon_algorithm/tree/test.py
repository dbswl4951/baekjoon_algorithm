from collections import defaultdict
import sys
input = sys.stdin.readline
t = int(input())

def dfs(cur, visited):
    visited[cur] = True
    print("dfs === cur, visited:", cur, visited)
    count = 0
    for i in tree[cur]:
        if not visited[i[0]]:
            print('next, count',i[0],count)
            count += min(i[1], dfs(i[0], visited))
            print('count:',count)
            #visited[i[0]] = True
        else:
            continue
    if count == 0:
        return 1e9
    else:
        print("return count :",count)
        return count


for _ in range(t):
    vertex, edge = map(int, input().split())
    tree = defaultdict(list)
    visited = [False] * (vertex + 1)
    for _ in range(edge):
        a, b, c = map(int, input().split())
        tree[a].append((b, c))
        tree[b].append((a, c))
    if vertex == 1:
        print(0)
    else:
        print(dfs(1, visited))