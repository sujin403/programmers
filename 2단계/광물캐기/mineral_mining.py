import math
from itertools import *

def solution(picks, minerals):
    answer = [25*25]
    # stone�� ������� ���� �Ƿε�
    mine = list(map(int,[i.replace("diamond","25").replace("iron","5").replace("stone","1") for i in minerals]))

    mcl = []
    # ���� ��� �� �Ƿε�
    while 5 < len(mine) :
        m = mine[:5]
        mcl.append((sum([math.ceil(m[i]/25) for i in range(5)]),
                    sum([math.ceil(m[i]/5) for i in range(5)]),
                    sum(m)))
        mine = mine[5:]
    # ���� ����ó��
    mcl.append((sum([math.ceil(mine[i]/25) for i in range(len(mine))]),
                sum([math.ceil(mine[i]/5) for i in range(len(mine))]),
                sum(mine)))
    mcl = [list(i) for i in mcl]
    p = [0,1,2]
    # �߻��� �� �ִ� ��� ����
    if len(mcl) <=sum(picks) :
        printList = list(product(p, repeat = len(mcl)))
        printList = [list(i) for i in printList]
    else : # ��̰� ĳ���ϴ� ������ ���� ������ ���
        printList = list(product(p, repeat = sum(picks)))
        printList = [list(i) for i in printList]
    for i in range(len(printList)):
        # ������ ���� ��� ���� �������� ������ answer ����Ʈ�� �߰�
        if printList[i].count(0) <= picks[0] and printList[i].count(1) <= picks[1] and printList[i].count(2) <= picks[2] :
            cnt = 0
            for j in range(len(printList[i])) :
                cnt += mcl[j][printList[i][j]]
            answer.append(cnt)
    
    return min(answer)