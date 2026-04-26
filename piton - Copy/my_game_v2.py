import pygame, random

pygame.init()

SIRKA = 900
VYSKA = 450

BILA = (255, 255, 255)
CERNA = (0, 0, 0)

FPS = 60

clock = pygame.time.Clock()

ERYCHLOST = 11
RYCHLOST = 10

ground_height = 100
ground_grounded = VYSKA - ground_height
ground = pygame.Rect(0, ground_grounded, SIRKA, ground_height,)

okno = pygame.display.set_mode((SIRKA, VYSKA))

x_enemy = 0
y_enemy = ground_grounded

x = SIRKA 
y = 300

run = True

e_starna_l = False


jump_time = 0


velocity = 0

velocity_jump_up = -7
gravity_calc = (velocity_jump_up * -1) * 1.5
gravity = gravity_calc

jump_time_up = 0
jump_time_up_rychlost = 17


velocity_pogo_up = -7

pogo_draw = 0

pogo_time_up = 0
pogo_time_up_rychlost = 21

pogo_cooldown = 0
pogo_cooldown_rychlost = 13
pogo_cooldown_rychlost_big = 23


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

#ground = pygame.draw.rect(okno, (BILA), (SIRKA, ))

text_fail = font_big.render("GAME OVER", True, (BILA),(CERNA))
text_fail2 = font.render("press space to play again", True, (BILA),(CERNA))

text_easy = font_big.render("easy mode", True, (BILA),(CERNA))
text_easy_2 = font.render("press a ", True, (BILA),(CERNA))

text_normal = font_big.render("normal mode", True, (BILA),(CERNA))
text_normal_2 = font.render("press b ", True, (BILA),(CERNA))

text_hard = font_big.render("hard mode", True, (BILA),(CERNA))
text_hard_2 = font.render("press c ", True, (BILA),(CERNA))


easy = 1.7
normal = 2.2
hard = 3

slash_delitel = normal


slash = pygame.image.load("slash_sword.png").convert_alpha()


time = 0
time_show = 0
air_time = 0
air_time_show = 0
max_air_time = 0


cube_height = 69

