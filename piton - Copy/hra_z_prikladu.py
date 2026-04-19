import pygame,random,time

# 1. Inicializace (knihovny, šířka a výška okna, zobrazení okna, popisku, ikony).
pygame.init()

SIRKA = 600
VYSKA = 300

SIRKA2 = SIRKA // 2
VYSKA2 = VYSKA // 2



run = True

score = 0
lives = 5

x_coin = SIRKA
y_coin = random.randrange(35, 281)

BILA = (255, 255, 255)
CERNA = (0, 0, 0)

FPS = 60

clock = pygame.time.Clock()

RYCHLOST = 10

CRYCHLOST = 10

x = 0
y = VYSKA // 2

okno = pygame.display.set_mode((SIRKA, VYSKA))

font = pygame.font.SysFont(None, 24)
font_big = pygame.font.SysFont(None, 48)

text_fail = font_big.render("GAME OVER", True, (BILA),(CERNA))
text_fail2 = font.render("press space to play again", True, (BILA),(CERNA))

drak = pygame.image.load("dragon_right.png")
obdelnik_kolem_draka = drak.get_rect()
obdelnik_kolem_draka.center = (x, y)

coin = pygame.image.load("coin.png")
coin_hitbox = coin.get_rect()
coin_hitbox.center = (x_coin, y_coin)


# # Popisek okna. (Nepovinný)
# pygame.display.set_caption("!!!!!!!!!!!!!!!!! DOPLŇ NÁZEV OKNA !!!!!!!!!!!!!!!!!")

# # Nahrání obrázku do proměnné ikona a použití. (Nepovinná)
# ikona = pygame.image.load("dragon_right.png")
# pygame.display.set_icon(ikona)
running = True

# Herní (nekonečná) smyčka.
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
    
    # 2. Zde získáme vstupy od uživatele.

    keys = pygame.key.get_pressed()
 
    

    if keys[pygame.K_w]:
        if obdelnik_kolem_draka.top < 0:
            pass
        else:
            y -= RYCHLOST
            print("up")

    if keys[pygame.K_s]:
        if obdelnik_kolem_draka.bottom > VYSKA:
            pass
        else:
            y += RYCHLOST
            print("down")


    x_coin -= CRYCHLOST
    print(x_coin)

    run = True
    
    score_score = "score",score
    text_score = font.render("score  " + str(score), True, (BILA), (CERNA),)
    #text_score = font.render(score_score, True, (BILA),(CERNA))


    # if lives == 0:
    #     while run:
    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT:
    #                 running = False
    #                 break



           
    #         print("GAME OVER")
    #         print("C")
    #         okno.blit(text_fail, (200, 100))
    #         okno.blit(text_fail2, (200, 150))

    #         lives = 5
    #         CRYCHLOST = 5
    #         score= 0
    #         pygame.display.update()
    #         if keys[pygame.K_SPACE]:
                
    #             run = False

    if lives == 0:
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    run = False
            keys = pygame.key.get_pressed()
            okno.fill(CERNA)

            okno.blit(text_fail, (203, 80))
            okno.blit(text_fail2, (200, 140))

            pygame.display.update()
            if keys[pygame.K_SPACE]:
                run = False  # any key restarts game
                lives = 5
                score = 0
                x_coin = SIRKA
                y_coin = random.randrange(35, 281)
                CRYCHLOST = 10



    # print(lives, x_coin, skore)




    # if keys[pygame.K_d]:
    #     if obdelnik_kolem_draka.right > SIRKA:
    #         pass
    #     else:
    #         x += RYCHLOST
    #         print("right")

    # if keys[pygame.K_a]:
    #     if obdelnik_kolem_draka.left < 0:
    #         pass
    #     else:
    #         x -= RYCHLOST
    #         print("left")

    # 3. Zde akt
    # ualizujeme herní prostředí (herní postavu, ostatní postavy, ...)



    # 4. Vykreslíme nové prostředí


    okno.fill(CERNA)

    obdelnik_kolem_draka.center = (x, y)

    pygame.draw.rect(okno, (255, 255, 255), obdelnik_kolem_draka, 1)
    okno.blit(drak, obdelnik_kolem_draka)

    coin_hitbox.center = (x_coin, y_coin)
    pygame.draw.rect(okno, (255, 255, 255), coin_hitbox, 1)
    okno.blit(coin, coin_hitbox)

    collision_w_coin = obdelnik_kolem_draka.colliderect(coin_hitbox)

    okno.blit(text_score, (270, 20))




    if collision_w_coin:
        x_coin = SIRKA
        y_coin = random.randrange(35, 281)
        coin_hitbox.center = (x_coin, y_coin)
        pygame.draw.rect(okno, (255, 255, 255), coin_hitbox, 1)
        okno.blit(coin, coin_hitbox)
        score = score +1
        CRYCHLOST += 1
    

    if x_coin < 0 :
        x_coin = SIRKA
        lives = lives -1
        y_coin = random.randrange(35, 281)
        













    pygame.display.update()

    clock.tick(FPS)

pygame.quit()