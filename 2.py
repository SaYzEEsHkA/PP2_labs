import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
done = True
clock = pygame.time.Clock()
songs = ["Макс Корж - Времена.mp3", "the-weeknd_false-alarm.mp3"]
i=0
while i<len(songs):
    pygame.mixer.music.load(songs[i])
    i=i+1

vol = 1.0
repeat = 0
start_time = 0

while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN: #клавиша enter:
                pygame.mixer.music.play(repeat, start_time)
            elif event.key == pygame.K_SPACE:
                pygame.mixer.music.pause()
            elif event.key == pygame.K_ESCAPE:
                pygame.mixer.music.stop()
            elif event.key == pygame.K_UP:
                vol = vol+0.1
                pygame.mixer.music.set_volume (vol)
                print("Volume: " + str(pygame.mixer.music.get_volume()))
            elif event.key == pygame.K_DOWN:
                vol = vol-0.1
                pygame.mixer.music.set_volume (vol)
                print("Volume: " + str(pygame.mixer.music.get_volume()))
            elif event.key == pygame.K_TAB:
                if repeat == 0:
                    repeat = -1
                    pygame.mixer.music.queue('Макс Корж - Времена.mp3')
                    print ("repeat on")
                else:
                    repeat = 0
                    print ("repeat off")
            elif event.key == pygame.K_RIGHT:
                start_time = start_time + 10
                pygame.mixer.music.play(repeat, start_time)
                print("+10 sec")
            elif event.key == pygame.K_LEFT:
                start_time = start_time - 10
                pygame.mixer.music.play(repeat, start_time)
                print("-10 sec")
            while i<len(songs):
                if event.key == pygame.K_PAGEUP:
                    i=i+1
                    pygame.mixer.music.queue(songs[i])
                elif event.key == pygame.K_PAGEDOWN:
                    i=i-1
                    pygame.mixer.music.queue(songs[i])

    pygame.display.flip()
    clock.tick(60)
