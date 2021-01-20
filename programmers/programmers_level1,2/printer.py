def solution(priorities, location):
    loc = [i for i in range(len(priorities))]  # 현재 대기목록에 있는 문서의 순서 [0,1,2,...]
    final_loc = []  # 출력 순서

    while len(priorities) != 0:
        if priorities[0] == max(priorities):  # 우선 순위가 가장 높다면
            final_loc.append(loc.pop(0))  # 출력
            priorities.pop(0)  # 대기목록에서 삭제
        else:
            priorities.append(priorities.pop(0))
            loc.append(loc.pop(0))
    return final_loc.index(location) + 1