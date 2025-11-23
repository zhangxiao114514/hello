from settings import PLAYER_SPEED, CELL_SIZE, MAZE_WIDTH, MAZE_HEIGHT

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = [x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE]
        self.has_key = False
        self.hp = 3

    def move(self, dx, dy, maze):
        nx, ny = self.x + dx, self.y + dy
        if 0 <= nx < MAZE_WIDTH and 0 <= ny < MAZE_HEIGHT and maze.is_path(nx, ny):
            self.x = nx
            self.y = ny
            self.rect[0] = self.x * CELL_SIZE
            self.rect[1] = self.y * CELL_SIZE

    def pick_key(self):
        self.has_key = True

    def use_potion(self):
        self.hp = min(self.hp + 1, 3)
