import pygame, time
from pygame import display, event, image

pygame.init()
okno = display.set_mode([1200, 800])


def obrabotka_sobitiy():
    # ОБРАБОТКА СОБЫТИЙ
    spisok_sobitiy = event.get()
    for sobitie in spisok_sobitiy:
        if sobitie.type == pygame.QUIT:
            exit()


def risovanie_kadra():
    okno.blit(fon_gori, [0, 0])
    pygame.display.flip()


fon_gori = image.load("kartynky/fon gori.jpg")

while 20 == 20:
    time.sleep(1 / 60)
    obrabotka_sobitiy()
    risovanie_kadra()