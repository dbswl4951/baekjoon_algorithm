def solution(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        skill_list = list(skill)
        for s in skills:            # for-else 구문
            if s in skill_list:
                if s != skill_list.pop(0):
                    break
        else:           # for문에서 break가 발생하지 않았을 때 동작
            answer += 1
    return answer