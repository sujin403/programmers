
from functools import cmp_to_key
import numpy as np

# 6문제 시간초과
# 근무태도, 동료평가 순으로 sort
def sort_list(x, y):
    return x[0] - y[0] if x[0] != y[0] else x[1] - y[1]


def solution(scores):
    ho = scores[0]
    ho_sum = sum(ho)
    scores.sort(key=cmp_to_key(sort_list)) #		[[1, 4], [2, 1], [2, 2], [3, 2], [3, 2]]
    answer = 1
    # 인센티브를 받는 사람 리스트
    incentive_list = []
    
    # 조건을 충족해 인센티브를 받는 사람을 리스트에 추가함
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



# 성공문제! 

from functools import cmp_to_key
import numpy as np

# 근무태도 UP 동료평가 down순으로 sort
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