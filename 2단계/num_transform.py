from collections import deque

# 30분만에 풀고 좋아했는데 반은 시간초과였다

def solution(x, y, n):
    answer = []
    q = deque()
    q.append((0,x))
    while q : 
        cnt, now = q.popleft()
        if now < y :
            q.append((cnt+1,(now + n)))
            q.append((cnt+1,(2 * now)))
            q.append((cnt+1,(3 * now)))
        if now == y :
            answer.append(cnt)
            
    if answer == [] :    
        return -1
    else :
        return min(answer)



# 그래서 수정했는데 이번에는 1/3 시간초과였다. 개선은 되었다.
# 계산한 값이 y보다 작고, 방문한적 없는 경우에만 추가함
from collections import deque

def solution(x, y, n):
    if x == y :
        return 0
    vsited = [x]
    q = deque()
    q.append((0,x))
    while q : 
        cnt, now = q.popleft()
        for i in (now + n,2 * now,3 * now):
            if i < y  and i not in vsited:
                q.append((cnt+1, i))
                vsited.append(i)
            if i == y :
                return cnt + 1
    return -1


#최종코드 
# visited를 탐색하는 시간을 줄였다.
from collections import deque

def solution(x, y, n):
    visited = [0]*1000001
    q = deque()
    q.append((0,x))
    visited[x] = 1
    while q : 
        cnt, now = q.popleft()
        if now == y :
            return cnt
        for i in (now + n,2 * now,3 * now):
            if i <= y  and visited[i] == 0:
                q.append((cnt+1, i))
                visited[i] = 1
            
    return -1



