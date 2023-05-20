from heapq import heappush, heappop

# make_matrix를 통해 회전하는 매트릭스를 만듬
def make_matrix(rows, columns):
    matrix = [[0 for x in range(columns)] for y in range(rows)]

    for y in range(rows):
        for x in range(columns):
            matrix[y][x] = y*columns + x + 1

    return matrix


def solution(rows, columns, queries):
    answer = []

    # 만들어진 회전하는 매트릭스가 돌아가면서 heap에 더하고 빼주면서  직사각형에서 테두리에 있는 숫자들을 한 칸씩 시계방향으로 회전
    matrix = make_matrix(rows, columns)

    for que in queries:
        y1, x1, y2, x2 = que
        heap = []

        y1x1 = matrix[y1-1][x1-1]
        y1x2 = matrix[y1-1][x2-1]
        y2x1 = matrix[y2-1][x1-1]
        y2x2 = matrix[y2-1][x2-1]

        heappush(heap,y1x1)
        heappush(heap,y1x2)
        heappush(heap,y2x1)
        heappush(heap,y2x2)

        for x in range(x2 - 1, x1 - 1, -1):
            matrix[y1-1][x] = matrix[y1-1][x-1]
            heappush(heap, matrix[y1-1][x])

        for y in range(y2 - 1, y1 - 1, -1):
            matrix[y][x2-1] = matrix[y-1][x2-1]
            heappush(heap, matrix[y][x2-1])

        for x in range(x1 - 1, x2 - 1, 1):
            matrix[y2-1][x] = matrix[y2-1][x+1]
            heappush(heap, matrix[y2-1][x])

        for y in range(y1 - 1, y2 - 1, 1):
            matrix[y][x1-1] = matrix[y+1][x1-1]
            heappush(heap, matrix[y][x1-1])

        matrix[y1][x2-1] = y1x2
        matrix[y2-1][x2-2] = y2x2
        matrix[y2-2][x1-1] = y2x1

        answer.append(heap[0])

    return answer
