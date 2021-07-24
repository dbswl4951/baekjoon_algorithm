#개미굴
'''
Trie 알고리즘
'''
import sys

class Node:
    def __init__(self,data):
        self.data=data
        self.children={}
        self.visited=0  # 방문(출력) 체크

class Trie:
    def __init__(self):
        # 루트 노드는 빈 노드로 설정
        self.head=Node(None)

    # 문자열 삽입
    def insert(self,data):
        # 루트 노트부터 검사 시작
        curr=self.head
        for d in data:
            # 현재 문자가 자식노드가 아니라면 노드 생성 후, 추가
            if d not in curr.children:
                curr.children[d]=Node(d)
            # 자식 노드로 이동
            curr=curr.children[d]

    # data로 이어진 문자열 찾기
    def search(self,data):
        cnt=0
        curr = self.head
        for idx,d in enumerate(data):
            # 자식 노드로 타고 내려가기
            if d in curr.children:
                curr=curr.children[d]
            # 아직 방문(출력)하지 않은 노드라면 출력
            if curr.visited==0:
                print('-' * cnt, end='')
                print(d)
                curr.visited=1
            cnt += 2

n=int(sys.stdin.readline().strip())
string=[]
result=[]
trie=Trie()
for _ in range(n):
    temp=list(sys.stdin.readline().split())
    temp=temp[1:]
    trie.insert(temp)
    if temp not in string:
        string.append(temp)
string.sort()
for s in string:
    trie.search(s)