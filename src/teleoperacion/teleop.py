#!/usr/bin/env python3

"""
Teleoperación básica del robot móvil AMR-BC.

Robot móvil AMR-BC - Trabajo Fin de Grado
Autor: Diego Luis García Montoya

Este script permite controlar el robot mediante teclado desde la Raspberry Pi 5.
Los comandos se envían por comunicación serie a la OpenRB-150, que se encarga
del control de los motores DYNAMIXEL XL430.
"""

import time
import serial
import keyboard


PUERTO_SERIE = "/dev/ttyACM0"
BAUDRATE = 115200
TIEMPO_ENTRE_COMANDOS = 0.2


def main():
    puerto = serial.Serial(PUERTO_SERIE, BAUDRATE)

    print("======================================")
    print(" TELEOPERACIÓN ROBOT AMR-BC")
    print("======================================")
    print("W: adelante")
    print("S: atrás")
    print("A: izquierda")
    print("D: derecha")
    print("X: parar")
    print("Ctrl + C: salir")
    print("--------------------------------------")

    try:
        while True:
            if keyboard.is_pressed("w"):
                puerto.write(b"w")
                print("adelante")
                time.sleep(TIEMPO_ENTRE_COMANDOS)

            elif keyboard.is_pressed("s"):
                puerto.write(b"s")
                print("atrás")
                time.sleep(TIEMPO_ENTRE_COMANDOS)

            elif keyboard.is_pressed("a"):
                puerto.write(b"a")
                print("izquierda")
                time.sleep(TIEMPO_ENTRE_COMANDOS)

            elif keyboard.is_pressed("d"):
                puerto.write(b"d")
                print("derecha")
                time.sleep(TIEMPO_ENTRE_COMANDOS)

            elif keyboard.is_pressed("x"):
                puerto.write(b"x")
                print("stop")
                time.sleep(TIEMPO_ENTRE_COMANDOS)

    except KeyboardInterrupt:
        print("\nFinalizando teleoperación...")
        puerto.write(b"x")

    finally:
        puerto.close()
        print("Puerto serie cerrado.")


if __name__ == "__main__":
    main()
