
#�ڿ� �ִ� ū�� ã��
#stack�� ����� index�� for���� number�� ���� answer�� index�� �־���
def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    for i, number in enumerate(numbers) :
        while stack and number > numbers[stack[-1]]:
            answer[stack.pop()] = number
        stack.append(i)
        
    return answer