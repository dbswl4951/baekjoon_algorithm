import math
from collections import Counter


def solution(progresses, speeds):
    answer = []
    remainList = []

    for i, progress in enumerate(progresses):
        pro = 100 - progress
        remainDays = math.ceil(pro / speeds[i])  # 반올림
        remainList.append(remainDays)

    for i in range(len(remainList) - 1):
        if remainList[i] > remainList[i + 1]:
            remainList[i + 1] = remainList[i]

    result = Counter(remainList)
    for key in result:
        answer.append(result[key])

    return answer