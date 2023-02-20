import collections

"""
do BFS from each building, and decrement all empty place for every building visit
when grid[i][j] == -b_nums, it means that grid[i][j] are already visited from all b_nums
and use dist to record distances from b_nums
"""

instrument = [0] * 12

def shortest_distance(grid):
    global instrument
    if not grid or not grid[0]:
        instrument[0] = 1
        return -1
    else:
        instrument[1] = 1

    matrix = [[[0,0] for i in range(len(grid[0]))] for j in range(len(grid))]

    count = 0    # count how many building we have visited
    for i in range(len(grid)):
        instrument[2] = 1
        for j in range(len(grid[0])):
            instrument[3] = 1
            if grid[i][j] == 1:
                instrument[4] = 1
                bfs(grid, matrix, i, j, count)
                count += 1
            else:
                instrument[5] = 1

    res = float('inf')
    for i in range(len(matrix)):
        instrument[6] = 1
        for j in range(len(matrix[0])):
            instrument[7] = 1
            if matrix[i][j][1]==count:
                instrument[8] = 1
                res = min(res, matrix[i][j][0])
            else:
                instrument[9] = 1

    instrument[10] = 1 if res!=float('inf') else instrument[11] = 1
    return res if res!=float('inf') else -1

def bfs(grid, matrix, i, j, count):
    q = [(i, j, 0)]
    while q:
        i, j, step = q.pop(0)
        for k, l in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]:
            # only the position be visited by count times will append to queue
            if 0<=k<len(grid) and 0<=l<len(grid[0]) and \
                    matrix[k][l][1]==count and grid[k][l]==0:
                matrix[k][l][0] += step+1
                matrix[k][l][1] = count+1
                q.append((k, l, step+1))

def checkcoverage():
    global instrument
    coverage = sum(instrument) / len(instrument) * 100

    print("----------Current Branch Coverage----------")
    print("Unreachable: 0")
    print("Branch coverage:", coverage, "%")
    print("----------Current Branch Coverage----------")

if __name__ == '__main__':
    checkcoverage()
