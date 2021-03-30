#후보 추천하기
import sys

#2차시도
def isInPicture(picture,s):
    for i in picture:   #사진틀에 이미 있는 학생이 추천됐으면 true
        if i[2]==s:
            return True
    return False    #아니면 false

n=int(sys.stdin.readline().strip())
m=int(sys.stdin.readline().strip())
picture=[]    #사진틀에 게시 된 (추천수, 몇번째인지, 학생번호)
vote=list(map(int,sys.stdin.readline().split()))
for i in range(m):
    if isInPicture(picture,vote[i]):    #사진틀에 있는 학생이 추천됐으면
        for idx,p in enumerate(picture):
            if p[2]==vote[i]:
                picture[idx][0]+=1  #추천수+1
                break
    else:   #사진틀에 없는 학생이 추천 됨
        if len(picture)<n:  #사진틀에 자리가 남았으면 빈자리에 사진 올림
            picture.append([1,i,vote[i]])
        else:   #사진틀에 자리가 없을 때
            picture[0]=[1,i,vote[i]]
    picture.sort(key=lambda x:(x[0],x[1]))
picture.sort(key=lambda x:x[2])
for i in range(len(picture)):
    print(picture[i][2],end=' ')


#1차 시도
'''
n=int(sys.stdin.readline().strip())
m=int(sys.stdin.readline().strip())
picture=[[-1,-1,-1]]+[[0,0,0] for _ in range(n)]    #사진틀에 게시 된 (학생 번호, 추천 수, 몇 번 째)
vote=[0]+list(map(int,sys.stdin.readline().split()))
for i in range(1,m+1):
    con=False
    for j in range(1,n+1):
        if vote[i]==picture[j][0]:  #이미 사진 게시 된 학생이 추천 됐으면 추천 수 +1
            picture[j][1]+=1
            picture[j][2]=i
            con=True
            break
    if con:
        continue
    if [0,0,0] in picture:    #비어있는 사진틀이 있을때 추천 된 학생 게시
        for j in range(1,n+1):
            if picture[j][0] == 0:
                picture[j]=[vote[i],1,i]  #(학생 번호, 추천 수, 몇 번 째)
                #print("picture111:::", picture)
                break
    else:   #사진틀이 꽉 차 있을 때
        picture.sort(key=lambda x:(x[1],x[2])) #추천 순,오래 된 순대로 sort
        #print("picture222:::",picture)
        picture.pop(1)  #사진 삭제
        picture.append([vote[i],1,i])   #새로운 학생 사진 게시
picture.sort(key=lambda x:x[0])
for i in range(1,n+1):
    if picture[i][0]!=0:
        print(picture[i][0],end=' ')
'''