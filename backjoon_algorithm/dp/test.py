from sys import stdin

n, k = map(int, stdin.readline().rstrip().split())
students = [0] * n
data = [0] *10
count = 0

for rank in range(n):
    name = len(stdin.readline().rstrip())
    students[rank] = name
    print("rank,name:",rank,name)
    print("student:",students)
    if rank > k:
        data[students[rank - k - 1]] -= 1
        print("data:",data)
    count += data[name]
    data[name] += 1
    print("count:",count)
    print("data2:",data)

print(count)
