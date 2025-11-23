import random
from settings import ITEM_TYPES, CELL_SIZE

class Item:
    def __init__(self, x, y, item_type):
        self.x = x
        self.y = y
        self.type = item_type
        self.rect = [x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE]

    @staticmethod
    def random_items(maze, count=3):
        items = []
        for _ in range(count):
            x, y = maze.get_random_path_cell()
            item_type = random.choice(ITEM_TYPES)
            items.append(Item(x, y, item_type))
        return items
