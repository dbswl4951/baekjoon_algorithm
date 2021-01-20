def solution(numbers):
    answer = []
    for i in range(len(numbers)-1):
        for j in range(len(numbers)-1):
            if(i!=j+1):
                sum=numbers[i]+numbers[j+1]
                if(sum not in answer):
                    answer.append(sum)
    answer.sort()
    return answer