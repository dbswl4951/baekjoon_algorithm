#물자열 뽑기
import sys,re

def dfs(string):
    # start: 매치 된 문자열의 시작 위치 반환
    # end: 매치된 문자열의 끝 위치 반환
    group=[(i.start(),i.end()) for i in re.finditer('aa+|bb+',string)]
    # 더이상 삭제 할 수 있는 패턴이 없다면 return 0
    if len(group)==0: return 0
    # 삭제 할 수 있는 패턴 있고, 중복 없앴을 때 길이가 1이면 모두 삭제 가능
    if len(set(string)) == 1: return 1

    for g in group:
        if dfs(string[:g[0]]+string[g[1]:]): return 1
    return 0

t=int(sys.stdin.readline().strip())
for _ in range(t):
    string=sys.stdin.readline().strip()
    print(dfs(string))