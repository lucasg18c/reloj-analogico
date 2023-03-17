import pygame as pg
from pygame import display
from pygame import event
from pygame import draw
from pygame import time
from time import localtime
from math import pi, cos, sin

class COLOR:
    blanco = 255, 255, 255
    negro = 0, 0, 0

LADO = 400
PADDING = 50
CENTRO = LADO / 2
RADIO = CENTRO - PADDING
ANCHO_BORDE = 1
LARGO_HORA = int(RADIO * .5)
LARGO_MINUTOS = int(RADIO * .9)
LARGO_SEGUNDOS = int(RADIO * .8)
ANCHO_HORA = 3
ANCHO_MINUTOS = 3
ANCHO_SEGUNDOS = 1



class Hora():

    khora = -pi / 21600
    kmin = -pi / 1800
    kseg = -pi / 30
    pi_div_2 = pi / 2
    pi_por_2 = 2 * pi

    def __init__(self) -> None:
        self.lt = localtime()
        self.punta_hora_x = 0
        self.punta_hora_y = 0
        self.punta_minutos_x = 0
        self.punta_minutos_y = 0
        self.punta_segundos_x = 0
        self.punta_segundos_y = 0

    def actualizar(self):
        self.lt = localtime()

        seg = self.lt[5]
        min = 60 * self.lt[4] + seg
        hora = 3600 * (self.lt[3] % 12) + min

        angulo = self.pi_div_2 + self.khora * hora
        if angulo < 0:
            angulo += self.pi_por_2

        self.punta_hora_x = CENTRO + cos(angulo) * LARGO_HORA
        self.punta_hora_y = CENTRO - sin(angulo) * LARGO_HORA

        angulo = self.pi_div_2 + self.kmin * min
        if angulo < 0:
            angulo += self.pi_por_2

        self.punta_minutos_x = CENTRO + cos(angulo) * LARGO_MINUTOS
        self.punta_minutos_y = CENTRO - sin(angulo) * LARGO_MINUTOS

        angulo = self.pi_div_2 + self.kseg * seg
        if angulo < 0:
            angulo += self.pi_por_2

        self.punta_segundos_x = CENTRO + cos(angulo) * LARGO_SEGUNDOS
        self.punta_segundos_y = CENTRO - sin(angulo) * LARGO_SEGUNDOS
        

def render(hora: Hora):
    ventana.fill(COLOR.blanco)

    # Borde
    draw.circle(
        ventana, 
        COLOR.negro, 
        (CENTRO, CENTRO),
        RADIO,
        ANCHO_BORDE)

    # Hora
    draw.line(
        ventana,
        COLOR.negro,
        (CENTRO, CENTRO),
        (hora.punta_hora_x, hora.punta_hora_y),
        ANCHO_HORA)

    # Minutos
    draw.line(
        ventana,
        COLOR.negro,
        (CENTRO, CENTRO),
        (hora.punta_minutos_x, hora.punta_minutos_y),
        ANCHO_MINUTOS)

    # Segundos
    draw.line(
        ventana,
        COLOR.negro,
        (CENTRO, CENTRO),
        (hora.punta_segundos_x, hora.punta_segundos_y),
        ANCHO_SEGUNDOS)

    

def main():
    global ventana

    pg.init()
    display.set_caption("Reloj")
    ventana = display.set_mode((LADO, LADO))

    clock = time.Clock()
    hora = Hora()

    run = True
    while run:

        for evento in event.get():
            if evento.type == pg.QUIT:
                run = False

        hora.actualizar()
        render(hora)
        display.flip()
        clock.tick(2)

    pg.quit()


if __name__ == "__main__":
    main()
