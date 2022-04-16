import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
screen2 = pygame.Surface((800, 600))

radius = 5
x = 0
y = 0
points = []
colors = { "blue": (0, 0, 255), "red": (255, 0, 0), "green": (0, 255, 0), "yellow": (255, 255, 0), "black": (0, 0, 0), "white": (255, 255, 255), "cyan": (0, 255, 255)}
color = colors["black"]
mouse_down = False
screen2.fill((colors["white"]))
screen.fill((colors["white"]))
mode = 1
prevX = -1
prevY = -1
currentX = -1
currentY = -1


while True:
    pygame.draw.rect(screen, colors["black"], pygame.Rect(10, 10, 30, 30))
    pygame.draw.rect(screen, colors["red"], pygame.Rect(43, 10, 30, 30))
    pygame.draw.rect(screen, colors["blue"], pygame.Rect(76, 10, 30, 30))
    pygame.draw.rect(screen, colors["green"], pygame.Rect(109, 10, 30, 30))
    pygame.draw.rect(screen, colors["yellow"], pygame.Rect(142, 10, 30, 30))
    pygame.draw.rect(screen, colors["cyan"], pygame.Rect(175, 10, 30, 30))
    pygame.draw.rect(screen, colors["black"], pygame.Rect(10, 43, 30, 30), 1)

    mouse_pos = pygame.mouse.get_pos()
    mouse_button = pygame.mouse.get_pressed()
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
            if event.key == pygame.K_BACKSPACE:
                screen.fill((colors["white"]))
            if event.key == pygame.K_l:
                mode = 1
            if event.key == pygame.K_c:
                mode = 2
            if event.key == pygame.K_r:
                mode = 3

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_down = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                screen2.blit(screen, (0, 0))
                mouse_down = False

        if (keys[pygame.K_RCTRL] or keys[pygame.K_LCTRL]) and (event.type == pygame.KEYDOWN and event.key == pygame.K_UP):
                radius += 2
        if (keys[pygame.K_RCTRL] or keys[pygame.K_LCTRL]) and (event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN):
                radius -= 2

        if mouse_down == True:
            if mouse_pos[0] >= 10 and mouse_pos[0] <= 40 and mouse_pos[1] >= 10 and mouse_pos[1] <= 40:
                color = colors["black"]
            if mouse_pos[0] >= 43 and mouse_pos[0] <= 73 and mouse_pos[1] >= 10 and mouse_pos[1] <= 40:
                color = colors["red"]
            if mouse_pos[0] >= 76 and mouse_pos[0] <= 106 and mouse_pos[1] >= 10 and mouse_pos[1] <= 40:
                color = colors["blue"]
            if mouse_pos[0] >= 109 and mouse_pos[0] <= 139 and mouse_pos[1] >= 10 and mouse_pos[1] <= 40:
                color = colors["green"]
            if mouse_pos[0] >= 142 and mouse_pos[0] <= 172 and mouse_pos[1] >= 10 and mouse_pos[1] <= 40:
                color = colors["yellow"]
            if mouse_pos[0] >= 175 and mouse_pos[0] <= 205 and mouse_pos[1] >= 10 and mouse_pos[1] <= 40:
                color = colors["cyan"]
            if mouse_pos[0] >= 10 and mouse_pos[0] <= 40 and mouse_pos[1] >= 33 and mouse_pos[1] <= 73:
                color = colors["white"]

        if mode == 1:
            screen.blit(screen2, (0, 0))
            if mouse_down == True:
                if event.type == pygame.MOUSEMOTION:
                    position = event.pos
                    points = points + [position]
            else:
                points = []

            i = 0
            while i < len(points) - 1:
                dx = points[i][0] - points[i+1][0]
                dy = points[i][1] - points[i+1][1]
                iterations = max(abs(dx), abs(dy))

                for j in range(iterations):
                    progress = 1.0 * j / iterations
                    aprogress = 1 - progress
                    x = int(aprogress * points[i][0] + progress * points[i+1][0])
                    y = int(aprogress * points[i][1] + progress * points[i+1][1])
                    pygame.draw.circle(screen, color, (x, y), radius)
                i += 1

        if mode == 2:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_down = True
                    currentX =  event.pos[0]
                    currentY =  event.pos[1]
                    prevX =  event.pos[0]
                    prevY =  event.pos[1]

            if event.type == pygame.MOUSEBUTTONUP:
                mouse_down = False
                screen2.blit(screen, (0, 0))


            if event.type == pygame.MOUSEMOTION:
                if mouse_down:
                    currentX =  event.pos[0]
                    currentY =  event.pos[1]


            if mouse_down and prevX != -1 and prevY != -1 and currentX != -1 and currentY != -1:
                screen.blit(screen2, (0, 0))
                pygame.draw.circle(screen, color, (prevX, prevY), max(abs(prevX - currentX), abs(prevY - currentY)), radius)


        if mode == 3:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_down = True
                    currentX =  event.pos[0]
                    currentY =  event.pos[1]
                    prevX =  event.pos[0]
                    prevY =  event.pos[1]

            if event.type == pygame.MOUSEBUTTONUP:
                mouse_down = False
                screen2.blit(screen, (0, 0))


            if event.type == pygame.MOUSEMOTION:
                if mouse_down:
                    currentX = event.pos[0]
                    currentY = event.pos[1]


            if mouse_down and prevX != -1 and prevY != -1 and currentX != -1 and currentY != -1:
                screen.blit(screen2, (0, 0))
                pygame.draw.rect(screen, color, pygame.Rect(min(prevX, currentX), min(prevY, currentY), abs(prevX - currentX), abs(prevY - currentY)), radius)

    pygame.display.flip()

    clock.tick(60)
