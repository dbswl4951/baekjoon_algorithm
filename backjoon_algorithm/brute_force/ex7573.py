#고기잡이
'''
1. 그물의 크기 정하기 (w+h=l//2)
2. 물고기 한 마리씩의 위치에서 그 물고기가 포함 될 수 있는 범위에서 모든 wXh 그물을 펼쳐 봄
    1) 그물 가로(x) 검사
        (해당 물고기 x좌표 - h, 해당 물고기 x좌표 + h)내에 있는 물고기 targetFish에 저장
    2) 그물 세로(y) 검사
        tagetFish 물고기 한 마리씩 검사
        (해당 물고기 y좌표 - w, 해당 물고기 y좌표 + w)내에 있는 물고기 개수 구함
        구한 값이 최종 물고기 개수

- 왜 j, jj는 0으로 초기화 해 주지 않는걸까?
    이미 fishes, targetFishes를 정렬 해 줬기 때문에, i~j 부분은 이미 다 처리 됨
    또한 그물을 오른쪽 아래 방향으로만 펼칠 수 있다 (j, jj가 증가하는 방향으로만)

    ex) fishes = [(1,3),(2,3),(3,5),(6,3)]
        i=0, j=3 => 0 ~ 2번째 물고기는 같은 그물에 있을 수 있다는 뜻
        다음 반목문인
        i=1에서 0 ~ 1번째는 이미 i=0에서 처리됐다
               1 ~ 2번째도 이미 i=0에서 처리됐따
        따라서 i=1일 때, j는 그대로 3부터 시작하면 됨
'''
import sys

n,l,m = map(int,sys.stdin.readline().split())
fishes = sorted([list(map(int,sys.stdin.readline().split())) for _ in range(m)])
fishesY = [fish[1] for fish in fishes]
l//=2

result=0
# 그물 크기 구하기
for w in range(1,l):
    h=l-w

    # i번째 물고기와 같은 그물에 있을 수 있는 물고기 구하기 (x 확인)
    j=0
    for i in range(m):
        while j<m and fishes[j][0]-fishes[i][0]<=h:
            j+=1
        targetFishes = sorted(fishesY[i:j])

        # ii번째 물고기와 같은 그물에 있을 수 있는 물고기 구하기 (y 확인)
        jj=0
        for ii in range(j-i):
            while jj<j-i and targetFishes[jj]-targetFishes[ii]<=w:
                jj+=1
            result = max(result,jj-ii)
print(result)