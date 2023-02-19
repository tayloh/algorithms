"""
This is a bfs-version of counting-islands problem in dfs section.
Given a 2d grid map of '1's (land) and '0's (water),
count the number of islands.
An island is surrounded by water and is formed by
connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:
11110
11010
11000
00000
Answer: 1

Example 2:
11000
11000
00100
00011
Answer: 3

Example 3:
111000
110000
100001
001101
001100
Answer: 3

Example 4:
110011
001100
000001
111100
Answer: 5
"""

instrument = [0] * 11

def count_islands(grid):
    global instrument
    instrument[0] = 1
    row = len(grid)
    col = len(grid[0])

    num_islands = 0
    visited = [[0] * col for i in range(row)]
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    queue = []

    for i in range(row):
        instrument[1] = 1
        for j, num in enumerate(grid[i]):
            instrument[2] = 1
            if num == 1 and visited[i][j] != 1:
                instrument[3] = 1
                visited[i][j] = 1
                queue.append((i, j))
                while queue:
                    instrument[4] = 1
                    x, y = queue.pop(0)
                    for k in range(len(directions)):
                        instrument[5] = 1
                        nx_x = x + directions[k][0]
                        nx_y = y + directions[k][1]
                        if nx_x >= 0 and nx_y >= 0 and nx_x < row and nx_y < col:
                            instrument[6] = 1
                            if visited[nx_x][nx_y] != 1 and grid[nx_x][nx_y] == 1:
                                instrument[7] = 1
                                queue.append((nx_x, nx_y))
                                visited[nx_x][nx_y] = 1
                            else:
                                instrument[8] = 1
                        else:
                            instrument[9] = 1
                instrument[1] = 1
                num_islands += 1
    instrument[10] = 1
    return num_islands

def checkcoverage():
    global instrument
    coverage = sum(instrument) / len(instrument) * 100

    print("----------Current Branch Coverage----------")
    print("Unreachable: 0")
    print("Branch coverage:", coverage, "%")
    print("----------Current Branch Coverage----------")

if __name__ == '__main__':
    #Taken from test_bfs:
    grid_1 = [[1, 1, 1, 1, 0], [1, 1, 0, 1, 0], [1, 1, 0, 0, 0],
              [0, 0, 0, 0, 0]]
    count_islands(grid_1)
    grid_2 = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 1, 0, 0],
              [0, 0, 0, 1, 1]]
    count_islands(grid_2)
    grid_3 = [[1, 1, 1, 0, 0, 0], [1, 1, 0, 0, 0, 0], [1, 0, 0, 0, 0, 1],
              [0, 0, 1, 1, 0, 1], [0, 0, 1, 1, 0, 0]]
    count_islands(grid_3)
    grid_4 = [[1, 1, 0, 0, 1, 1], [0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 0, 1],
              [1, 1, 1, 1, 0, 0]]
    count_islands(grid_4)

    checkcoverage()