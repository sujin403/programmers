
# �޽� ������ ���� �� ���밪�� answer�� ��
# 50% �ð��ʰ�
def solution(sequence):
    answer = 0
    se = []
    p = 1
    for i in sequence :
        se.append(i * p)
        p *= -1
    
    for i in range(len(sequence)) :
        c = i
        while c <= len(sequence) :
            s = sum(se[i:c])
            c += 1
            if max(s,-s) > answer:
                answer = max(s,-s)
    return answer


# �������� �ִ񰪰� �ּڰ� ����

def solution(sequence):
    answer = 0
    # se ������ sequence*pulse������ �������� ����
    se = []
    p = 1
    for i in range(len(sequence)) :
        if i == 0 :
            se.append(sequence[i])
        else : 
            se.append(se[i-1]+(sequence[i] * p))
        p *= -1
    # se������ �ִ񰪿��� �ּҰ��� �� ���� ���ӵ� �κм����� �ִ밪��
    # ������ ���� �ִ��� �� ���� ����
    return max(max(se),-min(se),max(se) - min(se))