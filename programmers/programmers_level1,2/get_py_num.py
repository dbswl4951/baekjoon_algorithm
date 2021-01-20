def solution(s):
    pList = []
    yList = []
    if 'p' not in s and 'P' not in s and 'y' not in s and 'Y' not in s:
        return True

    for i in range(len(s)):
        if (s[i] == 'p' or s[i] == 'P'):
            pList.append(s[i])
        elif (s[i] == 'y' or s[i] == 'Y'):
            yList.append(s[i])

    if (len(pList) == len(yList)):
        return True
    return False