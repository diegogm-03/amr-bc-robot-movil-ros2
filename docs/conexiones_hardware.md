# Conexiones hardware del robot AMR-BC

Este documento resume las principales conexiones hardware utilizadas en el robot móvil AMR-BC.

## Raspberry Pi 5 - RPLIDAR C1

| Señal RPLIDAR C1 | Raspberry Pi 5 |
|---|---|
| TX | RX GPIO15 / Pin 10 |
| RX | TX GPIO14 / Pin 8 |
| GND | GND |

El RPLIDAR C1 se comunica con la Raspberry Pi 5 mediante UART, empleando el puerto `/dev/ttyAMA0` y una velocidad de comunicación de `460800 baudios`.

La alimentación del LiDAR se realiza externamente mediante un convertidor DC-DC LM2596 de 12 V a 5 V. Por tanto, la conexión UART se emplea únicamente para comunicación de datos.

## Raspberry Pi 5 - IMU BNO055

| Señal IMU BNO055 | Raspberry Pi 5 |
|---|---|
| VIN | 3.3 V |
| GND | GND |
| SDA | GPIO2 / Pin 3 |
| SCL | GPIO3 / Pin 5 |

La IMU BNO055 se comunica con la Raspberry Pi 5 mediante el bus I2C, siendo la Raspberry Pi el maestro del bus.

## Raspberry Pi 5 - OpenRB-150

| Elemento | Conexión |
|---|---|
| Raspberry Pi 5 | USB |
| OpenRB-150 | `/dev/ttyACM0` |
| Baudrate | `115200` |

La Raspberry Pi 5 envía comandos de teleoperación por USB serie hacia la OpenRB-150.

## OpenRB-150 - Motores DYNAMIXEL XL430

Los motores DYNAMIXEL XL430 comparten un bus TTL común de alimentación y datos, conectados físicamente en cadena.

| Elemento | Descripción |
|---|---|
| Motor izquierdo | ID `1` |
| Motor derecho | ID `2` |
| Protocolo | DYNAMIXEL Protocol 2.0 |
| Baudrate | `57600` |
| Modo de operación | Velocidad |

La OpenRB-150 actúa como maestro de comunicación del bus DYNAMIXEL TTL.

## Sistema de alimentación

| Subsistema | Alimentación |
|---|---|
| Raspberry Pi 5 | Power bank USB-C con Power Delivery |
| Motores DYNAMIXEL | Bus principal de 12 V |
| OpenRB-150 | Bus de 12 V compartido con los motores |
| RPLIDAR C1 | Convertidor DC-DC LM2596 de 12 V a 5 V |
| IMU BNO055 | 3.3 V desde Raspberry Pi 5 |

El sistema separa la alimentación de potencia, destinada a motores y periféricos, de la alimentación de computación, destinada exclusivamente a la Raspberry Pi 5.
