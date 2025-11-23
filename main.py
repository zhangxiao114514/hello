import pygame
import sys
from settings import *
from maze import Maze
from player import Player
from enemy import Enemy
from item import Item

def draw_maze(screen, maze):
    for y in range(maze.height):
        for x in range(maze.width):
            color = WHITE if maze.is_path(x, y) else BLACK
            pygame.draw.rect(screen, color, (x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE))

def draw_player(screen, player):
    pygame.draw.rect(screen, BLUE, player.rect)

def draw_enemy(screen, enemy):
    pygame.draw.rect(screen, RED, enemy.rect)

def draw_items(screen, items):
    for item in items:
        color = YELLOW if item.type == 'key' else GREEN
        pygame.draw.rect(screen, color, item.rect)

def draw_ui(screen, player):
    font = pygame.font.SysFont(None, 24)
    text = f"HP: {player.hp}  Key: {'Yes' if player.has_key else 'No'}"
    img = font.render(text, True, (0,0,0))
    screen.blit(img, (10, SCREEN_HEIGHT-30))

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('迷宫逃脱')
    clock = pygame.time.Clock()

    maze = Maze()
    player_x, player_y = 1, 1
    player = Player(player_x, player_y)
    exit_x, exit_y = maze.width-2, maze.height-2
    enemy = Enemy(*maze.get_random_path_cell())
    items = Item.random_items(maze, count=5)

    running = True
    win = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        if keys[pygame.K_UP]: dy = -1
        if keys[pygame.K_DOWN]: dy = 1
        if keys[pygame.K_LEFT]: dx = -1
        if keys[pygame.K_RIGHT]: dx = 1
        if dx or dy:
            player.move(dx, dy, maze)
        # 敌人移动
        enemy.move(maze, player)
        # 检查碰撞
        for item in items[:]:
            if player.x == item.x and player.y == item.y:
                if item.type == 'key':
                    player.pick_key()
                elif item.type == 'potion':
                    player.use_potion()
                items.remove(item)
        if player.x == enemy.x and player.y == enemy.y:
            player.hp -= 1
            if player.hp <= 0:
                running = False
        if player.x == exit_x and player.y == exit_y and player.has_key:
            win = True
            running = False
        # 绘制
        screen.fill(GRAY)
        draw_maze(screen, maze)
        draw_items(screen, items)
        draw_player(screen, player)
        draw_enemy(screen, enemy)
        draw_ui(screen, player)
        pygame.display.flip()
        clock.tick(10)
    # 结束界面
    font = pygame.font.SysFont(None, 48)
    msg = '胜利！' if win else '失败！'
    img = font.render(msg, True, (0,0,0))
    screen.fill(WHITE)
    screen.blit(img, (SCREEN_WIDTH//2-60, SCREEN_HEIGHT//2-24))
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
