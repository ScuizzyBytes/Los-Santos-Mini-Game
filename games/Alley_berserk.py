import os
import random
import sys

import pygame

pygame.init()

WALK_ANIM = "/home/misha/Los-Santos-Mini-Game/9GAMES/assests/images/Alley_berserk/walk_anim"
ATAK_ANIM = "/home/misha/Los-Santos-Mini-Game/9GAMES/assests/images/Alley_berserk/attack_anim"

background = pygame.image.load("9GAMES/assests/images/Alley_berserk/background.png")
people_px = pygame.image.load("9GAMES/assests/images/Alley_berserk/people.png")
blood_px = pygame.image.load("9GAMES/assests/images/Alley_berserk/blood.png")

scaled_background = pygame.transform.scale(background, (1408, 768))
scaled_people = pygame.transform.scale(people_px, (50, 60))
scaled_blood = pygame.transform.scale(blood_px, (70, 70))

scaled_people.set_colorkey((255, 255, 255))
scaled_blood.set_colorkey((255, 255, 255))

W, H = 1408, 768
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
attacking = False
attacking_index = 0

names = sorted(
    f for f in os.listdir(WALK_ANIM)
    if f.startswith("pixel_frame") and f.lower().endswith(".png")
)
print(names)

frames = []
for name in names:
    img_anim = pygame.image.load(os.path.join(WALK_ANIM, name)).convert_alpha()
    frames.append(pygame.transform.scale(img_anim, (80, 80)))
    
attacking_anim = sorted(
    n for n in os.listdir(ATAK_ANIM)
    if n.startswith("pixel_attack") and n.lower().endswith(".png")
)
print(attacking_anim)

frames1 = []
for name1 in attacking_anim:
    img_anim2 = pygame.image.load(os.path.join(ATAK_ANIM, name1)).convert_alpha()
    frames1.append(pygame.transform.scale(img_anim2, (80, 80)))

x, y = 170, 170
flip = False
running = True

peoples = []
for j in range(20):
    posx = random.randint(200, W - 200)
    posy = random.randint(0, H)
    peoples.append({"posx": posx, "posy": posy})
    
def blood_squash(blood):
    if flip:
        screen.blit(pygame.transform.flip(blood, True, False), (x - 20, y))
    else:
        screen.blit(blood, (x + 50, y))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            attacking = True
            attacking_index = 0
            
    keys = pygame.key.get_pressed()
    moving = False
    
    index1 = (pygame.time.get_ticks() // 80) % len(frames1) if moving else 0
    sprite2 = pygame.transform.flip(frames1[index1], flip, False)
    
    if not attacking:
        if keys[pygame.K_a]:
            x -= 2
            flip = True
            moving = True
        if keys[pygame.K_d]:
            x += 2
            flip = False
            moving = True
        if keys[pygame.K_s]:
            y += 2
            moving = True
        if keys[pygame.K_w]:
            y -= 2
            moving = True
        
    screen.blit(scaled_background, (0, 0))
    
    for people in peoples:
        screen.blit(scaled_people, (people["posx"], people["posy"]))
    
    if attacking and not flip:
        attacking_index += 0.3
        blood_squash(scaled_blood)
        if attacking_index >= len(frames1):
            attacking = False
            attacking_index = 0
        current_sprite = frames1[int(attacking_index)]
    else:
        index = (pygame.time.get_ticks() // 80) % len(frames) if moving else 0
        current_sprite = frames[index]
        
    
    sprite_to_draw = pygame.transform.flip(current_sprite, flip, False)
    
    screen.blit(sprite_to_draw, (x, y))
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()
sys.exit()