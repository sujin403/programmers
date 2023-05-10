# 택배가 모두 수거될때까지 2 * (집까지의 거리)를 오간다
# 각 d와 p에 배달과 수거 수량을 담아 반복문을 수행한다.
def solution(cap, n, deliveries, pickups):
    answer = 0
    d = 0
    p = 0
    pos = n - 1

    # 모든 집의 택바를 수거해야함
    for i in range(n - 1, -1, -1):
        d += deliveries[i]
        p += pickups[i]

        # i번째 집에 모든 택배수거가 완료될 때 까지 반복
        while d > cap or p > cap:
            d -= cap
            p -= cap
            #pos 만큼 왕복이동함
            answer += 2 * (pos + 1)
            pos = i

    if d > 0 or p > 0:
        answer += 2 * (pos + 1)

    return answer