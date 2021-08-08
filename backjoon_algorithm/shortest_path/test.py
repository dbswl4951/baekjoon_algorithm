import sys
import heapq

input = sys.stdin.readline

# 다익스트라 함수를 정의한다.
def djt(s, e):
    print("s,e:",s,e)
    time = [INF for _ in range(n+1)]
    time[1] = 0
    q = [(0, 1)]
    while q:
        t, now = heapq.heappop(q)
        print("dist,now:",t,now)
        if now==n: break
        for next, plus in graph[now]:
        	# 이걸 생각해야 한다.
            # s,e는 선택된 노드들로 그 노드들의 경우는 고려하지 않도록 한다.
            # s,e가 선택되면 그곳은 검문소가 되므로 continue해준다.
            if s==now and e==next or s==next and e==now: continue
            if t+plus < time[next]:
                time[next] = t+plus
                # 이부분은 pre함수를 만든다. 처음 다익스트라를 진행할때 pre함수가 만들어진다.
                if not s:
                    pre[next] = now
                    print("pre:",pre)
                heapq.heappush(q, (time[next], next))
    return time[n]

INF = sys.maxsize

# 입력값을 받아온다.
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a].append((b,t))
    graph[b].append((a,t))
print("graph:",graph)
# 이 부분이 중요!!
# 최단경로로 진행했을 경우, 각 노드(index)에 이전노드(value)로 저장한다.
# 즉, 1번 인덱스에 5가 저장되면 5->1로 노드가 진행하는 최단경로가 존재하는것이다.
# 검문소를 고르는데 사용된다.
pre = [0 for _ in range(n+1)]

# 검문하지 않을때, 최단 시간을 알아낸다.
# 이때, pre 리스트에 정보를 다 기입해둔다.
result = djt(0,0)

ans = -1
e = n

# 끝점부터 시작점으로 돌아오면서 하나씩 검문소로 만들어 본다.
while pre[e]!=0:
    s = pre[e]
    output = djt(s, e)
    print("output:",output)
    # 처음 값과 비교해서 답을 갱신해준다.
    if output != INF:
        diff = output-result
        ans = max(ans, diff)
    else:
        ans = -1
        break
    # 시작점을 다시 끝점으로 바꾸고 다음 경로에 검문소를 만든다.
    e = s
print(ans)