import sys
read = sys.stdin.readline
f = lambda: map(int, read().split())

n,m = f()
k = int(read())
box = [[(0,0,0) for _ in range(m+1)]]

for i in range(n):
    word = read().strip()
    print("word:",word)
    box.append([(0,0,0)])
    for j in range(m):
        left, up, cross = box[i+1][j], box[i][j+1], box[i][j]
        print("left,up,cross:",left,up,cross)
        a,b,c = 0,0,0
        if word[j] == 'J':
            a = 1
        if word[j] == 'O':
            b = 1
        if word[j] == 'I':
            c = 1
        print("a,b,c:",a,b,c)
        box[i+1].append((left[0]+up[0]-cross[0]+a, left[1]+up[1]-cross[1]+b, left[2]+up[2]-cross[2]+c))
        print("box:",box[1:])

for i in range(k):
    p,q,r,s = f()
    x,y = p-1, q-1
    A,B,C,D = box[r][s], box[x][y], box[x][s], box[r][y]
    print(str(A[0]+B[0]-C[0]-D[0]) + ' ' + str(A[1]+B[1]-C[1]-D[1]) + ' ' + str(A[2]+B[2]-C[2]-D[2]))