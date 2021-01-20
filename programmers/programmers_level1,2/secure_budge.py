def solution(d, budget):
    result = 0
    sum = 0
    i = 0
    d.sort()

    while i<len(d):
        if (sum + d[i]) <= budget:
            sum += d[i]
            result += 1
        i += 1
    return result