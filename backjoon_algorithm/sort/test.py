buff = input()

memo = [[0 for i in range(501)] for j in range(501)]

for j in range(1,len(buff)):
    print("j====",j)
    for i in range(j-1,-1,-1):
        print("i:",i)
        if buff[i]+buff[j] in ('at','gc'):
            memo[i][j] = memo[i+1][j-1]+2
            print("memo[i+1][j-1],memo[i][j]:",memo[i+1][j-1],memo[i][j])
        for t in range(i+1,j):
            print("t:",t)
            print(memo[i][j],memo[i][t]+memo[t][j])
            memo[i][j] = max(memo[i][j],memo[i][t]+memo[t][j])

print(memo[0][len(buff)-1])