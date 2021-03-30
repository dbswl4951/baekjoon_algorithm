#두 배열의 원소 교체
'''
O(NlogN)을 보장 해야 함
min,max 함수의 시간 복잡도는 O(N)이므로 적합하지 X
'''

n,k = map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i]<b[i]:
        a[i],b[i]=b[i],a[i]
    else:
        break
sum=0
for i in a:
    sum+=i
print(sum)


#시간 초과 풀이
'''
n,k = map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
minA=min(a)
maxB=max(b)

for i in range(k):
    if minA<maxB:
        a[a.index(minA)],b[b.index(maxB)]=b[b.index(maxB)],a[a.index(minA)]
        minA=min(a)
        maxB=max(b)

sum=0
for i in a:
    sum+=i
print(sum)
'''