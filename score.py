# -*- encoding: utf-8 -*-

# Juego del Ahorcado
# UD 3. Diseño de programas
# Programación y Computación - 2º BTO
# IES Mar Serena - Curso 2021 / 2022

# Módulo encargado de gestionar a los jugadores, sus puntuaciones, y el proceso de guardar
# y cargar sus datos en el programa.

# Se define el nombre del fichero de datos.
FICHERO_DATOS = "datos_ahorcado.dat"

from persistencia import f_cargar, f_guardar

def f_crear_jugador(nick, datos):
    """Funcion que crea un jugador de nombre 'nick' y lo incluye en la estructura datos
     datos = {'nick' : numero_partidas_ganadas, 'nick1': 3, ...}

     Devuelve:

     (True, datos) Si se ha creado el jugador correctamente, y lo devuelve insertado en datos
     (False, "El jugador ya existe") Si el jugador ya existe"""

    if nick in datos:
        ret = False, "El jugador ya existe"
    else:
        datos[nick] = 0
        ret = True, datos

    return ret

def f_jugador_gana(nick, datos):
    """Funcion que incrementa en una partida ganada el score del jugador nick
    Devuelve la estructura de los datos con la modificacion hecha."""

    if nick in datos: datos[nick] += 1

    return datos

def f_cargar_jugadores():
    """Funcion que devuelve los datos del disco en json, y si hay error devuelve
    la estructura de datos de jugadores vacia"""

    try:
        ret = f_cargar(FICHERO_DATOS)
    except:
        ret = {}

    return ret

def f_guardar_jugadores(datos):
    """Funcion que guarda la estructura de datos de jugadores en disco"""

    f_guardar(datos, FICHERO_DATOS)
