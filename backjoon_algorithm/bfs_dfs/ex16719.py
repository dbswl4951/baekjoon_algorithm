#ZOAC
'''
- start : 초기 배열의 몇번째 index에서 해당 배열이 시작되는지

1. 배열의 가장 작은 알파벳, index 찾기
2. 알맞는 result index에 넣고 출력
3. 해당 index의 뒤부터 다시 탐색 후, index 앞 탐색
'''
import sys

def dfs(arr,start):
    if not arr: return

    alpa = min(arr)
    idx = arr.index(alpa)
    result[start+idx]=alpa
    print(''.join(result))

    dfs(arr[idx+1:],start+idx+1)
    dfs(arr[:idx],start)

arr = sys.stdin.readline().strip()
result = ['']*len(arr)
dfs(arr,0)