# success
# while문과 answer값을 활용해 불필요한 리스트를 줄였음
def solution(order):
    answer = 0
    sub_belt = []
    item = 1
    while item != len(order) + 1 :
        sub_belt.append(item) 
        while sub_belt and sub_belt[-1] == order[answer] :
            answer += 1 
            sub_belt.pop()
        item += 1
    return answer



# 시간초과
# 자세하게 조건을 설정한 것 같다..
def solution(order):
    answer = 0
    sub_belt = []
    item = [i + 1 for i in range(len(order))]
    while order :
        if item == [] :
            if sub_belt[-1] == order[0] :
                sub_belt.pop(-1)
                order.pop(0)
                answer += 1
            elif  order[0] < sub_belt[-1]: 
                return answer
        elif order[0] == item[0] :
            answer += 1
            order.pop(0)
            item.pop(0)
        elif sub_belt :
            if sub_belt[-1] == order[0] :
                sub_belt.pop(-1)
                order.pop(0)
                answer += 1
            elif  order[0] < sub_belt[-1]: 
                return answer
            else :
                sub_belt.append(item[0])
                item.pop(0)
        else :
            sub_belt.append(item[0])
            item.pop(0)            
    return answer