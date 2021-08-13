#즐거운 단어
import sys

def dfs(n,mo,za,flag,count):
    global result

    # 자음 or 모음이 3번 연속 된 경우
    if mo>=3 or za>=3: return
    if n==nLen:
        # 'L'이 없는 경우
        if flag: result+=count
        return

    now = string[n]
    # 현재 문자가 지정되어 있다면 자음, 모음인지 확인 (경우의 수는 1이므로 변화 X)
    if now!='_':
        if now in ('A','E','I','O','U'):
            dfs(n+1,mo+1,0,flag,count)
        else:
            dfs(n+1,0,za+1,flag,count)
    # '_'인 경우, 들어 갈 수 있는 모든 경우 계산
    else:
        # 모음 넣기
        dfs(n+1,mo+1,0,flag,count*5)
        # 자음 넣기 ('L'이 있는지 없는지에 따라)
        if not flag:
            # 'L' 넣기
            dfs(n+1,0,za+1,1,count)
            # 'L' 무시
            dfs(n+1,0,za+1,0,count*20)
        else:
            dfs(n+1,0,za+1,flag,count*21)

string=list(sys.stdin.readline().strip())
nLen,flag=len(string),0
if 'L' in string: flag=1
result=0
dfs(0,0,0,flag,1)
print(result)