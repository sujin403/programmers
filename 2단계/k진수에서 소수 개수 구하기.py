# k�������� �Ҽ����� ���ϱ�
# �Ҽ� �Ǻ�
# sosu �� ���� �Ҽ����� �Ǻ��ϰ� answer�� ���� ������
# n%k�� ���� �ڸ����� ���ϰ� �κм����� ����� �Ҽ����� �Ǻ��Ѵ�
def sosu(n):
    if n == 1:
        return False
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0:
            return False
    return True


def solution(n, k):
    answer, v, tmp = 0, ["0"], ""

    while n > 0:
        v.append(str(n % k))
        n = n // k

    for i in range(len(v) - 1, -1, -1):
        if v[i] != "0":
            tmp += v[i]
        elif v[i] == "0":
            if tmp and sosu(int(tmp)):
                answer += 1
            tmp = ""
    return answer