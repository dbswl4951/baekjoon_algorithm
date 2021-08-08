import sys
import bisect

input=sys.stdin.readline

n,m,k=map(int,input().split())

# 이진탐색으로 key들을 저장할 리스트
keys=[]

# 정확한 key와 value를 저장하기 위한 dict()
dic=dict()

# 이진탐색으로 키를 삽입함(순서대로 넣기위함)
def putkey(key):
    bisect.insort(keys,key)
    return

# k범위 안의 키가 있는지 찾는 것
def findkey(key):
    val=dic.get(key,-1)
    #print("val:",val)
    leng=len(keys)
    if val != -1:
        return key
    # 찾는 key값이 없다면
    else:
        key_idx=bisect.bisect(keys,key)
        # 입력한 key가 들어갈 예상될 곳이 첫 번째 인덱스일 때
        if key_idx==0:
            if abs(keys[0]-key)<=k:
                return keys[0]
        # 입력한 key가 들어갈 예상될 곳이 마지막 인덱스일 때
        elif key_idx==leng:
            if abs(keys[key_idx-1]-key)<=k:
                return keys[key_idx-1]
        else:
            # 답이 ?가 나와야함
            if keys[key_idx]-key==key-keys[key_idx-1]:
                return -2
            # 답 1개(왼쪽 키가 조건에 맞음)
            if keys[key_idx]-key>key-keys[key_idx-1]:
                if key-keys[key_idx-1]<=k:
                    return keys[key_idx-1]
            # 답 1개(오른쪽 키가 조건에 맞음)
            if keys[key_idx]-key<key-keys[key_idx-1]:
                if keys[key_idx]-key<=k:
                    return keys[key_idx]
    return -1

for i in range(n):
    key,val=map(int,input().split())
    dic[key]=val
    putkey(key)
print("dic:",dic)

for i in range(m):
    arr=list(map(int,input().split()))
    if arr[0]==1:
        # 값들을 저장한다
        # 여기는 정확한 키 밸류값
        dic[arr[1]]=arr[2]
        # 정확한 키를 저장
        putkey(arr[1])
    if arr[0]==2:
        tmpkey=findkey(arr[1])
        if tmpkey==-1 or tmpkey==-2:
            continue
        else:
            dic[tmpkey]=arr[2]
    if arr[0]==3:
        tmpkey=findkey(arr[1])
        if tmpkey==-1:
            print(-1)
        elif tmpkey==-2:
            print("?")
        else:
            print(dic[tmpkey])