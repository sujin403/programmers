# elements�� ���������� ����Ͽ� ���� �ӵ��� �����.
# �����̱� ������ elements�� 2�� �����ش�.
# set�� ����� �ߺ����� �����ߴ�.

def solution(elements):
    answer = set()
    N = len(elements)
    elements = 2 * elements
    for limit in range(1, N+1):
        for i in range(N):
            answer.add(sum(elements[i:i+limit]))
    return len(answer)