#월드컵
'''
1. 백트레킹 + 완탐 => DFS 사용
2. 팀끼리 대결 계산
    A - B,C,D,E,F
    B - C,D,E,F
    C - D,E,F
    ...
    => 조합 사용
3. 경기 번호 = k로 두고 dfs(0)부터 시작 (0번째 경기부터)
4. A팀과 B팀은
    1) 승/패
    2) 무/무
    3) 패/승
    3가지 경우가 가능함
    => 3가지 경우에 대해 모두 탐색
'''
import sys
from itertools import combinations

def dfs(k):
    global result

    # 총 15번의 경기가 끝났다면, 제대로 결과가 나왔는지 확인
    if k==15:
        for i in range(6):
            if not team[i]['win']==0: return
            if not team[i]['draw'] == 0: return
            if not team[i]['lose'] == 0: return
        result=1
        return

    # k번째 경기 수행
    # 1. '팀1=승, 팀2=패'인 경우
    if team[game[k][0]]['win'] and team[game[k][1]]['lose']:
        team[game[k][0]]['win']-=1
        team[game[k][1]]['lose']-=1
        # 다음 경기 수행
        dfs(k+1)
        team[game[k][0]]['win']+= 1
        team[game[k][1]]['lose']+= 1
    # 2. '팀1=무, 팀2=무'인 경우
    if team[game[k][0]]['draw'] and team[game[k][1]]['draw']:
        team[game[k][0]]['draw'] -= 1
        team[game[k][1]]['draw'] -= 1
        dfs(k + 1)
        team[game[k][0]]['draw'] += 1
        team[game[k][1]]['draw'] += 1
    # 3. '팀1=패, 팀2=승'인 경우
    if team[game[k][0]]['lose'] and team[game[k][1]]['win']:
        team[game[k][0]]['lose'] -= 1
        team[game[k][1]]['win'] -= 1
        dfs(k + 1)
        team[game[k][0]]['lose'] += 1
        team[game[k][1]]['win'] += 1

# 입력받은 데이터를 리스트로 만들기
def makeTeam(data):
    arr =[]
    for i in range(0,18,3):
        arr.append({
            'win':data[i],
            'draw':data[i+1],
            'lose':data[i+2]
        })

    return arr

# 조합으로 모든 팀과 팀 사이의 경기 구하기
game = list(combinations(range(6),2))
for _ in range(4):
    team = makeTeam(list(map(int,sys.stdin.readline().split())))
    result = 0
    dfs(0)
    print(result,end=' ')