
#뒤에 있는 큰수 찾기
#stack에 저장된 index와 for문의 number를 비교해 answer의 index에 넣어줌
def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    for i, number in enumerate(numbers) :
        while stack and number > numbers[stack[-1]]:
            answer[stack.pop()] = number
        stack.append(i)
        
    return answer