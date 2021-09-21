import sys
from itertools import combinations

def dfs(k):
    global result

    if k==15:
        if [e for e in team[0].values()] == [0]*3:
            print('result ======== ')
            print(team[0].values())
            result=1
        return
    print('k ,game[k]================', k, game[k])

    if team[game[k][0]]['win'] and team[game[k][1]]['lose']:
        print("승패")
        team[game[k][0]]['win']-=1
        team[game[k][1]]['lose'] -= 1
        print('team : ',team)
        dfs(k+1)
        print("현재 k:",k)
        team[game[k][0]]['win'] += 1
        team[game[k][1]]['lose'] += 1
        print('team22 : ', team)
    if team[game[k][0]]['draw'] and team[game[k][1]]['draw']:
        print('비김')
        team[game[k][0]]['draw']-=1
        team[game[k][1]]['draw'] -= 1
        print('team : ', team)
        dfs(k+1)
        team[game[k][0]]['draw'] += 1
        team[game[k][1]]['draw'] += 1
        print('team22 : ', team)
    if team[game[k][0]]['lose'] and team[game[k][1]]['win']:
        print('패승')
        team[game[k][0]]['lose']-=1
        team[game[k][1]]['win'] -= 1
        print('team : ', team)
        dfs(k+1)
        print("현재 k:", k)
        team[game[k][0]]['lose'] += 1
        team[game[k][1]]['win'] += 1
        print('team22 : ', team)

def makeTeam(record):
    arr=[]
    for i in range(0,18,3):
        arr.append({
            'win':record[i],
            'draw':record[i+1],
            'lose':record[i+2]
        })
    return arr

for _ in range(4):
    team = makeTeam(list(map(int,sys.stdin.readline().split())))
    game = list(combinations(range(6),2))
    print('game', game)
    result=0
    dfs(0)
    print('---------------------------------------')
