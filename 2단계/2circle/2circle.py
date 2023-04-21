import math

def solution(r1, r2):
    answer = 0
    # 축위의 점
    answer += 4*(int(r2-r1) + 1)
    
    # 1면에 위치하는 원 내부의 점
    a = 1
    b = r2
    al = []
    while a <= b :
        if math.sqrt((a*a)+(b*b)) < r1 : 
            a += 1
            b = r2
        elif math.sqrt((a*a)+(b*b)) > r2 :
            b -= 1
        elif a < b:
            al.append((a,b))
            al.append((b,a))
            b -= 1
        else :
            al.append((a,b))
            al.append((b,a))
            a +=1 
            b = r2

    # 4면 위에 위치하는 점
    # set : 중복 제거
    # print(al)
    # print(set(al))
    answer += len(set(al))*4
    
    return answer
