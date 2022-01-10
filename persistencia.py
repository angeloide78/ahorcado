# -*- encoding: utf-8 -*-

# Juego del Ahorcado
# UD 3. Diseño de programas
# Programación y Computación - 2º BTO
# IES Mar Serena - Curso 2021 / 2022

# Módulo de persistencia de datos.

import json

def f_guardar(datos, nomFich):
	"""Guarda estructura de datos en fichero"""
	
	# Se abre el fichero en modo escritura. 
	f = open(nomFich, "w")  
	# Guardamos estructura en el fichero.   
	json.dump(datos, f)
	# Cerramos el fichero. 
	f.close()  

	return None

def f_cargar(nomFich):
	"""Abrir fichero json"""
	
	f = open(nomFich, "r")  
	datos = json.load(f)
	f.close()
	
	# Devuelve la estructura de datos.
	return datos
