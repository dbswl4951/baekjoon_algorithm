def game(idx, nations_score, probability):
    print("idx,probability : ",idx,probability)
    print("nations_score:",nations_score)
    # 모든 매치가 끝났을 경우
    if idx == 6:
        # value로 sort
        sorted_score = sorted(list(nations_score.items()), key=lambda x: x[1], reverse=True)
        print("sorted_score:",sorted_score)

        # 동점 4명
        if sorted_score[0][1] == sorted_score[1][1] == sorted_score[2][1] == sorted_score[3][1]:
            for i in range(4):
                nations_probability[sorted_score[i][0]] += probability * 1 / 2  # 4팀중 2팀
            print("probability===",nations_probability)
            return
        # 동점 3명
        elif sorted_score[0][1] > sorted_score[1][1] == sorted_score[2][1] == sorted_score[3][1]:
            nations_probability[sorted_score[0][0]] += probability
            for i in range(1, 4):
                nations_probability[sorted_score[i][0]] += probability * 1 / 3  # 3팀중 1팀
            print("probability===", nations_probability)
            return
        elif sorted_score[0][1] == sorted_score[1][1] == sorted_score[2][1]:
            for i in range(3):
                nations_probability[sorted_score[i][0]] += probability * 2 / 3  # 3팀중 2팀
            print("probability===", nations_probability)
            return
        # 동점 2명
        elif sorted_score[0][1] > sorted_score[1][1] == sorted_score[2][1]:
            nations_probability[sorted_score[0][0]] += probability

            for i in range(1, 3):
                nations_probability[sorted_score[i][0]] += probability * 1 / 2  # 2팀중 1팀
            print("probability===", nations_probability)
            return
        # 동점자 없음
        else:
            for i in range(2):
                nations_probability[sorted_score[i][0]] += probability  # 상위 2팀
            print("probability===", nations_probability)
            return

    # A 승
    nations_score[data[idx][0]] += 3
    print("idx,probability : ", idx, probability)
    print('A팀 '+data[idx][0]+" 승 !")
    game(idx + 1, nations_score, probability * float(data[idx][2]))
    nations_score[data[idx][0]] -= 3

    # 무승부
    print("idx,probability : ", idx, probability)
    print("무승부!")
    nations_score[data[idx][0]] += 1
    nations_score[data[idx][1]] += 1
    game(idx + 1, nations_score, probability * float(data[idx][3]))
    nations_score[data[idx][0]] -= 1
    nations_score[data[idx][1]] -= 1

    # B 승
    print("idx,probability : ", idx, probability)
    print('B팀 '+data[idx][1]+" 승 !")
    nations_score[data[idx][1]] += 3
    game(idx + 1, nations_score, probability * float(data[idx][4]))
    nations_score[data[idx][1]] -= 3


if __name__ == "__main__":

    nations = input().split()
    nations_score = {}
    nations_probability = {}
    data = []

    for key in nations:
        nations_score[key], nations_probability[key] = 0, 0

    for _ in range(6):
        temp = list(input().split())
        data.append(temp)
    print("nations_score:",nations_score)
    print("data:",data)

    game(0, nations_score, 1)

    for key in nations:
        print(nations_probability[key])