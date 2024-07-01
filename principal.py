#! /usr/bin/env python
import os, random, sys, math

import pygame
from pygame.locals import *

from configuracion import *
from funcionesVACIAS import *
from extras import *

#Funcion principal
def main():
        #Centrar la ventana y despues inicializar pygame
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        pygame.init()
        #pygame.mixer.init()

        #Preparar la ventana
        pygame.display.set_caption("Armar palabras...")
        screen = pygame.display.set_mode((ANCHO, ALTO))

        #tiempo total del juego
        gameClock = pygame.time.Clock()
        totaltime = 0
        segundos = TIEMPO_MAX
        fps = FPS_inicial

        puntos = 0
        candidata = ""
        listaIzq = []
        listaMedio = []
        listaDer = []
        posicionesIzq = []
        posicionesMedio = []
        posicionesDer = []
        lista = []

        with open("lemarioMasCorto.txt","r") as archivo:
            no="\n"
            abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
            for linea in archivo:
                lista.append(linea)                       #cargo las palabras
                for caracter in range(len(lista)):
                    lista[caracter] = lista[caracter].replace(no,"")    #le saco /n, y lo reemplazo por un espacio
                    for dato in range(len(abc)):
                        if lista[caracter]==abc[dato]:                  #reviso si el elemento de la lista es igual al de la lista abc
                            lista[caracter] = lista[caracter].replace(abc[dato],"")    #aquellos elemento que sean iguales los remmplazo por un espacio
                    if lista[caracter]=="":                             # elimino cualquier carcater que sea igual a un espacio
                        lista.pop(caracter)

##        archivo= open("lemario.txt","r")
##        for linea in archivo.readlines():
##            lista.append(linea[0:-1])


        cargarListas(lista, listaIzq, listaMedio, listaDer, posicionesIzq , posicionesMedio, posicionesDer)
        dibujar(screen, candidata, listaIzq, listaMedio, listaDer, posicionesIzq ,
                posicionesMedio, posicionesDer, puntos,segundos)

        while segundos > fps/1000:
        # 1 frame cada 1/fps segundos
            gameClock.tick(fps)
            totaltime += gameClock.get_time()

            if True:
            	fps = 3

            #Buscar la tecla apretada del modulo de eventos de pygame
            for e in pygame.event.get():

                #QUIT es apretar la X en la ventana
                if e.type == QUIT:
                    pygame.quit()
                    return()

                #Ver si fue apretada alguna tecla
                if e.type == KEYDOWN:
                    letra = dameLetraApretada(e.key)
                    candidata += letra
                    if e.key == K_BACKSPACE:
                        candidata = candidata[0:len(candidata)-1]
                    if e.key == K_RETURN:
                        puntos += procesar(lista, candidata, listaIzq, listaMedio, listaDer, posicionesIzq, posicionesMedio, posicionesDer)
                        candidata = ""

            segundos = TIEMPO_MAX - pygame.time.get_ticks()/1000

            #Limpiar pantalla anterior
            screen.fill(COLOR_FONDO)

            #Dibujar de nuevo todo
            dibujar(screen, candidata, listaIzq, listaMedio, listaDer, posicionesIzq ,
                posicionesMedio, posicionesDer, puntos,segundos)

            pygame.display.flip()

            actualizar(lista, listaIzq, listaMedio, listaDer, posicionesIzq,
                posicionesMedio, posicionesDer)

        while 1:
            #Esperar el QUIT del usuario
            for e in pygame.event.get():
                if e.type == QUIT or segundos<=1:
                    pygame.quit()
                    return

##Programa Principal ejecuta Main
if __name__ == "__main__":
    main()
