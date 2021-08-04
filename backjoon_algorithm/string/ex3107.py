#IPv6
import sys

ipv6=list(sys.stdin.readline().strip().split(':'))
# 맨 앞에 '::'가 나왔을 때 처리
if not ipv6[0]:
    if len(set(ipv6))==1: ipv6=ipv6[2:]
    else: ipv6=ipv6[1:]
# 맨 뒤에 '::'가 나왔을 때 처리
elif not ipv6[-1]:
    if len(set(ipv6))==1: ipv6=ipv6[:-1]
    else: ipv6=ipv6[:-1]

result=''
for ip in ipv6:
    if not ip:
        repeat=8-(len(ipv6)-1)
        result+='0000:'*repeat
    elif len(ip)!=4:
        result+=('0'*(4-len(ip))+ip+':')
    else: result+=ip+':'
result=result[:-1]
print(result)