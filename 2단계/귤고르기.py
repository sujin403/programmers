# �ְ���
# list �迭�� ��Ҵ��� ��Ÿ�� ������ �߻��ؼ� collections�� counter�� ����ߴ�.
from collections import  Counter

def solution(k, tangerine):
    answer = 0
    # tangerine_cnt : ���� ũ�� �� ����
    tangerine_cnt = Counter(tangerine)

    sorted_tangerine = []
    for i in list(tangerine_cnt) :
        sorted_tangerine.append(tangerine_cnt[i])
    
    sorted_tangerine = sorted(sorted_tangerine)
    # bucket�� �� ���� ������ ũ�Ⱑ �� �� ���� 
    bucket = 0
    for i in  sorted_tangerine[::-1]:
        if bucket < k:
            bucket += i
            answer += 1
        else :
            return answer
    return answer