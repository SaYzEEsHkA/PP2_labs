import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
done = True
clock = pygame.time.Clock()
speed = 20
x=640
y=360

while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if x<0 or x>1280:
                    print ("Круг вышел за пределы поля")
                elif x<1280:
                    x=x+speed
            elif event.key == pygame.K_LEFT:
                if x<0 or x>1280:
                    print ("Круг вышел за пределы поля")
                elif x>0:
                    x=x-speed
            elif event.key == pygame.K_UP:
                if y<0 or y>720:
                    print ("Круг вышел за пределы поля")
                elif y>0:
                    y=y-speed
            elif event.key == pygame.K_DOWN:
                if y<0 or y>720:
                    print ("Круг вышел за пределы поля")
                elif y<720:
                    y=y+speed


    screen.fill((255,255,255))

    pygame.draw.circle(screen, (255,0,0),(x,y),25)

    pygame.display.flip()
    clock.tick(60)
