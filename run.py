import os

if __name__ == "__main__":
    current_dir = os.getcwd()

    # Check current and 'maze' directory for maze.py
    maze_path = os.path.join(current_dir, "maze", "maze.py")
    if not os.path.exists(maze_path):
        maze_path = os.path.join(current_dir, "maze.py")

    # Check current and 'showroom' directory for showroom.py
    showroom_path = os.path.join(current_dir, "showroom", "showroom.py")
    if not os.path.exists(showroom_path):
        showroom_path = os.path.join(current_dir, "showroom.py")

    # Run maze.py
    print("Maze ouput:")
    os.system(f'python3 \"{maze_path}\"')

    # Space between outputs
    print("-" * 50)

    # Run showroom.py
    print("Showroom output:")
    os.system(f'python3 \"{showroom_path}\"')
