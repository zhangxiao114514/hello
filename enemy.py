import random
from settings import ENEMY_SPEED, ENEMY_VISION_RANGE, CELL_SIZE, MAZE_WIDTH, MAZE_HEIGHT

class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = [x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE]
        self.patrol_dir = random.choice([(1,0),(-1,0),(0,1),(0,-1)])

    def move(self, maze, player):
        # 简单AI：如果玩家在视野内，追击，否则巡逻
        if abs(self.x - player.x) + abs(self.y - player.y) <= ENEMY_VISION_RANGE:
            dx = 1 if player.x > self.x else -1 if player.x < self.x else 0
            dy = 1 if player.y > self.y else -1 if player.y < self.y else 0
            if 0 <= self.x+dx < MAZE_WIDTH and 0 <= self.y+dy < MAZE_HEIGHT and maze.is_path(self.x+dx, self.y+dy):
                self.x += dx
                self.y += dy
        else:
            dx, dy = self.patrol_dir
            if 0 <= self.x+dx < MAZE_WIDTH and 0 <= self.y+dy < MAZE_HEIGHT and maze.is_path(self.x+dx, self.y+dy):
                self.x += dx
                self.y += dy
            else:
                self.patrol_dir = random.choice([(1,0),(-1,0),(0,1),(0,-1)])
        self.rect[0] = self.x * CELL_SIZE
        self.rect[1] = self.y * CELL_SIZE
