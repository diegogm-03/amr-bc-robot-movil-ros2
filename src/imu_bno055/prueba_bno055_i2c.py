#!/usr/bin/env python3

"""
Prueba de funcionamiento de la IMU BNO055 mediante I2C.

Robot móvil AMR-BC - Trabajo Fin de Grado
Autor: Diego Luis García Montoya

Este script permite validar la comunicación entre la Raspberry Pi 5
y la IMU BNO055, mostrando en tiempo real diferentes medidas del sensor:
temperatura, orientación Euler, aceleración, velocidad angular y campo magnético.
"""

import time
import board
import busio
import adafruit_bno055


def main():
    # Inicialización del bus I2C de la Raspberry Pi 5
    i2c = busio.I2C(board.SCL, board.SDA)

    # Inicialización del sensor BNO055
    sensor = adafruit_bno055.BNO055_I2C(i2c)

    print("====================================")
    print(" PRUEBA DE FUNCIONAMIENTO BNO055")
    print("====================================")
    print("Pulse Ctrl + C para finalizar la prueba.")

    try:
        while True:
            print("\nTemperatura:")
            print(sensor.temperature)

            print("\nOrientación Euler (Heading, Roll, Pitch):")
            print(sensor.euler)

            print("\nAceleración (m/s^2):")
            print(sensor.acceleration)

            print("\nVelocidad angular - Giroscopio (rad/s):")
            print(sensor.gyro)

            print("\nCampo magnético - Magnetómetro (uT):")
            print(sensor.magnetic)

            print("\n------------------------------------")

            time.sleep(1)

    except KeyboardInterrupt:
        print("\nPrueba finalizada por el usuario.")


if __name__ == "__main__":
    main()
