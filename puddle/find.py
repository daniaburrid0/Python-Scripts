def largest_puddle(map):
    # Initialize variables
    rows = len(map)
    cols = len(map[0])
    visited = [[False] * cols for _ in range(rows)]
    max_puddle_size = 0
    max_puddle_coords = []

    # Define a helper function to recursively explore the map
    def explore(i, j, puddle_size, puddle_coords):
        # Mark the current cell as visited
        visited[i][j] = True

        # Check the neighboring cells
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < rows and 0 <= nj < cols and not visited[ni][nj]:
                # If the neighboring cell is lower, explore it
                if map[ni][nj] < map[i][j]:
                    puddle_size, puddle_coords = explore(ni, nj, puddle_size, puddle_coords)
                # If the neighboring cell is higher, add to the puddle size
                elif map[ni][nj] > map[i][j]:
                    puddle_size += map[ni][nj] - map[i][j]
                    puddle_coords.append((ni, nj))

        return puddle_size, puddle_coords

    # Iterate over all cells and explore unvisited cells
    for i in range(rows):
        for j in range(cols):
            if not visited[i][j]:
                # If the cell is a local minimum, explore it
                if all(map[ni][nj] >= map[i][j] for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)] if 0 <= ni < rows and 0 <= nj < cols):
                    puddle_size, puddle_coords = explore(i, j, 0, [(i, j)])
                    if puddle_size > max_puddle_size:
                        max_puddle_size = puddle_size
                        max_puddle_coords = puddle_coords

    return max_puddle_coords

import colorama
from colorama import Fore, Style

def print_map(map, puddle_coords):
    colorama.init()

    for i, row in enumerate(map):
        for j, cell in enumerate(row):
            if (i, j) in puddle_coords:
                print(Fore.BLUE + str(cell) + Style.RESET_ALL, end=' ')
            else:
                print(str(cell), end=' ')
        print()

map = [
    [5, 5, 5, 5, 5, 2, 2],
    [5, 4, 3, 3, 5, 2, 2],
    [5, 3, 5, 3, 5, 2, 2],
    [5, 5, 5, 5, 5, 5, 2],
    [5, 5, 5, 5, 2, 1, 5],
    [5, 3, 2, 5, 1, 4, 5],
    [5, 5, 2, 5, 5, 3, 5]
]

puddle_coords = largest_puddle(map)
print_map(map, puddle_coords)