from collections import deque

# 30�и��� Ǯ�� �����ߴµ� ���� �ð��ʰ�����

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



# �׷��� �����ߴµ� �̹����� 1/3 �ð��ʰ�����. ������ �Ǿ���.
# ����� ���� y���� �۰�, �湮���� ���� ��쿡�� �߰���
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


#�����ڵ� 
# visited�� Ž���ϴ� �ð��� �ٿ���.
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



