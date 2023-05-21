# 2가지 코스요리 중 가장 많이 선택받은 메뉴를 return한다
# combination으로 조합을 만들고 counter로 조합의 개수를 센다.
# 이후 가장 많이 주문한 메뉴를 answer에 더하고 sort해서 return한다.
from itertools import combinations
from collections import Counter

def solution(orders, course):
    _list = []
    for order in orders:
        for c in course:
            _list += list(combinations(sorted(order), c))

    _dict = {k: [2] for k in course}
    for k, v in Counter([''.join(v) for v in _list]).items():
        if _dict[len(k)][0] == v:
            _dict[len(k)].append(k)
        elif _dict[len(k)][0] < v:
            _dict[len(k)] = [v, k]

    answer = []
    for v in _dict.values():
        answer += v[1:]
    return sorted(answer)