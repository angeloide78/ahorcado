#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

# Juego del Ahorcado
# UD 3. Diseño de programas
# Programación y Computación - 2º BTO
# IES Mar Serena - Curso 2021 / 2022

# Módulo de inicio del juego.

from gestion import f_gestion

def main():
    while True:
        if not f_gestion(): break

if __name__ == '__main__':
    main()