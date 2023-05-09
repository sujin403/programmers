# deque�� ����� ����Ǯ��
# �������� ã��, ���������� �Ÿ��� exit������ �Ÿ��� ���� ���ϰ� ���� ���� return�Ͽ���.
from collections import deque

def solution(maps):
    direction =  ((-1,0), (1,0), (0, 1), (0, -1))
    answer = -1
    m = len(maps)
    n=len(maps[0])
    for i in range(m):
        for j in range(n):
            if maps[i][j] == 'S':
                S = (i,j)
            if maps[i][j] == 'L':
                L = (i,j)
            if maps[i][j] == 'E':
                E = (i,j)                        
    stack = deque()
    stack.append((S,0))
    visited = {S : 1}
    # �������� �Ÿ� ã��
    while stack : 
        cur, depth = stack.popleft()
        if cur == L :
            answer = depth
            break
        for a, b in direction:
            x,y = cur[0] + a , cur[1] + b
            if  x >= 0 and y >= 0 and x < m and y < n : 
                if maps[x][y] != 'X' and (x,y) not in visited :
                    stack.append(((x,y),depth + 1))
                    visited[(x,y)] = 1
    if answer == -1:
        return -1    
    
    
     # exit���� ��ã��
    answer2 = -1
    stack = deque()
    stack.append((L,0))
    visited = {L : 1}
    while stack : 
        cur, depth = stack.popleft()
        if cur == E :
            answer2 = depth
            break
        for a, b in direction:
            x,y = cur[0] + a , cur[1] + b
            if  x >= 0 and y >= 0 and x < m and y < n :
                if maps[x][y] != 'X' and (x,y) not in visited :
                    stack.append(((x,y),depth + 1))
                    visited[(x,y)] = 1
                    
    if answer2 == -1:
        return -1

    return answer + answer2
