'''
owner : 고정된 길이 6
perm : 고정된 길이 3 (r,w,x,- 중), 대소문자 구별
name : 적어도 하나의 . 포함, 대소문자 구별
    . 이후는 확장자 (doc, xls, pdf)

파일 이름의 최소 길이를 구하라
없으면 NO FILES 출력
'''
def solution(S):
    sList=S.split('\n')
    for i in range(len(sList)):
        sList[i]=sList[i].lstrip()
    extension=('doc','xls','pdf')
    result=256

    for s in sList:
        owner,perms,names=s.split(' ')
        perm=perms.strip()
        name=names.split('.')
        if owner!='root': continue
        if name[-1] not in extension: continue
        if perm[1]!='-': continue
        cnt=0
        for n in name:
            cnt+=len(n)
        result=min(result,cnt+1)
    return str(result)

print(solution('root r-x delete-this.xls\n  root r-- bug-report.pdf\n  root r-- doc.xls\n  root r-- podcast.flac\n alice r-- system.xls\n  root --x invoices.pdf\n admin rwx SETUP.PY'))