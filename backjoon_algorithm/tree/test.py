N =int(input().strip())
lst = []
for i in range(N):
    lst.append(int(input().strip()))
lst.sort(reverse=True)
print(lst)
twosum = {a+b for a in lst for b in lst}
print("twosum",twosum)
find=False
for a in lst:
    for b in lst:
        print("a,b : ",a,b)
        if a-b in twosum:
            print("result :",a)
            find=True
            break
    if find:
        break