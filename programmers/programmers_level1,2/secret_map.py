def solution(n, arr1, arr2):
    map=[]
    for ar1,ar2 in zip(arr1,arr2):
        arr = (str(bin(ar1 | ar2)[2:]).zfill(n))      # 2진수로 변경
        map.append(arr.replace("1","#").replace("0"," "))
    return map