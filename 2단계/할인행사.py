
# �������
# 10�ϰ� ���ϴ� ��ǰ�� ������ŭ ������ �� �ִ��� ���ϴ� ����
def solution(want, number, discount):
    answer = 0
    for i in range(len(discount)) :
        # 10�ϰ������� ��� ���ϴ� ������ ��
        d10 = discount[i:i + 10]
        a = 0
        for j in range(len(want)) :
            if d10.count(want[j]) < number[j] :
                a = 1
                break
        if a == 0 :
            answer +=1
    return answer