# 귤고르기
# list 배열에 담았더니 런타임 에러가 발생해서 collections의 counter를 사용했다.
from collections import  Counter

def solution(k, tangerine):
    answer = 0
    # tangerine_cnt : 귤의 크기 별 개수
    tangerine_cnt = Counter(tangerine)

    sorted_tangerine = []
    for i in list(tangerine_cnt) :
        sorted_tangerine.append(tangerine_cnt[i])
    
    sorted_tangerine = sorted(sorted_tangerine)
    # bucket에 몇 가지 종류의 크기가 들어갈 때 까지 
    bucket = 0
    for i in  sorted_tangerine[::-1]:
        if bucket < k:
            bucket += i
            answer += 1
        else :
            return answer
    return answer