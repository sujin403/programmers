

# 아이디어 : x 좌표를 순서대로 돌면서 y좌표 최댓값을 answer에 더해줌
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