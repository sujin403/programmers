import math
from itertools import *

def solution(picks, minerals):
    answer = [25*25]
    # stone을 사용했을 때의 피로도
    mine = list(map(int,[i.replace("diamond","25").replace("iron","5").replace("stone","1") for i in minerals]))

    mcl = []
    # 도구 사용 별 피로도
    while 5 < len(mine) :
        m = mine[:5]
        mcl.append((sum([math.ceil(m[i]/25) for i in range(5)]),
                    sum([math.ceil(m[i]/5) for i in range(5)]),
                    sum(m)))
        mine = mine[5:]
    # 남은 광물처리
    mcl.append((sum([math.ceil(mine[i]/25) for i in range(len(mine))]),
                sum([math.ceil(mine[i]/5) for i in range(len(mine))]),
                sum(mine)))
    mcl = [list(i) for i in mcl]
    p = [0,1,2]
    # 발생할 수 있는 모든 순서
    if len(mcl) <=sum(picks) :
        printList = list(product(p, repeat = len(mcl)))
        printList = [list(i) for i in printList]
    else : # 곡괭이가 캐야하는 광물에 비해 부족한 경우
        printList = list(product(p, repeat = sum(picks)))
        printList = [list(i) for i in printList]
    for i in range(len(printList)):
        # 순서에 따라서 곡괭이 수가 부족하지 않으면 answer 리스트에 추가
        if printList[i].count(0) <= picks[0] and printList[i].count(1) <= picks[1] and printList[i].count(2) <= picks[2] :
            cnt = 0
            for j in range(len(printList[i])) :
                cnt += mcl[j][printList[i][j]]
            answer.append(cnt)
    
    return min(answer)