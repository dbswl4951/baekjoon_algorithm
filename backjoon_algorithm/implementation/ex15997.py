#승부 예측
'''
DFS + 브루트포스

모든 경우의 수를 돌면서 확률(probability)을 누적해서 계산한다.
모든 경기가 끝나면 구한 누적 확률을 teamProbability에 더한다

1) 한 번에 모든 경기가 일어나는 것이 아닌, 순차적으로 경기를 하는 것이므로
    모든 경우를 순서대로 계산하며 구해야 하는 것
2) 확률을 누적시켜 계산하는 것
=> 이 두가지가 떠올리기 어렵다ㅜ
'''

import sys

def dfs(idx,teamScores,probability):
    if idx==6:
        # value값을 기준으로 내림차순 정렬
        sortedScores =sorted(list(teamScores.items()), key=lambda x: x[1], reverse=True)

        # 동점 4팀
        if sortedScores[0][1]==sortedScores[1][1]==sortedScores[2][1]==sortedScores[3][1]:
            for i in range(4):
                teamProbability[sortedScores[i][0]] += probability * 1/2
            return
        # 동점 3팀
        elif sortedScores[0][1] > sortedScores[1][1]==sortedScores[2][1]==sortedScores[3][1]:
            teamProbability[sortedScores[0][0]]+=probability
            for i in range(1,4):
                teamProbability[sortedScores[i][0]] += probability * 1/3
            return
        elif sortedScores[0][1]==sortedScores[1][1]==sortedScores[2][1]:
            for i in range(3):
                teamProbability[sortedScores[i][0]] += probability * 2/3
            return
        # 동점 2팀
        elif sortedScores[0][1] > sortedScores[1][1]==sortedScores[2][1]:
            teamProbability[sortedScores[0][0]]+=probability
            for i in range(1,3):
                teamProbability[sortedScores[i][0]] += probability * 1/2
            return
        # 동점자 없음
        else:
            for i in range(2):
                teamProbability[sortedScores[i][0]] += probability
            return

    # A팀 승
    teamScores[data[idx][0]]+=3
    dfs(idx+1,teamScores,probability*float(data[idx][2]))
    teamScores[data[idx][0]]-=3

    # 무승부
    teamScores[data[idx][0]]+=1
    teamScores[data[idx][1]]+=1
    dfs(idx+1,teamScores,probability*float(data[idx][3]))
    teamScores[data[idx][0]]-=1
    teamScores[data[idx][1]]-=1

    # B팀 승
    teamScores[data[idx][1]] += 3
    dfs(idx + 1, teamScores, probability * float(data[idx][4]))
    teamScores[data[idx][1]] -= 3

teams = sys.stdin.readline().split()
teamScores,teamProbability={},{}
data=[]
for t in teams:
    teamScores[t], teamProbability[t] = 0, 0
for _ in range(6):
    data.append(list(sys.stdin.readline().split()))

dfs(0,teamScores,1)
for t in teams: print('%0.10f'%float(teamProbability[t]))