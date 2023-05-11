# elements를 누적합으로 계산하여 연산 속도를 낮췄다.
# 원형이기 때문에 elements에 2를 곱해준다.
# set을 사용해 중복값을 제거했다.

def solution(elements):
    answer = set()
    N = len(elements)
    elements = 2 * elements
    for limit in range(1, N+1):
        for i in range(N):
            answer.add(sum(elements[i:i+limit]))
    return len(answer)