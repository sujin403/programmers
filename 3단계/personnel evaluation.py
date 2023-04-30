
from functools import cmp_to_key
import numpy as np

# 6���� �ð��ʰ�
# �ٹ��µ�, ������ ������ sort
def sort_list(x, y):
    return x[0] - y[0] if x[0] != y[0] else x[1] - y[1]


def solution(scores):
    ho = scores[0]
    ho_sum = sum(ho)
    scores.sort(key=cmp_to_key(sort_list)) #		[[1, 4], [2, 1], [2, 2], [3, 2], [3, 2]]
    answer = 1
    # �μ�Ƽ�긦 �޴� ��� ����Ʈ
    incentive_list = []
    
    # ������ ������ �μ�Ƽ�긦 �޴� ����� ����Ʈ�� �߰���
    for score_s in scores:
        for score_b in scores[::-1] : 
            if score_b[0] > score_s[0] and score_b[1] > score_s[1] :
                break
            if score_s == score_b:
                incentive_list.append(score_s)
                if sum(score_s) > ho_sum:
                    answer += 1
                break
    if ho not in incentive_list :
        return -1

    return answer



# ��������! 

from functools import cmp_to_key
import numpy as np

# �ٹ��µ� UP ������ down������ sort
def sort_list(x, y):
    return x[0] - y[0] if x[0] != y[0] else y[1] - x[1] 


def solution(scores):
    target = scores[0]
    target_score = sum(target)
    scores.sort(key=cmp_to_key(sort_list)) #		[[1, 4], [2, 1], [2, 2], [3, 2], [3, 2]]
    answer = 1
    threshold = 0
    for score in scores[::-1]:
        if target[0] < score[0] and target[1] < score[1]:
            return -1
        if threshold <= score[1]:
            if target_score < score[0] + score[1]:
                answer += 1
            threshold = score[1]
    return answer