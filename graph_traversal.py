import time
from collections import deque
solution = {}  # solution dictionary
found = False

def search(path, walls, start, end, square, color="green", bfs=False, dfs=False):
    global found

    queue = []
    visited = set()
    frontier = deque()

    square.color(color)
    frontier.append(start)
    solution[start] = start
    while len(frontier) > 0:
        if bfs:
            x, y = frontier.popleft()

        elif dfs:
            x, y = frontier.pop()

        if (x - 24, y) in path and (x - 24, y) not in visited:  # check the cell on the left
            cell = (x - 24, y)
            if bfs:
                solution[cell] = x, y
            frontier.append(cell)  # add cell to frontier list
            visited.add((x - 24, y))  # add cell to visited list

        if (x, y - 24) in path and (x, y - 24) not in visited:  # check the cell down
            cell = (x, y - 24)
            if bfs:
                solution[cell] = x, y
            frontier.append(cell)
            visited.add((x, y - 24))

        if (x + 24, y) in path and (x + 24, y) not in visited:  # check the cell on the  right
            cell = (x + 24, y)
            if bfs:
                solution[cell] = x, y
            frontier.append(cell)
            visited.add((x + 24, y))

        if (x, y + 24) in path and (x, y + 24) not in visited:  # check the cell up
            cell = (x, y + 24)
            if bfs:
                solution[cell] = x, y
            frontier.append(cell)
            visited.add((x, y + 24))

        if bfs and (x, y) == end:
            found = True

        square.goto(x, y)
        square.stamp()
        if dfs:
            time.sleep(0.01)


def backRoute(s_x, s_y, e_x,e_y,square,color = "yellow"):
    global found,bfs_done
    if found:
        print('found!')
        x, y = e_x, e_y
        square.color(color)
        square.goto(solution[x, y])  # move the yellow sprite to the key value of solution ()
        square.stamp()
        while not (x, y) == (s_x, s_y):    # stop loop when current cells == start cell
            x, y = solution[x, y]               # "key value" now becomes the new key
            square.goto(solution[x, y])  # move the yellow sprite to the key value of solution ()
            square.stamp()

    return True if found else False

