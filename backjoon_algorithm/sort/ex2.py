#성적이 낮은 순서로 학생 출력하기

n = int(input())
grade=[]
for i in range(n):
    data=input().split()
    grade.append((data[0],int(data[1])))
grade.sort(key=lambda x:x[1])
for i in range(n):
    print(grade[i][0],end=' ')