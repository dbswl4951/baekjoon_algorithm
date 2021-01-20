def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        cutArray = array[commands[i][0]-1:commands[i][1]]
        cutArray.sort()
        answer.append(cutArray[commands[i][2]-1])
    return answer