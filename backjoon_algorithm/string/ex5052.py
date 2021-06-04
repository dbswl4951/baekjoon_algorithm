#전화번호 목록
'''
Trie 알고리즘
'''
import sys

class Node:
    def __init__(self,data=None):
        self.data=data
        self.children={}    # 자식 노드 저장
        self.end=0       # 해당 문자로 끝나는 문자열이 개수

class Tree:
    def __init__(self):
        self.head=Node(None)

    # 노드 삽입
    def insert(self,data):
        # root node에서 시작
        curr=self.head

        for d in data:
            if d not in curr.children:
                curr.children[d]=Node(d)
            # 다음 노드로 이동
            curr=curr.children[d]
        # 문자열의 끝임을 알리기 위해 end 증가
        curr.end+=1

    # 겹치는 문자열 있는지 검사 (일관성 있는 목록인지)
    def search(self,data):
        # root node에서 시작
        curr=self.head

        for idx,d in enumerate(data):
            # 다음 노드가 있으면 타고 내려간다
            if d in curr.children:
                curr=curr.children[d]
            # 문자열이 끝나기 전에 겹치는 문자열이 있으면 일관성 없는 것
            if idx!=len(data)-1:
                if curr.end>0: return False
        return True

t=int(sys.stdin.readline().strip())
for _ in range(t):
    n=int(sys.stdin.readline().strip())
    numbers=[sys.stdin.readline().strip() for _ in range(n)]
    f=0
    tree=Tree()
    # 데이터 삽입
    for num in numbers:
        tree.insert(num)
    # 일관성있는 목록인지 검사
    for num in numbers:
        flag=tree.search(num)
        if not flag:
            print('NO')
            f=1
            break
    if not f: print('YES')