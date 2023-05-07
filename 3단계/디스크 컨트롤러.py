# 성공코드
# heap을 사용해 연산 속도를 줄였다.

from heapq import heappop, heappush

def solution(jobs):
    task = len(jobs)
    
    answer = 0
    now = 0
    #요청시간에 따라 정렬
    jobs.sort(key=lambda x: (x[0],x[1]))
    
    have_to = []
    heappush(have_to, (0, jobs.pop(0)))
    
    while have_to :
        request_time,long_time  = heappop(have_to)[1]
        
        # 요청을 했을 때 테스크가 밀려있지 않는 경우
        if request_time > now :
            now = request_time + long_time
        else : 
            now += long_time
            
        answer += (now - request_time)
        while True :
            # 아직 업무가 끝나지 않은 경우
            if jobs and jobs[0][0] < now :
                heappush(have_to, (jobs[0][1], jobs[0]))
                jobs.pop(0)
            else : # 밀린 없무가 없고 요청업무는 남은 경우
                if jobs and len(have_to) == 0 :
                    
                    now_start = jobs[0][0]

                    while jobs :
                        job = jobs[0]

                        if job[0] != now_start :
                            break

                        heappush(have_to, (job[1], job))
                        now_start = job[0]
                        jobs.pop(0)

                break
                    
        
    return answer//task





# 틀린코드
# sort에서 요청 시간만 고려했더니 오류가 발생했다. 그래서 연산 시간도 함께 고려해주기로 하였다.

from heapq import heappop, heappush

def solution(jobs):
    answer = 0
    now = 0
    have_to = []
    task = len(jobs)
    for i in range(task) :
        request_time, long_time = jobs[i]

        # 요청시간부터 완료까지 걸리는 시간
        if now > request_time :
            have_to.append(jobs[i])
            
        elif have_to and i != task-1 :
            have_to.append(jobs[i])
            have_to.sort(key=lambda x: (x[1]))
            
            while now <jobs[i+1][0] and have_to:
                answer += now - have_to[0][0] + have_to[0][1]
                now += have_to[0][1]
                have_to.pop(0)  
                
        elif now < request_time:
            now = request_time + long_time
            answer += long_time
                
        else:
            have_to.append(jobs[i])
            have_to.sort(key=lambda x: (x[1]))
            for i in range(len(have_to)) :
                answer += now - have_to[0][0] + have_to[0][1]
                now += have_to[0][1]
                have_to.pop(0)
        
        
    # for문이 끝났는데 해야할일이 남은 경우
    if have_to :
        have_to.sort(key=lambda x: (x[1]))
        for i in range(len(have_to)) :
            answer += now - have_to[0][0] + have_to[0][1]
            now += have_to[0][1]
            have_to.pop(0)
    
    return int(answer/len(jobs))