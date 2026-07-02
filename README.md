# AMR-BC: Robot móvil modular de bajo coste

![ROS 2](https://img.shields.io/badge/ROS%202-Humble-blue)
![Python](https://img.shields.io/badge/Python-3.x-yellow)
![Platform](https://img.shields.io/badge/Platform-Raspberry%20Pi%205-red)
![Status](https://img.shields.io/badge/Status-Validated-success)
![License](https://img.shields.io/badge/License-MIT-green)

![Robot AMR-BC](images/robot_final.jpg)

## Descripción

Este repositorio recoge el desarrollo software, el diseño mecánico y parte de la documentación técnica del robot móvil **AMR-BC**, una plataforma robótica modular de bajo coste desarrollada como Trabajo Fin de Grado en Ingeniería Electrónica Industrial y Automática.

El proyecto integra diseño mecánico mediante impresión 3D, electrónica de control, sensorización, comunicación hardware-software y validación funcional mediante ROS 2.

La plataforma está basada en una **Raspberry Pi 5**, un controlador **OpenRB-150**, motores **DYNAMIXEL XL430**, un sensor **RPLIDAR C1**, una IMU **BNO055** y una arquitectura de alimentación separada para potencia y computación.

## Características principales

- Robot móvil de bajo coste con arquitectura modular.
- Chasis y soportes diseñados mediante CAD e impresión 3D.
- Control de motores DYNAMIXEL XL430 mediante bus TTL.
- Comunicación entre Raspberry Pi 5 y OpenRB-150.
- Integración del LiDAR RPLIDAR C1 mediante UART.
- Lectura de la IMU BNO055 mediante I2C.
- Visualización de datos LiDAR en ROS 2 y RViz2.
- Pruebas de teleoperación y validación percepción-actuación.
- Separación entre alimentación de potencia y alimentación de computación.
- Archivos STL y SolidWorks incluidos para documentación y fabricación mecánica.

## Arquitectura del sistema

El robot se estructura en los siguientes subsistemas:

| Subsistema | Elementos principales |
|---|---|
| Computación | Raspberry Pi 5 |
| Control de actuadores | OpenRB-150 |
| Actuación | Motores DYNAMIXEL XL430 |
| Percepción | RPLIDAR C1 e IMU BNO055 |
| Alimentación | Batería de 12 V y power bank USB-C PD |
| Software | Debian, Docker, ROS 2 Humble, Python y RViz2 |
| Diseño mecánico | Piezas CAD, STL y SolidWorks |

## Demostraciones

A continuación se muestran algunas pruebas realizadas durante la validación del robot móvil AMR-BC.

### Teleoperación del robot

Prueba de control manual del robot mediante teclado, verificando el movimiento de los motores DYNAMIXEL y la respuesta del sistema en tiempo real.

[Ver vídeo en YouTube](https://www.youtube.com/shorts/N6F5oDQjqJE)

### Lectura de la IMU BNO055

Validación de la comunicación I2C entre la Raspberry Pi 5 y la IMU BNO055, obteniendo datos de orientación, aceleración, giroscopio y magnetómetro.

[Ver vídeo en YouTube](https://www.youtube.com/shorts/N6F5oDQjqJE?feature=share)

### Validación del LiDAR en RViz2

Prueba de adquisición de datos del sensor RPLIDAR C1 mediante ROS 2 y visualización del escaneo 2D en RViz2.

[Ver vídeo en YouTube](https://www.youtube.com/watch?v=fPHqbw8lGJI)

### Teleoperación y escaneo LiDAR en tiempo real

Prueba conjunta donde el robot se controla por teleoperación mientras el LiDAR actualiza en tiempo real la representación del entorno en RViz2.

[Ver vídeo en YouTube](https://www.youtube.com/shorts/moTShs6l5g4?feature=share)

## Estructura del repositorio

```text
.
├── docs/                          # Esquemas, imágenes y documentación auxiliar
├── src/                           # Código fuente del robot
│   ├── lidar/
│   │   └── iniciar_lidar_rviz.sh
│   ├── imu_bno055/
│   │   └── prueba_bno055_i2c.py
│   ├── teleoperacion/
│   │   ├── iniciar_teleop.sh
│   │   └── teleop.py
│   └── openrb_dynamixel/
│       └── teleop_test.ino
├── ros2/                          # Configuración ROS 2, launch y RViz
├── cad/                           # Archivos CAD y piezas imprimibles
│   ├── stl/                       # Modelos STL preparados para impresión 3D
│   └── solidworks/                # Archivos editables originales de SolidWorks
├── images/                        # Imágenes utilizadas en el README
├── videos/                        # Enlaces a vídeos de validación
├── .gitignore
├── README.md
└── LICENSE
```

## Código incluido

El repositorio incluye los principales scripts utilizados durante la validación funcional del robot móvil AMR-BC.

| Archivo | Descripción |
|---|---|
| `src/lidar/iniciar_lidar_rviz.sh` | Script de arranque del RPLIDAR C1 y RViz2 dentro del contenedor Docker. |
| `src/imu_bno055/prueba_bno055_i2c.py` | Script de prueba para validar la comunicación I2C con la IMU BNO055. |
| `src/teleoperacion/iniciar_teleop.sh` | Script de inicio de la teleoperación desde la Raspberry Pi 5. |
| `src/teleoperacion/teleop.py` | Programa principal de control por teclado, enviando comandos serie a la OpenRB-150. |
| `src/openrb_dynamixel/teleop_test.ino` | Código cargado en la OpenRB-150 para controlar los motores DYNAMIXEL XL430. |

## Diseño mecánico

El repositorio también incluye archivos CAD relacionados con el diseño mecánico del robot.

| Carpeta | Descripción |
|---|---|
| `cad/stl/` | Archivos STL preparados para laminado e impresión 3D. |
| `cad/solidworks/` | Archivos originales editables de SolidWorks. |

Las piezas mecánicas incluyen soportes, elementos estructurales, llantas, neumáticos y piezas auxiliares diseñadas para la integración física de los componentes del robot.

Los archivos `.stl` están orientados a la fabricación mediante impresión 3D, mientras que los archivos de SolidWorks permiten editar y adaptar la geometría original de las piezas.

## Ejecución básica

### Teleoperación

Para iniciar la teleoperación desde la Raspberry Pi 5:

```bash
./iniciar_teleop.sh
```

El script comprueba la conexión de la OpenRB-150 en `/dev/ttyACM0`, arranca el contenedor Docker `tfg_robot_movimiento` y ejecuta el programa `teleop.py`.

Los comandos utilizados son:

| Tecla | Acción |
|---|---|
| `W` | Avance |
| `S` | Retroceso |
| `A` | Giro a la izquierda |
| `D` | Giro a la derecha |
| `X` | Parada |

### LiDAR y RViz2

Para lanzar el sistema de percepción mediante el RPLIDAR C1 y visualizar los datos en RViz2:

```bash
./iniciar_lidar_rviz.sh
```

El script arranca el contenedor `tfg_lidar_rviz_arm64`, ejecuta el nodo `sllidar_ros2` y abre RViz2 con la configuración guardada.

Los parámetros utilizados para el LiDAR son:

| Parámetro | Valor |
|---|---|
| Puerto serie | `/dev/ttyAMA0` |
| Baudrate | `460800` |
| Frame ID | `laser` |
| Inverted | `false` |
| Angle compensate | `true` |

La comunicación del RPLIDAR C1 con la Raspberry Pi 5 se realiza mediante UART. La alimentación del LiDAR se proporciona externamente mediante un convertidor DC-DC LM2596 de 12 V a 5 V, por lo que la conexión UART se emplea únicamente para comunicación de datos.

### IMU BNO055

Para comprobar la lectura de la IMU BNO055 mediante I2C:

```bash
python3 prueba_bno055_i2c.py
```

El script muestra en tiempo real datos de temperatura, orientación Euler, aceleración, giroscopio y magnetómetro.

La conexión utilizada es:

| Señal IMU BNO055 | Raspberry Pi 5 |
|---|---|
| VIN | 3.3 V |
| GND | GND |
| SDA | GPIO2 / Pin 3 |
| SCL | GPIO3 / Pin 5 |

## Conexiones principales

### RPLIDAR C1

| Señal RPLIDAR C1 | Raspberry Pi 5 |
|---|---|
| TX | RX GPIO15 / Pin 10 |
| RX | TX GPIO14 / Pin 8 |
| GND | GND |

El RPLIDAR C1 se comunica mediante UART, empleando el puerto `/dev/ttyAMA0`.

### IMU BNO055

| Señal IMU BNO055 | Raspberry Pi 5 |
|---|---|
| VIN | 3.3 V |
| GND | GND |
| SDA | GPIO2 / Pin 3 |
| SCL | GPIO3 / Pin 5 |

La Raspberry Pi 5 actúa como maestro del bus I2C.

### OpenRB-150 y DYNAMIXEL XL430

| Elemento | Descripción |
|---|---|
| Controlador | OpenRB-150 |
| Motores | DYNAMIXEL XL430 |
| Bus | DYNAMIXEL TTL |
| Motor izquierdo | ID `1` |
| Motor derecho | ID `2` |
| Baudrate DYNAMIXEL | `57600` |
| Comunicación Raspberry Pi 5 - OpenRB-150 | USB serie `/dev/ttyACM0` |

La OpenRB-150 actúa como maestro de comunicación del bus DYNAMIXEL TTL y controla los motores conectados físicamente en cadena.

## Estado del proyecto

El sistema ha sido validado a nivel de integración hardware-software, teleoperación, lectura de IMU y visualización de datos LiDAR en RViz2.

Actualmente, el robot permite:

- Control manual mediante teleoperación.
- Comunicación entre Raspberry Pi 5 y OpenRB-150.
- Control de motores DYNAMIXEL XL430.
- Lectura de datos de la IMU BNO055 mediante I2C.
- Visualización del entorno mediante RPLIDAR C1 en RViz2.
- Separación entre alimentación de potencia y alimentación de computación.
- Consulta de archivos mecánicos para impresión 3D y edición CAD.

Como líneas futuras se plantea la integración completa de la IMU en ROS 2, la implementación de navegación autónoma, la caracterización experimental de la autonomía y la mejora de la arquitectura software mediante paquetes ROS 2 específicos.

## Autor

**Diego Luis García Montoya**  
Grado en Ingeniería Electrónica Industrial y Automática  
Universidad de Almería

## Licencia

Este proyecto se distribuye bajo licencia MIT. Consulte el archivo `LICENSE` para más información.
