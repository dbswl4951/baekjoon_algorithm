#옥상 정원
import sys

n=int(sys.stdin.readline().strip())
building=[int(sys.stdin.readline().strip()) for _ in range(n)]
stack=[]    # -> 방향으로 볼 수 있는 빌딩 저장
result=0
for b in building:
    while stack and stack[-1]<=b:
        stack.pop()
    stack.append(b)
    # 기존에 stack에 있던 빌딩들이 새로 append된 b를 볼 수 있으므로, 
    # b를 제외한 (len(stack)-1) 모든 빌딩의 개수를 더함
    result+=len(stack)-1
print(result)