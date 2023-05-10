
def solution(storey):
    answer = 0
    #자리 수 별로 리스트에 담음
    sl = list(map(int,list(str(storey))))
    sl.reverse() 
    for i in range(len(sl)):
        # 마지막수
        if i == len(sl) -1 :
            if sl[i] > 5 :
                answer += (10 - sl[i]) + 1
            else :
                 answer += sl[i]
                    
        # 자리의 수가 5보다 큰 경우 10에서 뺀 값을 answer에 더해줌
        # 자리 수가 5이면서 다음자리의 수가 5이상인 경우에도 10에서 뺀 값을 aswer에 더해줌
        elif sl[i] > 5 or (sl[i] == 5 and sl[i+1] >= 5) :
            answer += (10 - sl[i])
            sl[i+1] += 1 #10에서 빼기위 다음 자리수에 10을 더해줘야함
        #5보다 작은 경우는 숫자를 answer에 더해줌
        else : 
            answer += sl[i]
        print(sl)
    return answer