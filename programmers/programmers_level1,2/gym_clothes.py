def solution(n, lost, reserve):
    answer = 0
    students = [1] * n
    for i, en in enumerate(reserve):
        students[en - 1] += 1
    for i, en in enumerate(lost):
        students[en - 1] -= 1

    for i in range(len(students) - 1):
        if (students[i] == 2 and students[i + 1] == 0):
            students[i] = 1
            students[i + 1] = 1
        if (students[i] == 0 and students[i + 1] == 2):
            students[i] = 1
            students[i + 1] = 1

    for i in range(len(students)):
        if (students[i] != 0):
            answer += 1

    return answer