# heap �ڷ� ������ �ڵ����� ���� ������ sort�Ǹ鼭, �ð��� ª�� �ɸ���.
from heapq import heappush, heappop

def solution(n, k, enemy):
    #���������� ��� ���带 ���°��
    if k >= len(enemy) :
        return len(enemy) 
    hq = []
    for round, monster in enumerate(enemy):
        heappush(hq, monster)
        # heap ����Ʈ�� ���̰� k�� �̻��� �Ǹ� n���� ���� ������
        # heappop�� �ּҰ����� ������ len(hq) > K �϶����� heappop �ϹǷ� n<0�� �� ���� hq����Ʈ ���� �������� ����ߴٰ� ���� ��
        if len(hq) > k:
            n -= heappop(hq)
        if n < 0:
            return round
        
    return len(enemy) 