#게임 개발
'''
틀림
'''

import sys

n,m = map(int,input().split())     #n:세로, m:가로
a,b,d = map(int,input().split())    #현재위치:(a,b) , d:방향 (0:북,1:동,2:남,3:서)
gameMap=[]
count=1     #방문한 칸의 수

for i in range(n):
    gameMap.append(list(map(int,sys.stdin.readline().split())))
while True:
    if gameMap[a][b-1]==1 and gameMap[a-1][b]==1 and gameMap[a][b+1]==1 and gameMap[a+1][b]==1:
       break
    else:
        if d==0:    #북쪽을 바라보고 있고
            if gameMap[a][b-1]!=1:   #바다나 가본 곳이 아니라면
                gameMap[a][b]=1
                b-=1    #이동
                count+=1
            d=3     #서쪽 바라봄
        elif d==3:  #서쪽을 바라보고 있고
            if gameMap[a+1][b]!=1:     #바다나 가본 곳이 아니라면
                gameMap[a][b] = 1
                a+=1
                count += 1
            d=2     #남쪽 바라봄
        elif d==2:
            if gameMap[a][b+1]!=1:
                gameMap[a][b] = 1
                b+=1
                count += 1
            d=1     #동쪽 바라봄
        else:   #d=1일때
            if gameMap[a-1][b]!=1:
                gameMap[a][b] = 1
                a-=1
                count += 1
            d=0     #북쪽 바라봄
print(count)