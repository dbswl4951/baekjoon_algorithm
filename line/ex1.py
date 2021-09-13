def solution(student, k):
    left,right=0,0
    cnt,result=0,0
    while left<=right and right<len(student):
        print('left, right,cnt:', left, right,cnt)

        if cnt<k:
            right+=1
            if right<len(student) and student[right]==1:
                cnt+=1
        elif cnt==k:
            result+=1
            right+=1
            print("result:",result)
            if right<len(student)-1 and student[right]==1: cnt+=1
        else:
            if student[left]==1: cnt-=1
            left+=1

        if right==len(student) and left!=len(student)-1:
            left+=1
            right=left
            if student[right]==1: cnt=1
            else : cnt=0
    return result

#print(solution([0,1,0,0],1))
print(solution([0, 1, 0, 0, 1, 1, 0],2))
#print(solution([0, 1, 0],2))