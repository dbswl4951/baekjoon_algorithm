N = int(input())  # N개의 회의실을 부여받는다.
metting = []  # 빈 리스트를 생성한다.
for _ in range(N):
    start, end = map(int, input().split())  # 회의 시작시간과 끝나는 시간을 입력받는다.
    metting.append([start, 1])  # 시작시간에는 1과 함께
    metting.append([end, -1])  # 끝나는 시간에는 -1 과 함께 라스트에 추가해준다.

metting.sort()  # metting 리스트의 원소 [a,b] 에서 a의 오름차순으로 정렬

room = 0
metting_cnt = 0

for _, state in metting:  # metting_cnt 값은 시작시간 리스트에는 올라가고 끝나는 시간 리스트에는 내려간다.
    metting_cnt = metting_cnt + state  # metting_cnt값은 결국 0으로 돌아올 수 밖에 없다. (회의는 시작하면 무조건 끝나므로)
    room = max(metting_cnt, room)  # 이용한 회의실의 개수를 room에 업데이트해준다.

print(room)