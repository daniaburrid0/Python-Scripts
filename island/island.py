import colorama
colorama.init()  # initialize colorama to enable colored output

# function to find all islands in the given map
def get_islands(map):
    islands = []
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == 1:
                island = set()
                stack = [(i, j)]
                while stack:
                    x, y = stack.pop()
                    if 0 <= x < len(map) and 0 <= y < len(map[0]) and map[x][y] == 1 and (x, y) not in island:
                        island.add((x, y))
                        stack.extend([(x+1, y), (x-1, y), (x, y+1), (x, y-1)])
                islands.append(island)
    return islands

# function to print the map with colored islands
def colored_map(map, islands):
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == 1:
                for island in islands:
                    if (i, j) in island:
                        print(colorama.Fore.GREEN + str(map[i][j]), end='')  # print green for island cells
                        break
                else:
                    print(colorama.Fore.RED + str(map[i][j]), end='')  # print red for non-island cells
            else:
                print(colorama.Fore.WHITE + str(map[i][j]), end='')  # print white for water cells
        print()

# example usage
map = [
    [1,1,0,1,1],
    [1,1,0,0,0],
    [0,0,0,0,0],
    [1,1,1,0,0],
]
islands = get_islands(map)
print(islands)
colored_map(map, islands)