import pygame, random

pygame.init()

SIRKA = 900
VYSKA = 400

BILA = (255, 255, 255)
CERNA = (0, 0, 0)

FPS = 60

clock = pygame.time.Clock()

ERYCHLOST = 10
RYCHLOST = 10


jump_rychlost = 10
jump_time_rychlost = 35


okno = pygame.display.set_mode((SIRKA, VYSKA))

x_enemy = 0
y_enemy = 300

x = SIRKA 
y = 300

run = True

e_starna_l = False


jump_time = 0
jump_y = 0


font = pygame.font.SysFont(None, 24)
font_big = pygame.font.SysFont(None, 48)

text_fail = font_big.render("GAME OVER", True, (BILA),(CERNA))
text_fail2 = font.render("press space to play again", True, (BILA),(CERNA))


enemy = pygame.image.load("enemy.png")
enemy = pygame.transform.scale(enemy, (enemy.get_width() // 2, enemy.get_height() // 2))
enemy.set_colorkey((69, 69, 69))
enemy_hitbox_fake = enemy.get_rect()
enemy_hitbox_fake.bottomleft = (x_enemy, y_enemy)

enemy_left = pygame.transform.flip(enemy,True,False)
enemy_left.set_colorkey((69, 69, 69))

#enemy_hitbox_real = pygame.draw.rect(okno, (255, 0, 0), (0,0, -100, -50), 1)

cube = pygame.image.load("cube.webp")
cube = pygame.transform.scale(cube, (cube.get_width() // 10, cube.get_height() // 10))
cube_hitbox = cube.get_rect()
cube_hitbox.bottomright = (x, y)

ground = pygame.Rect(0, 300, SIRKA, 100 )
#ground = pygame.draw.rect(okno, (BILA), (SIRKA, ))




running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break


    keys = pygame.key.get_pressed()


    print(jump_time)


    run = True

    




#----------------------------------------------ifs---------------------------------------------------------------------------------------------------------------------------------------------------------------------------


    if keys[pygame.K_a]:
        if cube_hitbox.left < 0:
            pass
        else:
            x -= RYCHLOST
            print("left")

    if keys[pygame.K_d]:
        if cube_hitbox.right > SIRKA:
            pass
        else:
            x += RYCHLOST
            print("right")


    if keys[pygame.K_SPACE]:
        if jump_time == 0:
            jump_time = jump_time_rychlost
            print("jump")
        pass

    if jump_time > 0 :
        if jump_time > jump_time_rychlost // 2.5 :
            jump_y -= jump_rychlost
            y = jump_y + 300
            jump_time -= 1
        else: 
            jump_y += jump_rychlost * 1.5
            y = jump_y + 300
            jump_time -= 1



    if enemy_hitbox_fake.left < 0 :
        e_starna_l = False
    
    if enemy_hitbox_fake.right > SIRKA :
        e_starna_l = True


#------------------------------------------------code----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



    if e_starna_l:
        x_enemy -= ERYCHLOST
    else:
        x_enemy += ERYCHLOST


    

#-----------------------------------------grafika-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


    okno.fill((CERNA))
    okno.fill((50, 50, 50), ground)


    enemy_hitbox_fake.bottomleft = (x_enemy, y_enemy)
    if e_starna_l:
        okno.blit(enemy_left, enemy_hitbox_fake)
    else:
        okno.blit(enemy, enemy_hitbox_fake)

    cube_hitbox.bottomright = (x, y)
    okno.blit(cube, cube_hitbox)
    # pygame.draw.rect(okno, (BILA), cube_hitbox, 1)


    x_enemy_hitbox = enemy_hitbox_fake.left + 4
    y_enemy_hitbox = enemy_hitbox_fake.top + 25

    enemy_hitbox_real = pygame.Rect(x_enemy_hitbox, y_enemy_hitbox, 120, 50)
    # enemy_hitbox_real = pygame.draw.rect(okno, (255, 0, 0), (x_enemy_hitbox, y_enemy_hitbox, 120, 50), 1)

    # pygame.draw.rect(okno, (255, 0, 0), cube_hitbox, 1)
 
    collision_w_enemy = cube_hitbox.colliderect(enemy_hitbox_real)

    if collision_w_enemy:
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    run = False
            keys = pygame.key.get_pressed()
            okno.fill(CERNA)

            okno.blit(text_fail, (350, 80))
            okno.blit(text_fail2, (353, 140))

            pygame.display.update()
            if keys[pygame.K_SPACE]:
                run = False 
                x_enemy = 0
                y_enemy = 300
                x = SIRKA 
                y = 300










    pygame.display.update()
    clock.tick(FPS)
pygame.quit()