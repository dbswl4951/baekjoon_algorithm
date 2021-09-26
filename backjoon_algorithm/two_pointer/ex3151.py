#합이 0
import sys

n = int(sys.stdin.readline().strip())
scores = sorted(list(map(int,sys.stdin.readline().split())))
result = 0

# 기준 팀(i) 한 개 선택 후, 투포인터 (left, right)사용
for i in range(n-2):
    if scores[i]>0: break
    # 정렬을 했기 때문에, 양 극단에서 시작하여 점점 범위 줄여 줌
    left,right = i+1,n-1
    goal = -scores[i]
    idx = n

    while left<right:
        value = scores[left]+scores[right]
        if value<goal:
            left+=1
        elif value>goal:
            right-=1
        else:
            # 두 수가 같은 경우, 두 수 사이의 수는 모두 같기 때문에 두 수 사이의 개수만큼 더함
            if scores[left] == scores[right]:
                result += right-left
            else:
                # idx ~ right는 같은 수
                # 따라서 left만 계속 옮겨주면서, 같은 수의 갯수인 'right-idx'만큼을 result에 더 함
                # 한 번 실행 후엔 while문을 돌지 않고 result에 값만 더 해주면 됨 (시간 줄일 수 있음)
                if idx > right:
                    idx = right
                    # scores[right]와 같은 수 count
                    while idx>left and scores[right]==scores[idx-1]:
                        idx-=1
                result += right-idx+1
            # tmp==goal이여도, scores[left]와 같은 수가 존재 할 수 있기 때문에 left 1 증가
            left+=1
print(result)