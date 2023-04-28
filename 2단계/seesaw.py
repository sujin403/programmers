
from collections import defaultdict

# 앞에서 중복되는 만큼 더해줌
def solution(weights):
    answer = 0
    # int가 아닐경우에는 answer에 추가하지 않음
    info = defaultdict(int)
    
    #info dictionary 값이 각 배수에 해당하면 answer에 더해줌 
    for w in weights:
        # 값이 중복되는 경우
        answer += info[w]
        # 2배수 3배수 조합으로 같은 값이 될 때 그 수만큼 answer에 더함
        answer += info[(w * 2) / 3] + info[(w * 3) / 2]
        # 4배수 3배수 조합으로 같은 값이 될 때
        answer += info[(w * 3) / 4] + info[(w * 4) / 3]
        # 2배수 4배수 조합으로 같은 값이 될 때 
        answer += info[(w * 4) / 2] + info[(w * 2) / 4]
        info[w] += 1
    return answer