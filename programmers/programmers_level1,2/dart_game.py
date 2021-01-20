def solution(dartResult):
    score = []
    n = ''

    for i in dartResult:
        if i.isnumeric():
            n += i
        else:
            if i == 'S':
                score.append(int(n))
            elif i == 'D':
                score.append(int(n) ** 2)
            elif i == 'T':
                score.append(int(n) ** 3)
            elif i == '#':
                score[-1] *= -1
            elif i == '*':
                if (len(score) > 1):
                    score[-2] *= 2
                score[-1] *= 2
            n = ''
    return sum(score)