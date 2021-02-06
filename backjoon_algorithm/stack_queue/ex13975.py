#파일 합치기3
'''
heapq를 사용
1. q에서 가장 작은 파일 두개를 뽑아 더한다.
 => 크기가 큰 파일을 일찍 합쳐버리면 그 파일은 언젠가 한 번 더 합쳐지기 때문에 최대한 늦추는 게 좋음
2. 합친걸 다시 큐에 추가. 반복

heapq를 사용하여 가장 작은 파일을 두개 뽑아 더하는 것 까지는 맞았으나,
합친 것을 그대로 큐에 넣고 가장 작은 두 수를 또 뽑아서 반복하지 않고
한 번에 q에서 작은것 두개 뽑아 더해서 다른 큐에 넣고, 또 q에서 작은 것 두 개 뽑아 더해서 다른 큐에 넣고...
q의 원소가 1개 이하로 남으면 다른 큐에서 또 계산을 수행해줬다.
'''
import sys,heapq

t=int(sys.stdin.readline().strip())
for _ in range(t):
    k=int(sys.stdin.readline().strip())
    numbers=list(map(int,sys.stdin.readline().split()))
    q=[]
    result=0
    for num in numbers:
        heapq.heappush(q,num)
    while len(q)>1:
        a=heapq.heappop(q)
        b=heapq.heappop(q)
        result+=(a+b)
        heapq.heappush(q,a+b)
    print(result)