menu_run = True

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    while menu_run:
        while menu_run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    menu_run = False
                    break


            keys = pygame.key.get_pressed()
            okno.fill(CERNA)


            print(menu_run,)
            okno.blit(text_easy, (230, 20))
            okno.blit(text_easy_2, (260, 60))

            okno.blit(text_normal, (210, 90))
            okno.blit(text_normal_2, (260, 130))

            okno.blit(text_hard, (230, 160))
            okno.blit(text_hard_2, (260, 200))

            pygame.display.update()
            if keys[pygame.K_a]:
                difficulty = ("easy")
                menu_run = False
                slash_delitel = easy
                slash_offset = 90
                slash = pygame.transform.scale(slash, (slash.get_width() // slash_delitel, slash.get_height() // slash_delitel))
                slash_hitbox = slash.get_rect()
                slash_hitbox.topright = (x + 20, y - 10)
                slash.set_colorkey((BILA))
            if keys[pygame.K_b]:
                difficulty = ("normal")
                menu_run = False
                slash_delitel = normal
                slash_offset = 30
                slash = pygame.transform.scale(slash, (slash.get_width() // slash_delitel, slash.get_height() // slash_delitel))
                slash_hitbox = slash.get_rect()
                slash_hitbox.topright = (x + 20, y - 10)
                slash.set_colorkey((BILA))
            if keys[pygame.K_c]:
                difficulty = ("hard")
                menu_run = False
                slash_delitel = hard
                slash_offset = 20
                slash = pygame.transform.scale(slash, (slash.get_width() // slash_delitel, slash.get_height() // slash_delitel))
                slash_hitbox = slash.get_rect()
                slash_hitbox.topright = (x + 20, y - 10)
                slash.set_colorkey((BILA))



    time += 1

    if time % 60 == 0 :
        time_show += 1


    if y != ground_grounded:
        air_time += 1
    else: 
        air_time = 0
        air_time_show = 0

    if air_time == 0:
        air_time_show = 0
    if air_time > 66 :
        air_time_show = air_time // 60
        if air_time_show > max_air_time :
            max_air_time = air_time_show



    keys = pygame.key.get_pressed()


    # print(y)
    print(jump_time_up, pogo_time_up, air_time_show, air_time)


    run = True

    
    if pogo_cooldown > 0 :
        pogo_cooldown -= 1



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
        if y == ground_grounded :
            if y == VYSKA - ground_height:
                jump_time_up = jump_time_up_rychlost
                print("jump")


    if jump_time_up > 0 :
        print("minus",jump_time_up)
        jump_time_up -= 1
        velocity = velocity_jump_up
        






    if enemy_hitbox_fake.left < 0 :
        e_starna_l = False
    
    if enemy_hitbox_fake.right > SIRKA :
        e_starna_l = True

    
    if keys[pygame.K_UP]:
        if pogo_cooldown == 0 :
            pogo_cooldown = pogo_cooldown_rychlost
            pogo_draw = 3




#------------------------------------------------code----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    if pogo_time_up > 0:
            pogo_time_up -= 1
            velocity = velocity_pogo_up



    if e_starna_l:
        x_enemy -= ERYCHLOST
    else:
        x_enemy += ERYCHLOST


    if jump_time_up == 0 and pogo_time_up == 0:
        velocity += gravity

#-----------------------------------------grafika-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




    # pygame.draw.rect(okno, (BILA), cube_hitbox, 1)


    # enemy_hitbox_real = pygame.draw.rect(okno, (255, 0, 0), (x_enemy_hitbox, y_enemy_hitbox, 120, 50), 1)

    # pygame.draw.rect(okno, (255, 0, 0), cube_hitbox, 1)


    okno.fill((CERNA))
    okno.fill((50, 50, 50), ground)

    if y != ground_grounded and pogo_time_up < 1 and jump_time_up < 1:
        velocity = gravity


    y += velocity

    if y < cube_height:
        y = cube_height

    if y > VYSKA - ground_height:
        y = VYSKA - ground_height



    cube_hitbox.bottomright = (x, y)
    x_enemy_hitbox = enemy_hitbox_fake.left + 4
    y_enemy_hitbox = enemy_hitbox_fake.top + 25
    enemy_hitbox_fake.bottomleft = (x_enemy, y_enemy)

    enemy_hitbox_real = pygame.Rect(x_enemy_hitbox, y_enemy_hitbox, 120, 50)
    if pogo_draw > 0 :
        slash_hitbox.topright = (x + slash_offset, y - 10)
        okno.blit(slash, slash_hitbox)
        pogo_draw -= 1


    pogo_w_enemy = slash_hitbox.colliderect(enemy_hitbox_fake) 

    if pogo_w_enemy:
        if pogo_draw == 2:
            pogo_time_up = pogo_time_up_rychlost
            pogo_cooldown = pogo_cooldown_rychlost_big




    if e_starna_l:
        okno.blit(enemy_left, enemy_hitbox_fake)
    else:
        okno.blit(enemy, enemy_hitbox_fake)

    okno.blit(cube, cube_hitbox)


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
                y_enemy = ground_grounded
                x = SIRKA 
                y = ground_grounded
                time = 0
                time_show = 0



    text_time = font.render("difficulty : " + str(difficulty) + "   time : " + str(time_show) + "    max air time : " + str(max_air_time), True, (BILA), (CERNA))
    okno.blit(text_time, (320, 20))

    if air_time > 60 :
        text_air_time = font.render("air time " + str(round(air_time_show, 1)), True, (BILA), (CERNA))
        okno.blit(text_air_time, (450, 60))




    pygame.display.update()
    clock.tick(FPS)
pygame.quit()