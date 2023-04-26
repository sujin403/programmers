
from collections import deque

def solution(maps):

    answer = []
    #방문기록
    visited = [[0]*len(maps[0]) for _ in range(len(maps))]

    drt = [[0,1],[0,-1],[1,0],[-1,0]]
    
    #bfs
    for i in range(len(maps)) :
        for j in range(len(maps[0])) :
            # X가 아니고 방문기록이 없으면 해당 무인도의 체류가능 기간을 구함
            if maps[i][j] !="X" and visited[i][j] == 0 :
                way = deque([(i,j)])
                # way.append((i,j))
                visited[i][j] = 1
                cost = int(maps[i][j])
                # way로 이동하며 체류가능 기간을 COST에 더함
                while way :
                    wx,wy = way.popleft()
                    for d in drt :
                        dx = wx + d[0]
                        dy = wy + d[1]
                        if len(maps) > dx >= 0 and len(maps[0]) > dy >= 0 and visited[dx][dy] == 0 and maps[dx][dy] != "X" :
                            way.append((dx,dy))
                            cost += int(maps[dx][dy])
                            visited[dx][dy] = 1
                answer.append(cost)
                
                
    # 체류 가능한 answer가 없으면 -1을 return
    return sorted(answer) if answer else [-1]
