# OpenRB-150 y motores DYNAMIXEL

Esta carpeta contiene el código cargado en la placa **OpenRB-150** para el control de los motores **DYNAMIXEL XL430** del robot móvil **AMR-BC**.

La OpenRB-150 recibe comandos desde la Raspberry Pi 5 mediante comunicación serie USB y actúa como maestro del bus DYNAMIXEL TTL, enviando las órdenes de velocidad a los motores.

## Archivo principal

- `teleop_test.ino`: programa cargado en la OpenRB-150. Recibe comandos por puerto serie desde la Raspberry Pi 5 y controla la velocidad de los motores DYNAMIXEL.

## Funcionamiento general

El sistema funciona de la siguiente manera:

1. La Raspberry Pi 5 ejecuta el script de teleoperación `teleop.py`.
2. El usuario pulsa una tecla de movimiento.
3. La Raspberry Pi envía un carácter por USB serie a la OpenRB-150.
4. La OpenRB-150 interpreta el carácter recibido.
5. La OpenRB-150 envía la orden correspondiente a los motores DYNAMIXEL XL430 mediante el bus TTL.

## Comandos utilizados

| Comando recibido | Acción |
|---|---|
| `w` | Avance |
| `s` | Retroceso |
| `a` | Giro a la izquierda |
| `d` | Giro a la derecha |
| `x` | Parada |

## Parámetros del sistema

| Parámetro | Valor |
|---|---|
| Controlador | OpenRB-150 |
| Motores | DYNAMIXEL XL430 |
| Motor izquierdo | ID `1` |
| Motor derecho | ID `2` |
| Protocolo DYNAMIXEL | `2.0` |
| Baudrate bus DYNAMIXEL | `57600` |
| Baudrate comunicación USB | `115200` |
| Modo de operación | Velocidad |
| Puerto DYNAMIXEL | `Serial1` |
| Puerto USB serie | `Serial` |

## Lógica de movimiento

| Acción | Motor izquierdo | Motor derecho |
|---|---:|---:|
| Avance | `50` | `-50` |
| Retroceso | `-50` | `50` |
| Giro izquierda | `-50` | `-50` |
| Giro derecha | `50` | `50` |
| Parada | `0` | `0` |

La diferencia de signo entre ambos motores se debe a su disposición física en el robot, ya que se encuentran montados enfrentados dentro de la arquitectura de tracción diferencial.

## Código utilizado

El archivo `teleop_test.ino` emplea la librería `Dynamixel2Arduino` para configurar los motores en modo velocidad y enviar órdenes de movimiento en función del comando recibido por puerto serie.

## Validación

La validación consistió en comprobar que los comandos enviados desde la Raspberry Pi 5 producían la respuesta esperada en los motores DYNAMIXEL, permitiendo el avance, retroceso, giro y parada del robot mediante teleoperación.
