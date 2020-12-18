#잃어버린 괄호
'''
1. 앞부터 시작. -A+B+.. 형태를 찾음.
2. -(A+B+...)형식으로 만듦
'''

sum=0
min_sum=0
m_list = input().split('-')

if '+' in m_list[0]:
    f_list = m_list[0].split('+')
    for i in f_list:
        min_sum+=int(i)
elif m_list[0]!='':
    min_sum+=int(m_list[0])

for m in m_list[1:]:
    if '+' in m:
        f_list = m.split('+')
        for f in f_list:
            sum += int(f)
        min_sum -= int(sum)
    else:
        min_sum-=int(m)
    sum = 0
print(min_sum)