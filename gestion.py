# -*- encoding: utf-8 -*-

# Juego del Ahorcado
# UD 3. Diseño de programas
# Programación y Computación - 2º BTO
# IES Mar Serena - Curso 2021 / 2022

# Módulo de gestión del juego.

from pantallas import f_pantalla_principal, f_error, f_acercade, f_pedir_palabra, \
    f_despedida, f_letras, f_pedir_letra, f_horca, f_finalizar, f_pedir_resolver, \
    f_pedir_usuario, f_visualizar_score
from score import f_crear_jugador, f_guardar_jugadores, f_cargar_jugadores, f_jugador_gana

def f_jugar(ranking):
    '''Función que implementa el juego del ahorcado'''
    
    # Control de errores.
    for i in ranking: ranking[i] = 0
    # Si no hay jugadores, incluimos el jugador anónimo.
    if len(ranking) == 0: ranking = {'anonimo':0}
    
    # Palabra secreta.
    palabra = f_pedir_palabra()
    palabra = palabra.upper()
    nletras = len(palabra)
    
    if nletras > 0:

        # Creamos la lista de letras de la palabra secreta.
        l = []
        i = 0
        while i < nletras:
            l.append(None)
            i += 1
        
        # ALGG 14-12-2021 Iteramos para cada jugador.
        b_finalizar = False
        
        # Jugadores eliminados.
        j_elim = 0
                
        while True:
            # Si se finaliza, salimos totalmente.
            if b_finalizar: break
            
            # Vamos iterando por cada jugador.
            for jugador in ranking:
                # Si se eliminaron todos los jugadores, se termina.
                if j_elim >= len(ranking): 
                    b_finalizar= True
                    break
                
                # Si se finaliza, salimos totalmente.
                if b_finalizar: break
                
                # Si el jugador ya perdió todas sus posibilidades, lo eliminamos.
                if ranking[jugador] == 9: 
                    j_elim += 1
                    continue
                            
                while True:
                    f_letras(l)
                    
                    # Pedimos letra, y la ponemos en mayúscula.
                    letra_candidata = f_pedir_letra(jugador).upper()
        
                    # ALGG 13-12-2021. Se intenta resolver la palabra.
                    if letra_candidata.lower() == "quiero resolver":
                        if palabra == f_pedir_resolver().upper():
                            f_finalizar(0, palabra)
                            # Recuperamos datos y aumentamos score al jugador.
                            datos = f_cargar_jugadores()
                            datos = f_jugador_gana(jugador, datos)
                            f_guardar_jugadores(datos)
                            b_finalizar = True
                            break
                        else:
                            # Fallo al intentar resolver.
                            f_horca(ranking[jugador], jugador)
                            ranking[jugador] += 1
                            break
                    else:
                        # ALGG 12-12-2021. Se quiere salir de la partida.
                        if letra_candidata.lower() == "salir partida":
                            b_finalizar = True
                            break
                        else:
                            # ALGG 14-12-2021. Si la letra ya se comprobo, hay error.
                            if letra_candidata in l:
                                f_horca(ranking[jugador], jugador)
                                ranking[jugador] += 1          
                                break
                            else:
                                # Se comprueba si está en la palabra secreta.
                                if not letra_candidata in palabra:
                                    f_horca(ranking[jugador], jugador)
                                    ranking[jugador] += 1        
                                    break
                                else:
                                    # Buscamos la letra candidata para ver si existe, y en qué posiciones.
                                    p = 0
                                    while p < nletras:
                                        if letra_candidata == palabra[p]:
                                            # Hay una coincidencia, por lo que lo incluimos...
                                            l[p] = letra_candidata
                                        p += 1
        
                    # Comprobamos si nos han ahorcado o hemos ganado.
                    if ranking[jugador] == 9:
                        f_finalizar(1, palabra)
                        break
                    
                    elif None not in l:
                        f_finalizar(0, palabra)
                        # Recuperamos datos y aumentamos score al jugador.
                        datos = f_cargar_jugadores()
                        datos = f_jugador_gana(jugador, datos)
                        f_guardar_jugadores(datos)
                        b_finalizar = True
                        break

def f_gestion():
    """Función de gestión del juego"""

    ret = True
    
    op = f_pantalla_principal()
    
    if op in ['1', '2', '3', '4' ,'5', '0']:
        
        # Salimos de la aplicación.
        if op == '0':
            f_despedida()
            ret = False
        
        # Acerca de...
        if op == '4':
            f_acercade()
            
        # Jugar.
        if op == '2':
            RANKING = f_cargar_jugadores()
            f_jugar(RANKING)

        # Visualizar resultados.
        if op == '3':
            RANKING = f_cargar_jugadores()
            f_visualizar_score(RANKING)

        # Crear jugadores.
        if op == '1':
            nick = f_pedir_usuario()
            RANKING = f_cargar_jugadores()
            flag, RANKING = f_crear_jugador(nick, RANKING)
            # Si hay un error, se informa.
            if not flag: f_error()
            else:
                # Guardamos el jugador.
                f_guardar_jugadores(RANKING)
                
    else:
        f_error()
    
    return ret    
    
  