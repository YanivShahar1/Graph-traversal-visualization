import tkinter
import turtle
import tkinter.messagebox
import random

from graph_traversal import *

window = tkinter.Tk()
window.config(bg="white")
canvas = tkinter.Canvas(master = window,bg="red", width = 800, height = 600)
canvas.grid(padx=2, pady=2, row=0, column=0, rowspan=10, columnspan=10)

square = turtle.RawTurtle(canvas)
square.shape("square")
square.penup()                    # lift up the pen so it do not leave a trail
square.speed(0)


# setup lists
walls = []
path = []

maze_in_process = False
maze_on_screen = False
bfs_done = False

global screen_s_x, screen_s_y, screen_e_x, screen_e_y

def get_random_start_end(max_height, max_width):
    valid_position = False
    while not valid_position:
        start_x = random.randint(1, max_width)
        start_y = random.randint(1, int(max_height / 4))
        end_x = random.randint(1, max_width)
        end_y = random.randint(int(max_height / 2), max_height -1)
        if start_x != end_x or start_y != end_y:  # different starting and ending positions
            valid_position = True

    return start_x, start_y, end_x, end_y


def generate_random_maze(max_height= 22, max_width = 30):
    global maze_on_screen, maze_in_process
    if maze_on_screen:
        tkinter.messagebox.showinfo("Error", "You should clean the maze first\nPress the Clear Maze button")
    else:
        maze_in_process = True
        height = random.randint(15,max_height)
        width = random.randint(11, max_width)

        start_x, start_y, end_x, end_y = get_random_start_end(height- 1, width -1)
        print(start_x,' ', start_y,' ', end_x,' ', end_y )
        global screen_s_x, screen_s_y, screen_e_x, screen_e_y
        for y in range(height):
            for x in range(width):
                screen_x = -338 + (x * 24)  # move to the x location on the screen staring at -588
                screen_y = 260 - (y * 24)  # move to the y location of the screen starting at 288

                if x == start_x and y == start_y: #found starting position
                    screen_s_x, screen_s_y = screen_x,screen_y
                    square.color("red")
                    square.goto(screen_x, screen_y)
                    square.stamp()

                elif x == end_x and y == end_y: #found ending position
                    screen_e_x,screen_e_y = screen_x,screen_y
                    path.append((screen_x, screen_y))
                    square.color("purple")
                    square.goto(screen_x, screen_y)
                    square.stamp()
                else:
                    maze_characters = ["wall", "empty", "empty"]  # twice chance for empty cell
                    character = random.choice(maze_characters)
                    if character == "wall":
                        square.color("black")
                        square.goto(screen_x, screen_y)  #
                        square.stamp()  # stamp a copy of the turtle on the screen
                        walls.append((screen_x, screen_y))  # add coordinate to walls list

                    elif character == "empty":
                        path.append((screen_x, screen_y))
                        square.color("#00ffff")
                        square.goto(screen_x, screen_y)
                        square.stamp()
                    else:
                        print("errorr!")

    maze_in_process = False
    maze_on_screen = True

def clear_maze():
    global dirty_maze, found, maze_on_screen, walls, path,bfs_done
    if maze_in_process:
        tkinter.messagebox.showinfo("Error", "Please wait untill the maze building finish")
    elif maze_on_screen:
        bfs_done = False
        canvas.delete("all")
        walls.clear()
        path.clear()
        solution.clear()
        dirty_maze = False
        found = False
        maze_on_screen = False


def check_maze_available():
    global maze_on_screen, maze_in_process
    res = True
    if maze_in_process:
        tkinter.messagebox.showinfo("Error", "Please wait untill the maze building finish")
        res = False
    elif not maze_on_screen:
        tkinter.messagebox.showinfo("Error", "No maze on screen")
        res = False
    return res


def play_bfs():
    global bfs_done
    if check_maze_available():
        search(path, walls, (screen_s_x, screen_s_y), (screen_e_x, screen_e_y), square, color="#05ff8c",bfs=True)
        bfs_done = True

def shortest_path():
    global bfs_done
    if check_maze_available():
        if bfs_done:
            found = backRoute(screen_s_x, screen_s_y, screen_e_x, screen_e_y, square, color="yellow")
            if not found:
                tkinter.messagebox.showinfo("No path", "Ther's no path from red to purple")
        else:
            tkinter.messagebox.showinfo("Error", "You should run BFS on this maze first!")

def play_dfs():
    if check_maze_available():
        search(path, walls, (screen_s_x, screen_s_y), (screen_e_x, screen_e_y), square, color="#ff7505",dfs=True)
