import pygame, time
from pygame import display, event, image


def obrabotka_sobitiy():
    # ОБРАБОТКА СОБЫТИЙ
    spisok_sobitiy = event.get()

    for sobitie in spisok_sobitiy:
        if sobitie.type == pygame.QUIT:
            exit()


fon_gori = image.load("kartynky/fon gori.jpg")

display.set_mode([1200, 800])
while 20 == 20:
    time.sleep(1 / 60)
    obrabotka_sobitiy()
