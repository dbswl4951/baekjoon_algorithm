def solution(s, n):
    result = ''
    asc=0
    for i in s:
        if i==' ':
            result+=' '
        else:
            asc=ord(i)+n
            if(ord(i)<=90 and asc>=91) or asc>=123:
                asc-=26
            result+=chr(asc)
    return result