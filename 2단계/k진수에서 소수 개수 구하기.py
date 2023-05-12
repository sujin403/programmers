# k진수에서 소수개수 구하기
# 소수 판별
# sosu 를 통해 소수인지 판별하고 answer에 답을 더해줌
# n%k를 통해 자리수를 구하고 부분수열을 만들어 소수인지 판별한다
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