N, I, M = map(int, input().split())
fishes = sorted(tuple(map(int, input().split())) for _ in range(M))
fishes_y = [x[1] for x in fishes]

I //= 2
answer = 0
print('fishes:',fishes)

for w in range(1, I):
    h = I - w
    j = 0
    print("w,h === ",w,h)
    # x좌표가 그물 내에 있는지 확인
    for i in range(M):
        print('i,j:', i, j)
        while j < M and fishes[j][0] - fishes[i][0] <= w:
            j += 1
        print('i,j:',i,j)

        target_fishes = sorted(fishes_y[i:j])
        print('target_fishes : ',target_fishes)

        # y좌표가 그물 내에 있는지 확인
        jj = 0
        for ii in range(j - i):
            while jj < j - i and target_fishes[jj] - target_fishes[ii] <= h:
                jj += 1
            print('ii,jj :',ii,jj)
            answer = max(answer, jj - ii)

print(answer)