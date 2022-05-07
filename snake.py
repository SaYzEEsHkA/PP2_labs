import psycopg2
import random
import time
import pygame
from config import config

pygame.init()

WID, HEI = 600, 600
SCREEN = pygame.display.set_mode((WID, HEI))
BLOCK_SIZE = 30
levels = [5, 10, 15, 20, 25]
level = 1
done, die, new_level, menu = False, False, False, False
FPS = 5
Clock = pygame.time.Clock()

background = pygame.image.load('сетка.png')
apple = pygame.image.load('яблоко.png')
font = pygame.font.SysFont('comicsansms', 30)

SCORE = 0


class Point:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y


class Food:
    def __init__(self, wall):
        self.point = random.choice(wall)
        self.image = apple
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.point.x * 30, self.point.y * 30)

    def draw(self):
        SCREEN.blit(self.image, self.rect)

    def eat_and_move(self, snake, wall):
        global SCORE

        if self.point.x == snake.body[0].x and self.point.y == snake.body[0].y:
            SCORE += 1
            self.point = random.choice(wall)
            self.rect.topleft = (self.point.x * 30, self.point.y * 30)


class Wall():
    def __init__(self, level):
        self.body = []
        self.for_food = []
        plan = open(f'levels/level{level}.txt', 'r')

        for y in range(0, HEI // BLOCK_SIZE + 1):
            for x in range(0, WID // BLOCK_SIZE + 1):
                if plan.read(1) == '#':
                    self.body.append(Point(x, y))
        for y in range(0, BLOCK_SIZE + 1):
            for x in range(0, WID // BLOCK_SIZE + 1):
                if plan.read(1) != '#' and y < 20 and x < 20:
                    self.for_food.append(Point(x, y))

    def draw(self):
        for point in self.body:
            rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, (226, 135, 67), rect)


class Snake:
    def __init__(self):
        global SCORE
        self.body = [Point(10, 10)]
        self.dx, self.dy = 0, 0
        self.level = SCORE // 5 + 1
        self.reson = ''

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        self.body[0].x += self.dx
        self.body[0].y += self.dy

    def draw(self):
        rect = pygame.Rect(BLOCK_SIZE * self.body[0].x, BLOCK_SIZE * self.body[0].y, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(SCREEN, (51, 102, 0), rect)
        x, y, z = 52, 103, 1
        for i in range(1, len(self.body)):
            rect = pygame.Rect(BLOCK_SIZE * self.body[i].x, BLOCK_SIZE * self.body[i].y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, (x + (i * 2), y + (i * 2), z + (i * 2)), rect)

    def check_collision(self, wall, food):
        global die
        if food.point.x == self.body[0].x and food.point.y == self.body[0].y:
            self.body.append(Point(food.point.x, food.point.y))

        for point in self.body[2: len(self.body) - 1]:
            if self.body[0].x == point.x and self.body[0].y == point.y:
                die = True
                self.reson = 'Ты врезался в себя'

        if self.body[0].x >= WID // BLOCK_SIZE:
            self.reson = 'Ты врезался в границу'
            die = True
        if self.body[0].y >= HEI // BLOCK_SIZE:
            self.reson = 'Ты врезался в границу'
            die = True
        if self.body[0].x < 0:
            self.reson = 'Ты врезался в границу'
            die = True
        if self.body[0].y < 0:
            self.reson = 'Ты врезался в границу'
            die = True

        for i in wall.body:
            if self.body[0].x == i.x and self.body[0].y == i.y:
                die = True
                self.reson = 'Ты врезался в стену'



def table(name):
    global SCORE
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("CREATE TABLE snake_user(name VARCHAR(255) PRIMARY KEY, score INTEGER NOT NULL)")
        conn.commit()
    except(Exception, psycopg2.DatabaseError):
            try:
                params = config()
                conn = psycopg2.connect(**params)
                cur = conn.cursor()
                command = f"""INSERT INTO public.snake_user(
                    name, score)
                    VALUES (%s, 0)"""
                cur.execute(command, (name,))
                conn.commit()
            except:
                params = config()
                conn = psycopg2.connect(**params)
                cur = conn.cursor()
                command = """SELECT score FROM public.snake_user
                    WHERE name = %s;"""
                cur.execute(command, (name,))
                SCORE = int(cur.fetchone()[0])
                print('Your level is',SCORE // 5 + 1)
                print('Your score is equal to', SCORE)
    finally:
        if conn is not None:
            conn.close()




def save(name, score):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        command = """UPDATE public.snake_user
        SET score = %s
        WHERE name = %s;"""
        cur.execute(command, (score, name))
        conn.commit()
        print('save')
    except:
        print('Сохранение не удалось')
    finally:
        if conn is not None:
            conn.close()

def game(name):
    global done, menu, SCORE, new_level, FPS, level, die, levels
    snake = Snake()
    wall = Wall(snake.level)
    food = Food(wall.for_food)

    while not done:
        POINT = pygame.mouse.get_pos()
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                done = True
            if menu:
                if i.type == pygame.MOUSEBUTTONDOWN:
                    if 240 <= POINT[0] <= 360 and 400 <= POINT[1] <= 450:
                        save(name, SCORE)
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_RIGHT:
                    if snake.dx != -1:
                        snake.dx = 1
                        snake.dy = 0
                if i.key == pygame.K_LEFT:
                    if snake.dx != 1:
                        snake.dx = -1
                        snake.dy = 0
                if i.key == pygame.K_UP:
                    if snake.dy != 1:
                        snake.dx = 0
                        snake.dy = -1
                if i.key == pygame.K_DOWN:
                    if snake.dy != -1:
                        snake.dx = 0
                        snake.dy = 1
                if i.key == pygame.K_ESCAPE:
                    menu = not menu

        if SCORE in levels:
            if SCORE == 25:
                SCREEN.fill((255, 255, 255))
                SCREEN.blit(font.render('You completed the game.', True, (54, 57, 97)), (116, 322))
                pygame.display.update()
                time.sleep(3)
                done = True
            else:
                snake.body[0].x, snake.body[0].y = 10, 11
                die = False
                snake.level = SCORE // 5 + 1
                wall = Wall(snake.level)
                levels.pop(0)

        SCREEN.blit(background, (0, 0))

        if not menu:
            wall.draw()
            snake.draw()
            food.draw()
            snake.move()
            snake.check_collision(wall, food)
            food.eat_and_move(snake, wall.for_food)
            FPS = snake.level + 4

        if menu:
            die = False
            FPS = 0
            pygame.draw.rect(SCREEN, (86, 117, 62), (100, 100, 400, 400))
            button = pygame.Rect(240, 400, 120, 50)
            pygame.draw.rect(SCREEN, (99, 135, 74), button)
            SCREEN.blit(font.render('SAVE', True, (255, 255, 255)), (260, 400))
            SCREEN.blit(font.render(str(SCORE), True, (255, 255, 255)), (260, 300))
        if die:
            SCREEN.fill((255, 0, 0))
            SCREEN.blit(font.render('Your snake died', True, (0, 0, 0)), (180, 314))
            SCREEN.blit(font.render(str(snake.reson), True, (0, 0, 0)), (10, 500))
            pygame.display.update()
            time.sleep(2)
            done = True
        SCREEN.blit(font.render(str(SCORE), True, (163, 219, 159)), (0, -7))
        pygame.display.flip()
        Clock.tick(FPS)

if __name__ == '__main__':
    name = input('Enter your name\n')
    table(name)

    game(name)



pygame.quit()
