#사냥꾼
'''
1초안에 돌아가야 하므로 O(nlogn) 만에 해결해야 함
둘 중 하나를 fix해놓고 나머지 하나를 log시간 안에 해결해야 시간초과가 나지 않음
 1) 사대를 fixed할 경우
     각 사대에 사격거리 내에 있는 동물의 수를 탐색해야 하기 때문에 TLE 발생
 2) 동물을 fixed할 경우
    동물에 좌표에 따라 L값을 이용하면 자신을 저격할 수 있는 사대를 찾을 수 있음
    예를 들어 L=4이고, 동물이 (7,2)에 있다면 동물을 사냥할 수 있는 사로의 범위는 5~9임

<핵심>
각 동물의 가장 가까운 양쪽의 사대를 이분탐색으로 찾아 사냥할 수 있는지 확인 (탐색 범위 : 사대의 위치)
<아래 코드의 시간 복잡도>
O(NlogM)
'''
import sys

m,n,l=map(int,sys.stdin.readline().split())
gun=list(map(int,sys.stdin.readline().split())) #사대 위치
animal=[]
for _ in range(n):
    x,y=map(int,sys.stdin.readline().split())
    animal.append((x,y))
gun.sort()
animal.sort(key=lambda x:x[0])
#print(gun)
#print(animal)
result=0    #잡을 수 있는 동물의 수
idx=0
for i in range(n):  #동물의 위치에 따른 총 사격범위 따짐
    start,end=idx,m-1   #사대 index를 범위로 설정
    mid=0
    #print("start,end===",start,end)
    while start<=end:   #동물과 가까운 사대를 이진 탐색으로 찾음
        mid=(start+end)//2
        #print("mid:",mid)
        if gun[mid]<=animal[i][0]:  #x축 좌표를 기준으로 가장 가까운 왼쪽 사대를 찾음
            if m-1==mid or gun[mid+1]>animal[i][0]: #더이상 탐색 할 사대가 없으면 break
                #print("break!")
                break
            start=mid+1
        else:
            end=mid-1
    idx=mid
    if abs(animal[i][0]-gun[mid])+animal[i][1]<=l:  #왼쪽 사대 범위 안에 있을때
        result+=1
    elif m>mid+1 and abs(animal[i][0]-gun[mid+1])+animal[i][1]<=l:  #오른쪽 사대 범위 안
        result+=1
    #print("result==",result)
print(result)