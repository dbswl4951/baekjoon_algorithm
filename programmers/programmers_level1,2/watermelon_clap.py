def solution(n):
    list=[]
    for i in range(1,n+1):
        if(i%2==0):
            list.append('박')
        else:
            list.append('수')
    return ''.join(list)