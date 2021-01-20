def solution(board, moves):
    basket=[]       #바구니
    for i,move in enumerate(moves):
        for j in range(len(board)):     #세로로 들어감
            if(board[j][move-1]!=0):
                basket.append(board[j][move-1])
                board[j][move-1]=0
                break

    i=0
    result=0
    while i<len(basket)-1:
        if(i>=0 and basket[i]==basket[i+1]):
            del basket[i]
            del basket[i]
            result +=2
            i-=2
        i+=1
    return result