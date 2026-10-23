import pygame
from pygame import mixer

pygame.init()
mixer.init()

W, H = 700, 700

mixer.music.load("pygame/background2.mp3")
mixer.music.set_volume(0.2)

mixer.music.play(-1)

screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Los Santos")
running = True
clock = pygame.time.Clock()
fliped = True

police_img = pygame.image.load("tief_game/police.png").convert_alpha()
me_img = pygame.image.load("tief_game/tief.png").convert_alpha()
background = pygame.image.load("tief_game/background.jpg").convert()

me_img.set_colorkey((255, 255, 255))
police_img.set_colorkey("#F5CDFF")

scale_police = pygame.transform.scale(police_img, (60, 70))
scale_tief = pygame.transform.scale(me_img, (60, 70))
scale_background = pygame.transform.scale(background, (700, 700))

fliped_tief = pygame.transform.flip(scale_tief, True, False)

overlay = pygame.Surface((W, H))
overlay.fill((0, 0, 0))
overlay.set_alpha(128)
font = pygame.font.SysFont(None, 48)

HP = 100 

pos_x, pos_y = 350, 350
pos2_x, pos2_y = 250, 350

game_over = False 

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if game_over:
        screen.blit(scale_background, (0, 0))
        screen.blit(scale_police, (pos2_x, pos2_y))
        if fliped:
            screen.blit(fliped_tief, (pos_x, pos_y))
        else:
            screen.blit(scale_tief, (pos_x, pos_y))
        screen.blit(overlay)
        
        text_surface = font.render("WANTED", True, (255, 0, 0))
        
        screen.blit(text_surface, (255, 300))
        pygame.display.flip()
        clock.tick(60)
        continue
                   
    keys = pygame.key.get_pressed()
        
    if keys[pygame.K_a]:
        pos_x -= 5
        fliped = False
    if keys[pygame.K_d]:
        pos_x += 5
        fliped = True
    if keys[pygame.K_s]:
        pos_y += 5
    if keys[pygame.K_w]:
        pos_y -= 5
        
    dx = pos_x - pos2_x
    dy = pos_y - pos2_y
    
    lenght = (dx ** 2 + dy ** 2) ** 0.5
    speed = 4
    
    if lenght <= speed:
        pos2_x = pos_x
        pos2_y = pos_y
    else:    
        dir_x = dx / lenght
        dir_y = dy / lenght
        pos2_x += dir_x * speed
        pos2_y += dir_y * speed

    screen.blit(scale_background, (0, 0))
    screen.blit(scale_police, (pos2_x, pos2_y))

    if fliped:
        screen.blit(fliped_tief, (pos_x, pos_y)) 
    else:
        screen.blit(scale_tief, (pos_x, pos_y))
    
    if int(pos2_y) == int(pos_y) and int(pos2_x) == int(pos_x):
        game_over = True 
        mixer.music.stop()
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
