import pygame, time, help
from pygame import display, event, image, transform

pygame.init()
okno = display.set_mode([700, 800])


def obrabotka_sobitiy():
    global ekran
    # ОБРАБОТКА СОБЫТИЙ
    spisok_sobitiy = event.get()
    for sobitie in spisok_sobitiy:
        if sobitie.type == pygame.QUIT:
            exit()
        if sobitie.type == pygame.MOUSEBUTTONDOWN:
            if sobitie.button == 1:

                if lou.collidepoint(sobitie.pos) == 1:
                    ekran = "nastroiki"
                if kollet.collidepoint(sobitie.pos) == 1:
                    ekran = "pushka"


def risovanie_kadra():
    if "gl" == ekran:
        risovanie_gl()
    if "nastroiki" == ekran:
        risovanie_nastroek()
    if "pushka" == ekran:
        risovanie_pushek()


def risovanie_gl():
    okno.blit(fon, [0, 0])
    okno.blit(knopka_nastroiki, lou)
    okno.blit(knopka_pushek, kollet)
    okno.blit(ball_attack, [100, 100])
    pygame.display.flip()


def risovanie_nastroek():
    okno.fill([64, 64, 64])
    okno.blit(OK, geil)
    pygame.display.flip()


def risovanie_pushek():
    okno.fill([51, 51, 51])
    okno.blit(OK, geil)
    pygame.display.flip()


def sdelay_nazvanie_igri():
    f = pygame.font.SysFont("comicsansms", 100, False, True)  # создаём шрифт
    gavs = f.render("attack", True, [255, 90, 0])  # делаем картинку из букв
    gavs = pygame.transform.rotate(gavs, 10)  # поворачиваем картинку

    amber = f.render("Ball", True, [255, 90, 0])
    amber = pygame.transform.rotate(amber, 10)

    volt = pygame.Surface([500, 500], pygame.SRCALPHA)

    volt.blit(gavs, [100, 100])
    volt.blit(amber, [100, 50])
    return volt


fon = image.load("kartynky/fon.png")
fon = pygame.transform.scale(fon, [700, 800])
knopka_nastroiki = image.load("kartynky/knopka_nastroiki.png")
knopka_nastroiki = help.izmeni_kartinku(knopka_nastroiki, 74, 74, [0, 168, 243], 1)
lou = pygame.Rect(10, 10, 74, 74)
knopka_pushek = image.load("kartynky/knopka_pushek.png")
knopka_pushek = help.izmeni_kartinku(knopka_pushek, 74, 74, [0, 168, 243], 1)
kollet = pygame.Rect(100, 10, 74, 74)
ball_attack = sdelay_nazvanie_igri()
OK = image.load("kartynky/OK.png")
OK = help.izmeni_kartinku(OK, 80, 74, [0, 168, 243], 1)
geil = pygame.Rect(0, 0, 80, 74)
geil.centerx = 350
geil.centery = 605
ekran = "gl"

while 20 == 20:
    time.sleep(1 / 60)
    obrabotka_sobitiy()
    risovanie_kadra()
