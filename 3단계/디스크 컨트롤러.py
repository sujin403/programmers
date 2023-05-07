# �����ڵ�
# heap�� ����� ���� �ӵ��� �ٿ���.

from heapq import heappop, heappush

def solution(jobs):
    task = len(jobs)
    
    answer = 0
    now = 0
    #��û�ð��� ���� ����
    jobs.sort(key=lambda x: (x[0],x[1]))
    
    have_to = []
    heappush(have_to, (0, jobs.pop(0)))
    
    while have_to :
        request_time,long_time  = heappop(have_to)[1]
        
        # ��û�� ���� �� �׽�ũ�� �з����� �ʴ� ���
        if request_time > now :
            now = request_time + long_time
        else : 
            now += long_time
            
        answer += (now - request_time)
        while True :
            # ���� ������ ������ ���� ���
            if jobs and jobs[0][0] < now :
                heappush(have_to, (jobs[0][1], jobs[0]))
                jobs.pop(0)
            else : # �и� ������ ���� ��û������ ���� ���
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





# Ʋ���ڵ�
# sort���� ��û �ð��� ����ߴ��� ������ �߻��ߴ�. �׷��� ���� �ð��� �Բ� ������ֱ�� �Ͽ���.

from heapq import heappop, heappush

def solution(jobs):
    answer = 0
    now = 0
    have_to = []
    task = len(jobs)
    for i in range(task) :
        request_time, long_time = jobs[i]

        # ��û�ð����� �Ϸ���� �ɸ��� �ð�
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
        
        
    # for���� �����µ� �ؾ������� ���� ���
    if have_to :
        have_to.sort(key=lambda x: (x[1]))
        for i in range(len(have_to)) :
            answer += now - have_to[0][0] + have_to[0][1]
            now += have_to[0][1]
            have_to.pop(0)
    
    return int(answer/len(jobs))