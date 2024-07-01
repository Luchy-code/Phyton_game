import pygame
from pygame.locals import *
from configuracion import *


def dameLetraApretada(key):
    if key == K_a:
        return("a")
    elif key == K_b:
        return("b")
    elif key == K_c:
        return("c")
    elif key == K_d:
        return("d")
    elif key == K_e:
        return("e")
    elif key == K_f:
        return("f")
    elif key == K_g:
        return("g")
    elif key == K_h:
        return("h")
    elif key == K_i:
        return("i")
    elif key == K_j:
        return("j")
    elif key == K_k:
        return("k")
    elif key == K_l:
        return("l")
    elif key == K_m:
        return("m")
    elif key == K_n:
        return("n")
    elif key == K_o:
        return("o")
    elif key == K_p:
        return("p")
    elif key == K_q:
        return("q")
    elif key == K_r:
        return("r")
    elif key == K_s:
        return("s")
    elif key == K_t:
        return("t")
    elif key == K_u:
        return("u")
    elif key == K_v:
        return("v")
    elif key == K_w:
        return("w")
    elif key == K_x:
        return("x")
    elif key == K_y:
        return("y")
    elif key == K_z:
        return("z")
    elif key == K_SPACE:
       return(" ")
    else:
        return("")


def escribirEnPantalla(screen, palabra, posicion, tamano, color):
    fuente=pygame.font.SysFont("Bernard MT",30)
    ren = fuente.render(palabra, 1, color)
    screen.blit(ren, posicion)

def dibujar(screen, candidata, listaIzq, listaMedio, listaDer, posicionesIzq ,
                posicionesMedio, posicionesDer, puntos,segundos):

    fuente=pygame.font.SysFont("Bernard MT",30)

    #Linea del piso
    pygame.draw.line(screen, (255,255,255), (0, ALTO-70) , (ANCHO, ALTO-70), 5)

    #linea vertical
    pygame.draw.line(screen, (255,255,255), (ANCHO//3, ALTO-70) , (ANCHO//3, 0), 5)

    #linea vertical
    pygame.draw.line(screen, (255,255,255), (2*ANCHO//3, ALTO-70) , (2*ANCHO//3, 0), 5)

    ren1 = fuente.render(candidata, 1, COLOR_TEXTO)
    ren2 = fuente.render("Puntos: " + str(puntos), 1, COLOR_TEXTO)

    if(segundos<11):
            ren3 = fuente.render("Tiempo: " + str(int(segundos)), 1, COLOR_TIEMPO_FINAL)
    else:
        if(segundos<31):
            ren3 = fuente.render("Tiempo: " + str(int(segundos)), 1, COLOR_TIEMPO_MEDIO)
        else:
            ren3 = fuente.render("Tiempo: " + str(int(segundos)), 1, COLOR_TEXTO)

##    pal=fuente.render("hola",1,30)
##    screen.blit(pal,(100,100))

    for i in range(len(listaIzq)):
        screen.blit(fuente.render(listaIzq[i], 1, COLOR_LETRAS), posicionesIzq[i])
    for i in range(len(listaMedio)):
        screen.blit(fuente.render(listaMedio[i], 1, COLOR_LETRAS), posicionesMedio[i])
    for i in range(len(listaDer)):
        screen.blit(fuente.render(listaDer[i], 1, COLOR_LETRAS), posicionesDer[i])

    screen.blit(ren1, (190, 570))
    screen.blit(ren2, (680, 10))
    screen.blit(ren3, (10, 10))

PRIMER_LINEA_VERTICAL = ANCHO//3
SEGUNDA_LINEA_VERTICAL = ANCHO//3*2