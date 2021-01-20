def solution(arr):
    arrList=[]
    for i in range(len(arr)-1):
        if(arr[i]!=arr[i+1]):
            arrList.append(arr[i])
    arrList.append(arr[-1])
    return arrList