

# ���̵�� : x ��ǥ�� ������� ���鼭 y��ǥ �ִ��� answer�� ������
import math

def solution(k, d):
    answer = 0
    y_point = (d//k)*k
    for i in range(0,d+1,k):
        x_point = i
        while math.sqrt(x_point**2 + y_point**2) > d:
            y_point -= k
        answer+= int(y_point/k) + 1
    return answer