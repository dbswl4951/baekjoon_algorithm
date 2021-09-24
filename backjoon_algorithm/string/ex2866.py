#문자열 잘라내기
import sys

r,c = map(int,sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(r)]
transeBoard = list(map(list,zip(*board)))
string = []
for i in range(c):
    string.append(''.join(transeBoard[i][1:]))
idx,result = 0,0

while idx<c:
    s = set(string)
    if len(s)==len(string):
        result+=1
        idx+=1
        for i in range(c):
            string[i] = string[i][1:]
    else: break
print(result)