import random

import pygame
from pygame import mixer

pygame.init()
mixer.init()

W, H = 800, 700

music = mixer.music.load("background2.mp3")
mixer.music.set_volume(0.2)

mixer.music.play(-1)

#Displays
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Los Santos")
running = True
clock = pygame.time.Clock()
fliped = True

#Images 
police_img = pygame.image.load("police.png").convert_alpha()
me_img = pygame.image.load("tief.png").convert_alpha()
background = pygame.image.load("background.jpg").convert()

me_img.set_colorkey((255, 255, 255))
police_img.set_colorkey("#F5CDFF")

scale_police = pygame.transform.scale(police_img, (60, 70))
scale_tief = pygame.transform.scale(me_img, (60, 70))
scale_background = pygame.transform.scale(background, (W, H))

small_bg = pygame.transform.smoothscale(scale_background, (W // 20, H // 20))
blured_background = pygame.transform.smoothscale(small_bg, (W, H))

fliped_tief = pygame.transform.flip(scale_tief, True, False)

overlay = pygame.Surface((W, H))
overlay.fill((0, 0, 0))
overlay.set_alpha(128)
font = pygame.font.SysFont(None, 100)
font2 = pygame.font.SysFont(None, 50)

pos_x, pos_y = 350, 350
pos2_x, pos2_y = 250, 350

player_rect = pygame.Rect(pos_x, pos_y, 60, 70)

#Stars Creating
stars = []
coins = 0

for _ in range(10):
        posx = random.randint(0, W - 50)
        posy = random.randint(0, H - 50)
        stars.append({"rect": pygame.Rect(posx, posy, 20, 20),
                      "posx": posx,
                      "posy": posy}) 

game_over = False
Win = False 

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  
    
    if Win:
        screen.blit(blured_background, (0, 0))
        screen.blit(overlay, (0, 0))
        
        screen.blit(scale_police, (pos2_x, pos2_y))
        if fliped:
            screen.blit(fliped_tief, (pos_x, pos_y))
        else:
            screen.blit(scale_tief, (pos_x, pos_y))
        keys3 = pygame.key.get_pressed()
        
        text_surface = font.render("YOU WON!!!", True, (0, 255, 0))
        text_surface2 = font2.render("Press [E] to exit...", True, (20, 20, 20))
        
        screen.blit(text_surface, (180, 150))
        screen.blit(text_surface2, (230, 250))
        
        if keys3[pygame.K_e]:
            Win = False
            pygame.quit()
        
        pygame.display.flip()
        clock.tick(60)
        continue
    
    #BUSTED Screen
    if game_over:
        screen.blit(blured_background, (0, 0))
        screen.blit(overlay, (0, 0))
        
        screen.blit(scale_police, (pos2_x, pos2_y))
        keys2 = pygame.key.get_pressed()
        if fliped:
            screen.blit(fliped_tief, (pos_x, pos_y))
        else:
            screen.blit(scale_tief, (pos_x, pos_y))

        text_surface = font.render("BUSTED", True, (255, 0, 0))
        text_surface2 = font2.render("Press [Q] to continue...", True, (20, 20, 20))
        
        screen.blit(text_surface, (240, 150))
        screen.blit(text_surface2, (200, 250))
        if keys2[pygame.K_q]:
            game_over = False
            
            pos_x, pos_y = 350, 350
            pos2_x, pos2_y = 250, 350
            mixer.music.play(-1)
            screen.blit(scale_background, (0, 0))
        
        pygame.display.flip()
        clock.tick(60)
        continue
                   
    keys = pygame.key.get_pressed()
    
    #Player Movement   
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
    
    player_rect.topleft = (pos_x, pos_y)
        
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
        
    #Backgroung
    screen.blit(scale_background, (0, 0))
    
    #Stars
    for star in stars[:]:
        pygame.draw.circle(screen, (255, 251, 0), (int(star["posx"]), int(star["posy"])), 10)
        
        if player_rect.colliderect(star["rect"]):
                print("YOU grabed 1 Coin!")
                coins += 1
                stars.remove(star)

    #Star Hitbox
    screen.blit(scale_police, (pos2_x, pos2_y))     

    if fliped:
        screen.blit(fliped_tief, (pos_x, pos_y)) 
    else:
        screen.blit(scale_tief, (pos_x, pos_y))
    
    if int(pos2_y) == int(pos_y) and int(pos2_x) == int(pos_x):
        game_over = True 
        mixer.music.stop()
    
    if coins == 10:
        Win = True
        mixer.music.load("Win_Sound.mp3")
        mixer.music.set_volume(10)
        mixer.music.play()
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
