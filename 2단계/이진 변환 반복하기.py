# ���� ��ȯ �ݺ��ϱ�
# s�� 1�� �ɶ����� ��ȯ�ϸ� a�� Ƚ���� ��
# bin�Լ��� ���� 10������ 2������ ��ȯ��
def solution(s):
    a, b = 0, 0
    while s != '1':
        a += 1
        num = s.count('1')
        b += len(s) - num
        s = bin(num)[2:]
    return [a, b]
