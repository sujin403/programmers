
# 펄스 수열을 합하 후 절대값을 answer과 비교
# 50% 시간초과
def solution(sequence):
    answer = 0
    se = []
    p = 1
    for i in sequence :
        se.append(i * p)
        p *= -1
    
    for i in range(len(sequence)) :
        c = i
        while c <= len(sequence) :
            s = sum(se[i:c])
            c += 1
            if max(s,-s) > answer:
                answer = max(s,-s)
    return answer


# 누적합의 최댓값과 최솟값 뺄셈

def solution(sequence):
    answer = 0
    # se 수열에 sequence*pulse수열의 누적합을 생성
    se = []
    p = 1
    for i in range(len(sequence)) :
        if i == 0 :
            se.append(sequence[i])
        else : 
            se.append(se[i-1]+(sequence[i] * p))
        p *= -1
    # se수열의 최댓값에서 최소값을 뺀 값이 연속된 부분수열의 최대값임
    # 누적합 값이 최댓값이 될 수도 있음
    return max(max(se),-min(se),max(se) - min(se))