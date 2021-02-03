import pygame, time, help
from pygame import display, event, image, transform

pygame.init()
okno = display.set_mode([700, 800])


def obrabotka_sobitiy():
    # ОБРАБОТКА СОБЫТИЙ
    spisok_sobitiy = event.get()
    for sobitie in spisok_sobitiy:
        if sobitie.type == pygame.QUIT:
            exit()
        if sobitie.type == pygame.MOUSEBUTTONDOWN:
            if sobitie.button == 1:
                print(sobitie.pos)

                if lou.collidepoint(sobitie.pos) == 1:
                    print("nastroiki")
                if kollet.collidepoint(sobitie.pos) == 1:
                    print("pushka")


def risovanie_kadra():
    okno.blit(fon_gori, [0, 0])
    okno.blit(knopka_nastroiki, lou)
    okno.blit(knopka_pushek, kollet)
    okno.blit(ball_attack, [100, 100])
    pygame.display.flip()


def sdelay_nazvanie_igri():
    f = pygame.font.SysFont("comicsansms", 100, False, True)
    gavs = f.render("ball attack", True, [43, 219, 133])
    amber = pygame.transform.rotate(gavs, 10)
    return amber


fon_gori = image.load("kartynky/fon gori.jpg")
knopka_nastroiki = image.load("kartynky/knopka_nastroiki.png")
knopka_nastroiki = help.izmeni_kartinku(knopka_nastroiki, 74, 74, [0, 168, 243], 1)
lou = pygame.Rect(0, 0, 74, 74)
knopka_pushek = image.load("kartynky/knopka_pushek.png")
knopka_pushek = help.izmeni_kartinku(knopka_pushek, 74, 74, [0, 168, 243], 1)
kollet = pygame.Rect(85, 0, 74, 74)
ball_attack = sdelay_nazvanie_igri()

while 20 == 20:
    time.sleep(1 / 60)
    obrabotka_sobitiy()
    risovanie_kadra()
