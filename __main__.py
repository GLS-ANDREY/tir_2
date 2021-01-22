import pygame, time
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


def risovanie_kadra():
    okno.blit(fon_gori, [0, 0])
    okno.blit(knopka_nastroiki, [0, 0])
    pygame.display.flip()


fon_gori = image.load("kartynky/fon gori.jpg")
knopka_nastroiki = image.load("kartynky/knopka_nastroiki.jpg")
knopka_nastroiki = transform.scale(knopka_nastroiki, [74, 74])

while 20 == 20:
    time.sleep(1 / 60)
    obrabotka_sobitiy()
    risovanie_kadra()
