
# bfs 알고리즘을 이용하여 노드간의 간선정보를 토대로 graph를 만들어 실행
# 방문한 node을 True, 끊어진 노드를 False로 표현한 후 count을 하여 서로 연결된 node의 개수를 구함
from collections import deque

def make_graph(wires, n):
    cnt = 0
    graph = []

    for i in range(n + 1):
        node = []
        graph.append(node)

    for i in range(len(wires)):
        graph[wires[i][0]].append(wires[i][1])
        graph[wires[i][1]].append(wires[i][0])

    return graph

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    list = []

    while queue:
        v = queue.popleft()
        list.append(v)

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

    return list

def solution(n, wires):
    answer = 100
    wires = sorted(wires, key = lambda x : (x[0], x[1]))

    # i번째 간선을 잘랐을 때
    for i in range(len(wires)):
        wire = wires[:i]+wires[i+1:]

        graph = make_graph(wire, n)

        # 탐색의 시작노드
        node = []
        node = set(node)
        for j in range(1, n + 1):
            visited = [False] * (n + 1)
            bfs(graph, j, visited)
            node.add(visited.count(True))

        if max(node) - min(node) < answer:
            answer = max(node) - min(node)

    return answer