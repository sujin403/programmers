from math import sqrt

# 결국 답지를 봄
def solution(r1, r2):
    quar = 0
    # 면에 위치하는 점들
    for i in range(0, r1):
        quar += int(sqrt(r2**2 - i**2)) - int(sqrt(r1**2 - i**2 - 1))

    #선에 위치하는 점 찾기
    for i in range(r1, r2):
        quar += int(sqrt(r2**2 - i**2))

    # 4분면이 공통이기에 quar * 4
    return quar * 4