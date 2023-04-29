
# 할인행사
# 10일간 원하는 제품의 수량만큼 구매할 수 있는지 구하는 문제
def solution(want, number, discount):
    answer = 0
    for i in range(len(discount)) :
        # 10일간격으로 담아 원하는 수량과 비교
        d10 = discount[i:i + 10]
        a = 0
        for j in range(len(want)) :
            if d10.count(want[j]) < number[j] :
                a = 1
                break
        if a == 0 :
            answer +=1
    return answer