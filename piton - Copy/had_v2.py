import pygame, random

pygame.init()

SIRKA = 300
VYSKA = 450

BILA = (255, 255, 255)
CERNA = (0, 0, 0)

FPS = 5

clock = pygame.time.Clock()


RYCHLOST = 10
smer = 3

okno = pygame.display.set_mode((SIRKA, VYSKA))


back_cikl = 0


x_hlava = 150
y_hlava = 300

x_telo = x_hlava
y_telo = y_hlava - 10

had = [(150, 300), (150, 290)]



x_jablko = random.randrange(0, SIRKA // 10)
y_jablko = random.randrange(0, VYSKA // 10)

x_jablko *= 10
y_jablko *= 10


run = True

back_ct_x = 0
back_ct_y = 0

back_ctverec = pygame.Rect(back_ct_x, back_ct_y, 10, 10)



font = pygame.font.SysFont(None, 24)
font_big = pygame.font.SysFont(None, 48)

text_fail = font_big.render("GAME OVER", True, (BILA),(CERNA))
text_fail2 = font.render("press space to play again", True, (BILA),(CERNA))


#ground = pygame.draw.rect(okno, (BILA), (SIRKA, ))

text_fail = font_big.render("GAME OVER", True, (BILA),(CERNA))
text_fail2 = font.render("press space to play again", True, (BILA),(CERNA))

text_easy = font_big.render("easy mode", True, (BILA),(CERNA))
text_easy_2 = font.render("press a ", True, (BILA),(CERNA))

text_normal = font_big.render("normal mode", True, (BILA),(CERNA))
text_normal_2 = font.render("press b ", True, (BILA),(CERNA))

text_hard = font_big.render("hard mode", True, (BILA),(CERNA))
text_hard_2 = font.render("press c ", True, (BILA),(CERNA))

for_cikl_cislo = 1350

menu_run = True

running = True

back_run = True


had_hlava = pygame.Rect(x_hlava, y_hlava, 10, 10) 
had_telo = pygame.Rect(x_telo,y_telo, 10, 10)
jablko = pygame.Rect(x_jablko, y_jablko, 10, 10)

speed_cooldown = 0 

x_hlava_tmp = x_hlava 
y_hlava_tmp = y_hlava + 10
tela = [[x_hlava_tmp, y_hlava_tmp], [x_hlava_tmp, y_hlava_tmp + 10], [x_hlava_tmp, y_hlava_tmp + 20], [x_hlava_tmp, y_hlava_tmp + 30], [x_hlava_tmp, y_hlava_tmp + 40], [x_hlava_tmp, y_hlava_tmp + 50], [x_hlava_tmp, y_hlava_tmp + 60], [x_hlava_tmp, y_hlava_tmp + 70]]
true_collision = False


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    print(x_hlava, y_hlava, x_hlava_tmp, y_hlava_tmp, tela)

    speed_cooldown += 1 

    run = True


    keys = pygame.key.get_pressed() 


    if keys[pygame.K_d]:
        if smer != 1 :
            smer = 2

    if keys[pygame.K_a]:
        if smer != 2 :
            smer = 1

    if keys[pygame.K_s]:
        if smer != 3 :
            smer = 4

    if keys[pygame.K_w]:
        if smer != 4 :
            smer = 3





    x_hlava_tmp = x_hlava
    y_hlava_tmp = y_hlava
    if smer == 1:
        x_hlava -= RYCHLOST
    elif smer== 1: x_hlava -= RYCHLOST
    elif smer== 2: x_hlava += RYCHLOST
    elif smer== 4: y_hlava += RYCHLOST
    elif smer== 3: y_hlava -= RYCHLOST

    for i in range(len(tela)):
        print(i)
        i_poradi = (len(tela) - i) - 1
        if i_poradi != 0:
            tela[i_poradi] = tela[i_poradi - 1]
        else: tela[0] = [x_hlava_tmp, y_hlava_tmp]
        print(i_poradi)
            





    




    okno.fill((CERNA))


    # while back_run :
    #     back_cikl += 1
    #     if back_ct_x > VYSKA :
    #         back_ct_x = 0
    #         back_ct_y += 10
    #     if back_ct_x % 20 == 0 and back_ct_y % 20 == 0 or back_ct_x % 20 != 0 and back_ct_y % 20 != 0 :

    #         okno.fill((BILA), back_ctverec)
    #     else: okno.fill((CERNA), back_ctverec)
    #     back_ctverec = pygame.Rect(back_ct_x, back_ct_y, 10, 10)
    #     # okno.fill((0, 0, 255), back_ctverec)
    #     back_ct_x += 10
    #     # okno.fill((200, 200, 255), back_ctverec)
    #     if back_run == 1350: back_run = False



    # if speed_cooldown == 20:
    #     x_hlava += X_RYCHLOST
    #     y_hlava += Y_RYCHLOST
    #     speed_cooldown = 0
       
    collision = had_hlava.colliderect(had_telo)
    eat = had_hlava.colliderect(jablko)

    

    if collision or true_collision or x_hlava < 0 or x_hlava >= SIRKA or y_hlava < 0 or y_hlava >= VYSKA:
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    run = False
            keys = pygame.key.get_pressed()
            okno.fill(CERNA)

            okno.blit(text_fail, (50, 80))
            okno.blit(text_fail2, (53, 140))

            pygame.display.update()
            if keys[pygame.K_SPACE]:
                run = False 
                X_RYCHLOST = 0
                Y_RYCHLOST = -10
                                
                x_hlava = 150
                y_hlava = 300

                x_telo = x_hlava
                y_telo = y_hlava - 10

                x_jablko = random.randrange(0, SIRKA // 10)
                y_jablko = random.randrange(0, VYSKA // 10)

                x_jablko *= 10
                y_jablko *= 10
                had = [(150, 300), (150, 290)]
                x_hlava_tmp = x_hlava 
                y_hlava_tmp = y_hlava + 10
                tela = [[x_hlava_tmp, y_hlava_tmp]]
                true_collision = False


                



    if eat :

        x_jablko = random.randrange(0, SIRKA // 10) * 10
        y_jablko = random.randrange(0, VYSKA // 10) * 10
        eat_tela_len = len(tela) - 1


        if smer== 1:
            tela.append([tela[eat_tela_len][0] + RYCHLOST, tela[eat_tela_len][1]])
        elif smer== 2: tela.append([tela[eat_tela_len][0] - RYCHLOST, tela[eat_tela_len][1]])
        elif smer== 4: tela.append([tela[eat_tela_len][0], tela[eat_tela_len][1] - RYCHLOST])
        elif smer== 3: tela.append([tela[eat_tela_len][0], tela[eat_tela_len][1] + RYCHLOST])



    had_hlava = pygame.Rect(x_hlava, y_hlava, 10, 10) 
    # had_telo = pygame.Rect(x_telo,y_telo, 10, 10)
    jablko = pygame.Rect(x_jablko, y_jablko, 10, 10)


    okno.fill((0, 255, 0), had_hlava)


    for s in range(len(tela)):

        had_telo = pygame.Rect(tela[s][0], tela[s][1], 10, 10)
        if s % 2 == 0 :
            okno.fill((0, 200, 0), had_telo)
        else: okno.fill((0, 255, 0), had_telo)
        collision = had_hlava.colliderect(had_telo)
        if collision:
            true_collision = True
        


    okno.fill((255, 0, 0), jablko)

    # back_run = True

    print(x_hlava, y_hlava, tela, collision)



    pygame.display.update()
    clock.tick(FPS)
pygame.quit()