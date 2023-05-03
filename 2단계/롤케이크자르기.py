# 롤케이크 자르기
# 시간초과
# len을 매 for문마다 사용해서 시간초과가 발생했다

def solution(topping):
    answer = 0
    for index in range(len(topping)) :
        if len(set(topping[:index])) == len(set(topping[index:])) :
            answer += 1      
    return answer


# len을 사용하지 않기 위해 counter를 사용했다
# bro ch를 counter와 set으로 설정해 시간을 줄였다.

from collections import Counter

def solution(topping):
    answer = 0
    bro = Counter(topping)
    ch = set()
    for index in topping :
        bro[index] -= 1
        if bro[index] == 0 :
            del bro[index]
        ch.add(index)
        
        if len(bro) == len(ch) :
            answer += 1   
        elif answer > 0 :
            break
    return answer