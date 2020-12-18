#단어 수학
'''
<답안 알고리즘>
1. 입력받은 각 단어들이 위치한 자릿수를 각 알파벳마다 기록
 ex) ABC = A*100 + B*10 + C*1 => alphabet[A] = 100, alphabet[B] = 10, alphabet[C] = 1
 만약 'ABC + BCA'를 한다면 ::
 alphabet[A] = 101
 alphabet[B] = 110
 alphabet[C] = 11
2. 이 값들을 내림차순으로 정렬
3. 큰 값부터 작은 값으로 9부터 0까지 맵핑
 따라서 'ABC + BCA'의 값은 ::: 9*110 + 8*101 + 7*11 = 1875

=> 가장 큰 자릿수들에 위치한 알파벳부터 차례대로 9부터 맵핑시켜주는 그리디 방식
'''

n=int(input())
#ord() : 문자 -> 아스키코드 ('A'=65)
word = [list(map(lambda x: ord(x)-65, input())) for _ in range(n)]
alpha = [0] * 26

for i in range(n):
    j=0
    for w in word[i][::-1]:
        alpha[w]+=(10**j)   #십의 자리수부터 10씩 곱해 줘서 더함
        j+=1
alpha.sort(reverse=True)    #큰 수부터 정렬
result,t =0,9
print(alpha)
for i in range(26):     #알파벳 수=26
    if alpha[i]==0:
        break
    result+=(t*alpha[i])    #가장 큰 자리수부터 t=9 부터(8,7..) 매핑
    t-=1
print(result)
