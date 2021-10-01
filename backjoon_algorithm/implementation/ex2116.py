#주사위 쌓기
import sys
'''
- 맨 아래 주사위를 정하면, 나머지 주사위의 윗면, 아랫면은 정해짐
- 윗면, 아랫면을 fix 해놓고 옆면을 회전시키면서 최댓값 구함
'''

n = int(sys.stdin.readline().strip())
dice = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
rotate = {0:5, 1:3, 2:4, 3:1, 4:2, 5:0}
result = 0

for i in range(6):
    maxVal = []
    numbers = [1, 2, 3, 4, 5, 6]

    # 첫번째 주사위 윗면, 아랫면 fix 후, 최댓값 구하기
    bottom = dice[0][i]
    top = dice[0][rotate[i]]
    numbers.remove(bottom)
    numbers.remove(top)
    maxVal.append(max(numbers))

    # 두번째 ~ n번째 주사위 윗면, 아랫면 fix 후, 최댓값 구하기
    for j in range(1,n):
        numbers = [1,2,3,4,5,6]
        bottom = top
        top = dice[j][rotate[dice[j].index(bottom)]]
        numbers.remove(bottom)
        numbers.remove(top)
        maxVal.append(max(numbers))
    result = max(result,sum(maxVal))
print(result)