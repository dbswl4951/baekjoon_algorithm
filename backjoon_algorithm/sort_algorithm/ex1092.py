#배
'''
1. 만약 크레인의 무게 제한보다 큰 박스가 있다면 -1 출력
2. 크레인, 박스 내림차순 정렬
3. 앞에서 부터 순서대로  박스 무게가 크레인의 무게 제한보다 작거나 같으면 크레인에 담고 옮기기 반복

시간 초과 때문에 del 말고 index를 사용해서 풀려다가 반례 폭탄으로 시간 엄청 끌었음.
그냥 del 사용해서 pypy로 제출ㅜ
'''
import sys

n=int(input())
limit=list(map(int,sys.stdin.readline().split()))
m=int(input())
box=list(map(int,sys.stdin.readline().split()))
limit.sort(reverse=True)
box.sort(reverse=True)

if limit[0] < box[0]:  # 크레인의 무게 제한보다 상자의 무게가 더 무거울 경우
    print(-1)
    exit()  #실행 중지
t=0
while box:
    for i in limit:
        for j in range(len(box)):
            if i>=box[j]:   #크레인으로 상자를 옮길 수 있으면
                del box[j]  #옮기고 리스트에서 삭제
                break   #다음 크레인으로 이동
    t+=1
print(t)





''' 실패 코드
def carry():
    global t
    idx = 0
    count = []
    if limit[0] < box[0]:  # 크레인의 무게 제한보다 상자의 무게가 더 무거울 경우
        return -1
    else:
        while idx < len(box):
            for i in range(len(limit)):
                if idx in count:
                    idx+=1
                    pass
                if idx < len(box):
                    if limit[i] >= box[idx]:
                        idx += 1
                    else:
                        if count:
                            count.append(count[-1] + 1)
                        else:
                            c = idx
                            while c < len(box):
                                if limit[i] < box[c]:
                                    c += 1
                                else:
                                    break
                            count.append(c)
            t += 1
        return t

n=int(input())
limit=list(map(int,sys.stdin.readline().split()))
m=int(input())
box=list(map(int,sys.stdin.readline().split()))
limit.sort(reverse=True)
box.sort(reverse=True)
t=0
print(carry())
'''