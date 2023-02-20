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


def count_islands(grid):
    row = len(grid)
    col = len(grid[0])

    num_islands = 0
    visited = [[0] * col for i in range(row)]
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    for i in range(row):
        for j, num in enumerate(grid[i]):
            if is_visited_land(i, j, visited, grid):
                visited = find_island(i, j, grid, visited, directions, row, col)
                num_islands += 1

    return num_islands


# Finds the island that contains the given cell and returns the updated visited matrix
def find_island(i, j, grid, visited, directions, row, col):
    visited[i][j] = 1
    queue = [(i, j)]
    while queue:
        x, y = queue.pop(0)
        for k in range(len(directions)):
            nx_x = x + directions[k][0]
            nx_y = y + directions[k][1]

            is_in_bound = 0 <= nx_x < row and 0 <= nx_y < col

            if is_in_bound:
                if is_visited_land(nx_x, nx_y, visited, grid):
                    queue.append((nx_x, nx_y))
                    visited[nx_x][nx_y] = 1
    return visited

def is_visited_land(x, y, visited, grid):
    return visited[x][y] != 1 and grid[x][y] == 1

if __name__ == '__main__':
    #Taken from test_bfs:
    grid_1 = [[1, 1, 1, 1, 0], [1, 1, 0, 1, 0], [1, 1, 0, 0, 0],
              [0, 0, 0, 0, 0]]
    print(count_islands(grid_1))
    grid_2 = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 1, 0, 0],
              [0, 0, 0, 1, 1]]
    print(count_islands(grid_2))
    grid_3 = [[1, 1, 1, 0, 0, 0], [1, 1, 0, 0, 0, 0], [1, 0, 0, 0, 0, 1],
              [0, 0, 1, 1, 0, 1], [0, 0, 1, 1, 0, 0]]
    print(count_islands(grid_3))
    grid_4 = [[1, 1, 0, 0, 1, 1], [0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 0, 1],
              [1, 1, 1, 1, 0, 0]]
    print(count_islands(grid_4))