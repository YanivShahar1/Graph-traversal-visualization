from maze import *


#buttons:
generate_maze_button = tkinter.Button(master = window, text="Generate random maze", command = generate_random_maze)
generate_maze_button.config(bg="red",fg="black")
generate_maze_button.grid(padx=2, pady=2, row=0, column=11, sticky='nsew')

bfs_button = tkinter.Button(master = window, text ="BFS visualization", command=play_bfs)
bfs_button.config(bg="#05ff8c",fg="black")
bfs_button.grid(padx=2, pady=2, row=2, column=11, sticky='nsew')

Shortest_path_button = tkinter.Button(master = window, text ="Shortest path", command=shortest_path)
Shortest_path_button.config(bg="yellow",fg="black")
Shortest_path_button.grid(padx=2, pady=2, row=2, column=12, sticky='nsew')

dfs_button = tkinter.Button(master = window, text="DFS visualization", command=play_dfs)
dfs_button.config(bg="#ff7505", fg="black")
dfs_button.grid(padx=2, pady=2, row=3, column=11, sticky='nsew')


clear_maze_button = tkinter.Button(master = window, text="Clear Maze", command = clear_maze)
clear_maze_button.config(bg="green",fg="black")
clear_maze_button.grid(padx=2, pady=2, row=5, column=11, sticky='nsew')

window.mainloop()