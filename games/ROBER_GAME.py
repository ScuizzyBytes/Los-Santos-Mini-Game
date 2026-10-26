import random

import pygame

pygame.init()
pygame.mixer.init()

W, H = 800, 700

music = pygame.mixer.music.load("9GAMES/assests/sounds/background2.mp3")
pygame.mixer.music.set_volume(0.2)

pygame.mixer.music.play(-1)

#Displays
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Los Santos")
running = True
clock = pygame.time.Clock()
fliped = True
#Images 
coins_image = pygame.image.load("9GAMES/assests/images/coin.png").convert_alpha()
police_img = pygame.image.load("9GAMES/assests/images/police.png").convert_alpha()
me_img = pygame.image.load("9GAMES/assests/images/tief.png").convert_alpha()
background = pygame.image.load("9GAMES/assests/images/background.jpg").convert()
icon = pygame.image.load("9GAMES/assests/images/Icon.png").convert_alpha()
icon.set_colorkey((0, 0, 0))
coins_image.set_colorkey((255, 255, 255))

icon = pygame.display.set_icon(icon)

me_img.set_colorkey((255, 255, 255))
police_img.set_colorkey("#F5CDFF")

scale_police = pygame.transform.scale(police_img, (60, 70))
scale_tief = pygame.transform.scale(me_img, (60, 70))
scale_background = pygame.transform.scale(background, (W, H))
scale_coins = pygame.transform.scale(coins_image, (30, 30))

small_bg = pygame.transform.smoothscale(scale_background, (W // 10, H // 10))
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
police_rect = pygame.Rect(pos2_x, pos2_y, 60, 70)

#Stars Creating
stars = []
coins = []

for _ in range(20):
    posx = random.randint(50, W - 50)
    posy = random.randint(50, H - 50)
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

        try:    
            pygame.display.update()
        except pygame.error:
            print("You left")
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
        pygame.mixer.music.pause()
        
        coins.clear()
        stars.clear()
        
        screen.blit(text_surface, (240, 150))
        screen.blit(text_surface2, (200, 250))
        
        screen.blit(scale_police, (pos2_x, pos2_y))
        
        if keys2[pygame.K_q]:
            game_over = False
            
            pos_x, pos_y = 350, 350
            pos2_x, pos2_y = 250, 350
            pygame.mixer.music.unpause()
            
            for _ in range(20):
                posx = random.randint(50, W - 50)
                posy = random.randint(50, H - 50)
                stars.append({"rect": pygame.Rect(posx, posy, 20, 20),
                              "posx": posx,
                              "posy": posy})
            
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
    police_rect.topleft = (pos2_x, pos2_y)
        
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
        screen.blit(scale_coins, star["rect"].topleft)
        
        if player_rect.colliderect(star["rect"]):
                print("YOU grabed 1 Coin!")
                coins.append(1)
                stars.remove(star)
        
        if player_rect.colliderect(police_rect):
            game_over = True

    #Police Hitbox
    screen.blit(scale_police, (pos2_x, pos2_y))     

    if fliped:
        screen.blit(fliped_tief, (pos_x, pos_y)) 
    else:
        screen.blit(scale_tief, (pos_x, pos_y))
    
    if int(pos2_y) == int(pos_y) and int(pos2_x) == int(pos_x):
        game_over = True 
        pygame.mixer.music.pause()
    
    if len(coins) == 20:
        Win = True
        pygame.mixer.music.load("9GAMES/assests/sounds/Win_Sound.mp3")
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.play()
    
    pygame.display.flip()
    clock.tick(60)

print("You left!")
pygame.quit()
