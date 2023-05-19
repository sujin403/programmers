# 쿼드압축 후 개수 세기
# 재귀함수를 사용했다
# 배열에 최종적으로 남는 0의 개수와 1의 개수를 배열에 담았다
def solution(arr):
    global answer
    answer = [0, 0]
    quad(arr, answer, len(arr))
    return answer

def quad(arr, s, n):
    x, y, tg = s[0], s[1], arr[s[0]][s[1]]
    for i in range(n):
        for j in range(n):
            if arr[x+i][y+j] != tg:
                quad(arr, [x, y], n//2)
                quad(arr, [x, y+n//2], n//2)
                quad(arr, [x+n//2, y], n//2)
                quad(arr, [x+n//2, y+n//2], n//2)
                return
    answer[tg] += 1
