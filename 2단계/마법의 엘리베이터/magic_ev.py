
def solution(storey):
    answer = 0
    #�ڸ� �� ���� ����Ʈ�� ����
    sl = list(map(int,list(str(storey))))
    sl.reverse() 
    for i in range(len(sl)):
        # ��������
        if i == len(sl) -1 :
            if sl[i] > 5 :
                answer += (10 - sl[i]) + 1
            else :
                 answer += sl[i]
                    
        # �ڸ��� ���� 5���� ū ��� 10���� �� ���� answer�� ������
        # �ڸ� ���� 5�̸鼭 �����ڸ��� ���� 5�̻��� ��쿡�� 10���� �� ���� aswer�� ������
        elif sl[i] > 5 or (sl[i] == 5 and sl[i+1] >= 5) :
            answer += (10 - sl[i])
            sl[i+1] += 1 #10���� ������ ���� �ڸ����� 10�� ���������
        #5���� ���� ���� ���ڸ� answer�� ������
        else : 
            answer += sl[i]
        print(sl)
    return answer