# 이진 변환 반복하기
# s가 1이 될때까지 변환하며 a의 횟수를 셈
# bin함수를 통해 10진수를 2진수로 변환함
def solution(s):
    a, b = 0, 0
    while s != '1':
        a += 1
        num = s.count('1')
        b += len(s) - num
        s = bin(num)[2:]
    return [a, b]
