# success
# while���� answer���� Ȱ���� ���ʿ��� ����Ʈ�� �ٿ���
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



# �ð��ʰ�
# �ڼ��ϰ� ������ ������ �� ����..
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