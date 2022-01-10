# -*- encoding: utf-8 -*-

# Juego del Ahorcado
# UD 3. Diseño de programas
# Programación y Computación - 2º BTO
# IES Mar Serena - Curso 2021 / 2022

# Módulo de pantallas, peticiones de información y gráficos del juego.

import pwinput
# import getpass

def f_letras(letras):
    '''Función que visualiza las posiciones de las letras'''
    
    cadena = "La palabra contiene las siguientes letras: "
    
    for letra in letras:
    
        if letra is None: 
            cadena += "_ "
        else:
            cadena += "{} ".format(letra.upper())
    
    print(cadena)
    
    return None
    
def f_despedida():
    '''Función que visualiza la despedida del programa'''
    
    cadena = '''
    
    ==> El Ahorcado <== 
    
   Vuelve pronto!!!
   '''
    
    print(cadena)
    
    return None

def f_acercade():
    '''Función que visualiza el Acerca de... del programa'''
    
    cadena = '''
    
    ==> El Ahorcado <== 
    
         Juego del Ahorcado
  Programación y Computación - 2º BTO
   IES Mar Serena - Curso 2021 / 2022
   '''
    
    print(cadena)
    f_continuar()
    
    return None

def f_pantalla_principal():
    '''Función que presenta la pantalla principal del programa, y devuelve la opción introducida'''
    
    cadena = '''
    
    ==> El Ahorcado <== 
    
    1) Crear un jugador nuevo.
    2) Jugar.
    3) Visualizar resultados.
    4) Acerca de...
    0) Salir
    
    ==> '''
    
    ret = input(cadena)
    
    return ret

def f_error():
    '''Función que devuelve un error al introducir un dato'''
        
    cadena = '''
    
    ==> El Ahorcado <== 
    
    ERROR: El dato introducido no es correcto...'''
    
    print(cadena)
    f_continuar()
    
    return None

def f_continuar():
    '''Función que espera a que pulsemos cualquier tecla para continuar'''
    
    cadena = "Pusla cualquier tecla para continuar..."
    
    input(cadena)
    
    return None

def f_pedir_usuario():
    '''Función que pide la inserción de un nombre de usuario, y lo devuelve'''
    
    cadena = '''
    
    ==> El Ahorcado <== 
    
    Nombre del nuevo jugador: '''
    
    ret = input(cadena)
    
    return ret
  
def f_pedir_palabra():
    '''Función que pide la palabra secreta, y la devuelve'''
    
    cadena = '''
    
    ==> El Ahorcado <== 
    
    Palabra: '''
    # ret = getpass.getpass(prompt=cadena)
    ret = pwinput.pwinput(prompt=cadena)
    return ret  

def f_pedir_letra(jugador):
    '''Función que pide la inserción de una letra, y la devuelve'''
    
    cadena = '''
    ==> El Ahorcado <== 

                Turno para el jugador {}   
                
    - Si quieres resolver la palabra escribe "quiero resolver" (sin comillas)
    - Si quieres salir de la partida escribe "salir partida" (sin comillas)
    
    Introduce una letra: '''.format(jugador)
    
    ret = input(cadena)
    
    return ret
    
def f_pedir_resolver():
    '''Función que pide una palabra para intentar resolver, y la devuelve'''
    
    cadena = '''
    
    ==> El Ahorcado <== 
    
    Introduce la palabra para resolver la partida: '''
    
    ret = input(cadena)
    
    return ret

# def f_ganador(palabra):
#     cadena = '''
#
#     HAS ACERTADO!!!! La palabra secreta es {}
#     '''.format(palabra.lower())
#
#     print(cadena)
#     f_continuar()
#
#     return None
#
# def f_perdedor(palabra):
#     cadena = '''
#
#     HAS PERDIDO!!!! La palabra secreta es {}
#     '''.format(palabra.lower())
#
#     print(cadena)
#     f_continuar()
#
#    return None

def f_finalizar(opcion, palabra):
    '''Funcion de finalizacion.
    opcion es 0 visualiza el mensaje ganador
    opcion es 1 visualiza el mensaje perdedor'''

    if opcion == 0:
        cadena = '''
    
         HAS ACERTADO!!!! La palabra secreta es {}
         '''.format(palabra.lower())

    if opcion == 1:
        cadena = '''

          HAS PERDIDO!!!! La palabra secreta es {}
          '''.format(palabra.lower())

    print(cadena)
    f_continuar()

    return None

def f_visualizar_score(jugadores):
    '''Función que visualiza el resultado de los jugadores'''
    
    cadena = '''
    
    ==> El Ahorcado <== 
    
    Resultado de los jugadores
    --------------------------'''
    
    linea = ""
    for i in jugadores: 
        linea += "\n{} - Partidas ganadas: {}".format(i, jugadores[i])
    cadena += linea

    if jugadores == {}: cadena = "No hay jugadores dados de alta"
    
    print(cadena)
    f_continuar()

    return None

def f_horca(opcion, jugador = ""):
    '''Función que visualiza la horca, a partir de la opción pasada como parámetro
    Valores de opcion:
    0 : Pinta la base de la horca.
    1 : El caso 0 y pinta el palo vertical.
    2 : El caso 1 y pinta el palo horizontal superior.
    3 : El caso 2 y pinta la cabeza ahoracada.
    4 : El caso 3 y pinta el tronco del ahorcado.
    5 : El caso 4 y pinta el brazo izquierdo.
    6 : El caso 5 y pinta el brazo derecho.
    7 : El caso 6 y pinta la pierna izquieda.
    8 : El caso 7 y pinta la pierna derecha. AHORCADO!!!
    '''
    
    if int(opcion) == 0:
        cadena = '''... han puesto el tablón de abajo...
        
        
        
        
        
        ________
        '''
    elif int(opcion) == 1:
        cadena = '''... acaban de poner el palo vertical... ándate con ojo...
        
            |
            |
            |
            | 
        ____|____
        '''        
    elif int(opcion) == 2:
        cadena = '''... uff.. el palo de arriba está listo... siente tu muerte...
        
            |----
            |
            |
            | 
        ____|____
        '''        
    elif int(opcion) == 3:
        cadena = '''... Ostras!!!! tu cabeza pende de un hilo...
        
            |----
            |   *
            |
            | 
        ____|____
        '''        
    elif int(opcion) == 4:
        cadena = '''... te veo degadito... 
        
            |----
            |   *
            |   |
            | 
        ____|____
        '''        
    elif int(opcion) == 5:
        cadena = '''... el manco de Lepanto... colega... estás fastidiado...
        
            |----
            |   *
            |   |-
            | 
        ____|____
        '''        
    elif int(opcion) == 6:
        cadena = '''... ¿haciendo palmas? Espabila que vas a perder!!!
        
            |----
            |   *
            |  -|-
            | 
        ____|____
        '''        
    elif int(opcion) == 7:
        cadena = '''... a la siguiente te vas al paredón....
        
            |----
            |   *
            |  -|- 
            |  /
        ____|____
        '''        
    elif int(opcion) == 8:
        cadena = '''... te han dejado colgado...
        
            |----
            |   *
            |  -|- 
            |  / \ 
        ____|____
        '''        

    cadena = "{} {}".format(jugador, cadena) 
    print(cadena)
    return None