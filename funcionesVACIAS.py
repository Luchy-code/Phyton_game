from principal import *
from configuracion import *

import random
import math


def cargarListas(lista, listaIzq, listaMedio, listaDer, posicionesIzq, posicionesMedio, posicionesDer):
    if (len(lista)>0):  # si la lista no esta vacia pasamos a buscar la palabra aleatoria
        palabra = lista[random.randint(0, len(lista)-1)]
        palabra1=""  #trozos de la palabra
        palabra2=""  #trozos de la palabra
        palabra3=""  #trozos de la palabra
        #divison nos indica cuantas letras habra por cada columna
        if (len(palabra)>2):  #si la palabra al azar es mayor a 2
            division1= random.randint(1, len(palabra)-2)
            for i in range(division1): #hasta estenumero se va a guardar las letras en la columna
                palabra1=palabra1+palabra[i]
            for letra in palabra1:  #posiciones
                borde_desde = 1
                borde_hasta = PRIMER_LINEA_VERTICAL-15
                guardarLetraEnListas(listaIzq, posicionesIzq, letra, borde_desde, borde_hasta)

            division2= random.randint(division1+1, len(palabra)-1)
            for i in range(division1, division2):#hasta estenumero se va a guardar la las letras
                palabra2=palabra2+palabra[i]
            for letra in palabra2: #posiciones
                borde_desde = PRIMER_LINEA_VERTICAL+15
                borde_hasta = SEGUNDA_LINEA_VERTICAL-15
                guardarLetraEnListas(listaMedio, posicionesMedio, letra, borde_desde, borde_hasta)

            for i in range(division2, len(palabra)):
                palabra3=palabra3+palabra[i]
            for letra in palabra3: #posiciones
                borde_desde = SEGUNDA_LINEA_VERTICAL+15
                borde_hasta = ANCHO-15
                guardarLetraEnListas(listaDer, posicionesDer, letra, borde_desde, borde_hasta)
            print(division1,division2)
            print(palabra,palabra1,palabra2,palabra3)

def guardarLetraEnListas(lista, posiciones, letra, borde_izquierdo, borde_derecho):
    #todas las letras de la palabra al azar las mandamos para aca y armamos la lista
    pos_y = 20 #posicion y del comienzo fija
    lista.append(letra)
##    print(lista)
    pos_x = random.randint(borde_izquierdo, borde_derecho) #posicion x al azar
    posiciones.append([pos_x, pos_y]) #guardamos ambas en al lista posiciones


def bajar(lista, posiciones):
    if len(lista) > 0: #si la lista no esta vacia
        movimiento_y = 7  # velocidaddel movimiento
        for pos_x_y in posiciones:
            pos_x_y[1] += movimiento_y  # aumentamos y para que haga el bajo de bajada
            if pos_x_y[1] > ALTO-90:  # si la letra llego al piso
                lista.pop(0) #borramos la palabra de a lista y sus posiciones
                posiciones.pop(0)

def actualizar(lista, listaIzq, listaMedio, listaDer, posicionesIzq, posicionesMedio, posicionesDer):
    bajar(listaIzq, posicionesIzq)
    bajar(listaMedio, posicionesMedio)
    bajar(listaDer, posicionesDer)
    if random.randint(1, 10) == 1: #hasta no nos de 1 no vamos a agregar otra aplabra en la pantalla
        cargarListas(lista, listaIzq, listaMedio, listaDer, posicionesIzq, posicionesMedio, posicionesDer)

##def estaCerca(elem, lista):
##    #es opcional, se usa para evitar solapamientos
##    pass

def Puntos(candidata):
    vocales = "aeiou"
    cons_dificiles = "jkqwxyz"
    total_puntos = 0
    for letra in candidata:
        if letra in vocales:
            total_puntos += 1
        elif letra in cons_dificiles:
            total_puntos += 5
        else:
            total_puntos += 2
    return total_puntos

def procesar(lista, candidata, listaIzq, listaMedio, listaDer, posicionesIzq, posicionesMedio, posicionesDer):
    musica= pygame.mixer.Sound("sonido.mp3")
    if esValida(lista, candidata, listaIzq, listaMedio, listaDer, posicionesIzq, posicionesMedio, posicionesDer):
        musica.play()
        return Puntos(candidata)
    else:
        return 0
    # chequea que candidata sea correcta en cuyo caso devuelve el puntaje y 0 si no es correcta


def esValida(lista, candidata, listaIzq, listaMedio, listaDer, posicionesIzq, posicionesMedio, posicionesDer):
    if candidata in lista:
        pos_izq_usadas = []
        pos_medio_usadas = []
        pos_der_usadas = []
        col = 1  # empieza buscando desde la primer columna
        i = 0
        #index() devuelve la primera aparición / índice del elemento en la lista dada como argumento de la función
        while i < len(candidata):
            l = candidata[i]  # letra
            if col == 1:
                if l in listaIzq:
                    pos_izq_usadas.append(listaIzq.index(l))
                    i += 1
                else:
                    col = 2  # busco en la columna del medio
            elif col == 2:
                if l in listaMedio:
                    pos_medio_usadas.append(listaMedio.index(l))
                    i += 1
                else:
                    col = 3  # busco en la columna de la derecha
            else:
                if l in listaDer:
                    pos_der_usadas.append(listaDer.index(l))
                    i += 1
                else:
                    return False  # si no se encuentra en la ultima columna, no existe la letra
        borrarLetrasDeListas(listaIzq, posicionesIzq, pos_izq_usadas)
        borrarLetrasDeListas(listaMedio, posicionesMedio, pos_medio_usadas)
        borrarLetrasDeListas(listaDer, posicionesDer, pos_der_usadas)
        return True  # si se recorrio toda la palabra, es correcta
    else:
        return False  # si no es una palabra del diccionario
    # devuelve True si candidata cumple con los requisitos

def borrarLetrasDeListas(lista, posiciones, pos_usadas):
    #se hace en caso de que la candidata sea verdadera
    #La forma más sencilla de ordenar una lista en Python es utilizar el método sort() de la clase list
    pos_usadas.sort()
    cont_pop = 0
    for pos in pos_usadas:
        lista.pop(pos-cont_pop) #borramos las letras
        posiciones.pop(pos-cont_pop) #borramosla posicion
        cont_pop += 1