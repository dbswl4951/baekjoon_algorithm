from sys import stdin
from heapq import heappop, heappush
input = lambda: map(int,stdin.readline().split())

def search(s):
    D = [float('inf') for _ in range(node_num+1)]
    D[s] = 0
    q = [(0,s)]

    while q:
        w,p = heappop(q)

        if D[p] < w:
            continue
        for np in graph[p]:
            nw = graph[p][np]
            print("np,nw:", np,nw)
            if D[np] > nw+w:
                D[np] = nw+w
                heappush(q,(D[np],np))
    return D

T = int(stdin.readline())

for _ in range(T):
    node_num,edge_num,cand_num = input()
    S,G,H = input()

    graph = [dict() for _ in range(node_num+1)]

    for _ in range(edge_num):
        a,b,d = input()
        d*= 2
        graph[a][b] = d
        graph[b][a] = d
    print("graph:",graph)

    cand = [int(stdin.readline()) for _ in range(cand_num)]

    # 홀수로 만들기
    graph[G][H] -= 1
    graph[H][G] -= 1
    print("graph2:", graph)

    res = search(S)
    # 홀수인 애들이 정답
    answer = [ c for c in cand if res[c]%2 == 1]
    print("res:",res)
    print("answer:",answer)

    answer.sort()
    print(' '.join(map(str,answer)))