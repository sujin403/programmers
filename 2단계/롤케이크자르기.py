# ������ũ �ڸ���
# �ð��ʰ�
# len�� �� for������ ����ؼ� �ð��ʰ��� �߻��ߴ�

def solution(topping):
    answer = 0
    for index in range(len(topping)) :
        if len(set(topping[:index])) == len(set(topping[index:])) :
            answer += 1      
    return answer


# len�� ������� �ʱ� ���� counter�� ����ߴ�
# bro ch�� counter�� set���� ������ �ð��� �ٿ���.

from collections import Counter

def solution(topping):
    answer = 0
    bro = Counter(topping)
    ch = set()
    for index in topping :
        bro[index] -= 1
        if bro[index] == 0 :
            del bro[index]
        ch.add(index)
        
        if len(bro) == len(ch) :
            answer += 1   
        elif answer > 0 :
            break
    return answer