# heap 자료 구조는 자동으로 작은 순서로 sort되면서, 시간이 짧게 걸린다.
from heapq import heappush, heappop

def solution(n, k, enemy):
    #무적권으로 모든 라운드를 막는경우
    if k >= len(enemy) :
        return len(enemy) 
    hq = []
    for round, monster in enumerate(enemy):
        heappush(hq, monster)
        # heap 리스트의 길이가 k개 이상이 되면 n에서 빼기 시작함
        # heappop은 최소값부터 빠지고 len(hq) > K 일때부터 heappop 하므로 n<0일 때 남은 hq리스트 값은 무적권을 사용했다고 보면 됨
        if len(hq) > k:
            n -= heappop(hq)
        if n < 0:
            return round
        
    return len(enemy) 