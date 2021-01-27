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
    # pygame.draw.rect(okno, [255, 0, 0], lou, 3)
    pygame.display.flip()


fon_gori = image.load("kartynky/fon gori.jpg")
knopka_nastroiki = image.load("kartynky/knopka_nastroiki.png")
knopka_nastroiki = help.izmeni_kartinku(knopka_nastroiki, 74, 74, [0, 168, 243], 1)
lou = pygame.Rect(0, 0, 74, 74)
knopka_pushek = image.load("kartynky/knopka_pushek.png")
knopka_pushek = help.izmeni_kartinku(knopka_pushek, 74, 74, [0, 168, 243], 1)
kollet = pygame.Rect(85, 0, 74, 74)

while 20 == 20:
    time.sleep(1 / 60)
    obrabotka_sobitiy()
    risovanie_kadra()
