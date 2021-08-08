#전설의 JBNU
'''
이분탐색 bisec 함수를 사용 해야 한다
'''
import sys,bisect

def insertKey(key):
    # 이진탐색으로 key 삽입 => 순서대로 정렬되어 삽입 됨
    bisect.insort(keys,key)

def findKey(key):
    # keysDic에 해당 key값이 있는지 찾음 => 없다면 -1 반환
    value = keysDic.get(key,-1)
    if value!=-1: return key

    # bisect_left() 함수를 통해 해당 key가 몇 번째 index에 삽입되는지 확인
    bisectIdx=bisect.bisect_left(keys,key)

    # key가 맨 앞에 삽입 될 시
    if bisectIdx==0:
        if abs(keys[0]-key)<=k: return keys[0]
    # key가 맨 뒤에 삽입 될 시
    elif bisectIdx==len(keys):
        if abs(key-keys[-1])<=k: return keys[-1]

    else:
        # 답이 2개
        if keys[bisectIdx]-key==key-keys[bisectIdx-1]:
            return -2
        # 답 1개 (왼쪽 키 반환)
        if keys[bisectIdx]-key>key-keys[bisectIdx-1]:
            if key-keys[bisectIdx-1]<=k:
                return keys[bisectIdx-1]
        # 답 1개 (오른쪽 키 반환)
        if keys[bisectIdx]-key<key-keys[bisectIdx-1]:
            if keys[bisectIdx]-key<=k:
                return keys[bisectIdx]
    return -1

n,m,k=map(int,sys.stdin.readline().split())
keys=[]
keysDic=dict()
for _ in range(n):
    a,b=map(int,sys.stdin.readline().split())
    insertKey(a)
    keysDic[a]=b

for _ in range(m):
    arr=list(map(int,sys.stdin.readline().split()))
    # (key,value) 삽입
    if arr[0]==1:
        insertKey(arr[1])
        keysDic[arr[1]]=arr[2]
    # key로 검색 된 데이터를 value로 변경
    elif arr[0]==2:
        tmpKey=findKey(arr[1])
        if tmpKey==-1 or tmpKey==-2: continue
        keysDic[tmpKey]=arr[2]
    # key로 검색한 value 출력
    else:
        tmpKey = findKey(arr[1])
        if tmpKey==-1: print(-1)
        elif tmpKey==-2: print('?')
        else: print(keysDic[tmpKey])