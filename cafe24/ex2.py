def solution(numArr):
    subjectSum = sum(numArr)
    result1 = subjectSum/3
    result2 = ''
    if result1>=90: result2='A'
    elif result1>=80: result2='B'
    elif result1>=70: result2='C'
    elif result1>=60: result2='D'
    else: result2='F'

    return [str("{:.2f}%".format(result1)[:-1]),result2]

print(solution([100, 100, 98]))
print(solution([100, 100, 100]))