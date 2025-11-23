import random
from settings import MAZE_WIDTH, MAZE_HEIGHT

class Maze:
    def __init__(self):
        self.width = MAZE_WIDTH
        self.height = MAZE_HEIGHT
        self.grid = [[1 for _ in range(self.width)] for _ in range(self.height)]
        self.generate_maze()

    def generate_maze(self):
        # 随机深度优先生成迷宫
        stack = []
        x, y = 1, 1
        self.grid[y][x] = 0
        stack.append((x, y))
        while stack:
            x, y = stack[-1]
            neighbors = []
            for dx, dy in [(-2,0),(2,0),(0,-2),(0,2)]:
                nx, ny = x+dx, y+dy
                if 1 <= nx < self.width-1 and 1 <= ny < self.height-1:
                    if self.grid[ny][nx] == 1:
                        neighbors.append((nx, ny))
            if neighbors:
                nx, ny = random.choice(neighbors)
                self.grid[(y+ny)//2][(x+nx)//2] = 0
                self.grid[ny][nx] = 0
                stack.append((nx, ny))
            else:
                stack.pop()

    def is_wall(self, x, y):
        return self.grid[y][x] == 1

    def is_path(self, x, y):
        return self.grid[y][x] == 0

    def get_random_path_cell(self):
        while True:
            x = random.randrange(1, self.width, 2)
            y = random.randrange(1, self.height, 2)
            if self.is_path(x, y):
                return x, y
