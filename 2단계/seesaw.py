
from collections import defaultdict

# �տ��� �ߺ��Ǵ� ��ŭ ������
def solution(weights):
    answer = 0
    # int�� �ƴҰ�쿡�� answer�� �߰����� ����
    info = defaultdict(int)
    
    #info dictionary ���� �� ����� �ش��ϸ� answer�� ������ 
    for w in weights:
        # ���� �ߺ��Ǵ� ���
        answer += info[w]
        # 2��� 3��� �������� ���� ���� �� �� �� ����ŭ answer�� ����
        answer += info[(w * 2) / 3] + info[(w * 3) / 2]
        # 4��� 3��� �������� ���� ���� �� ��
        answer += info[(w * 3) / 4] + info[(w * 4) / 3]
        # 2��� 4��� �������� ���� ���� �� �� 
        answer += info[(w * 4) / 2] + info[(w * 2) / 4]
        info[w] += 1
    return answer