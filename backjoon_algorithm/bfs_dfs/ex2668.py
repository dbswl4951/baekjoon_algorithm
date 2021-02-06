#숫자 고르기
import sys

n=int(sys.stdin.readline().strip())
dic={}
for i in range(n):
    dic[i+1]=int(sys.stdin.readline().strip())
while True:
    valueSet=set(dic.values())
    dic={key:value for key,value in dic.items() if key in valueSet}
    if valueSet==set(dic.values()): break
print(len(dic))
for key in dic.keys():
    print(key)