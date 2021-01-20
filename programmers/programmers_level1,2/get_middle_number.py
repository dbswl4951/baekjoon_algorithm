def solution(s):
    list=[]
    length=len(s)//2
    if ((len(s)%2)==0):       #단어의 길이가 짝수라면
        list=s[length-1:length+1]
    else:       #단어의 길이가 홀수
        list=s[length:length+1]
    answer=''.join(list)
    return answer