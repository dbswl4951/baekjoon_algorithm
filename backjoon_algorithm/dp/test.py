import re

def solve(s):
    it=re.finditer('aa+|bb+', s)
    for i in it:
        print(i)
    # start: 매치 된 문자열의 시작 위치
    # end: 매치된 문자열의 끝 위치
    group = [(m.start(), m.end()) for m in re.finditer('aa+|bb+', s)]
    print("group:",group)
    if len(group) == 0: return 0
    if len(set(s)) == 1: return 1
    for g in group:
        print("g:",g)
        print(s[:g[0]] + s[g[1]:])
        if solve(s[:g[0]] + s[g[1]:]) == 1:
            return 1
    return 0

strings = [input() for _ in range(int(input()))]
for string in strings:
    print("string:",string)
    print(solve(string))