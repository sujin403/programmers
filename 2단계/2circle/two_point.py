from math import sqrt

# �ᱹ ������ ��
def solution(r1, r2):
    quar = 0
    # �鿡 ��ġ�ϴ� ����
    for i in range(0, r1):
        quar += int(sqrt(r2**2 - i**2)) - int(sqrt(r1**2 - i**2 - 1))

    #���� ��ġ�ϴ� �� ã��
    for i in range(r1, r2):
        quar += int(sqrt(r2**2 - i**2))

    # 4�и��� �����̱⿡ quar * 4
    return quar * 4