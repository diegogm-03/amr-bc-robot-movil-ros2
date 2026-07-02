# LiDAR RPLIDAR C1

Esta carpeta contiene los archivos utilizados para la validación del sensor RPLIDAR C1 mediante ROS 2 y RViz2.

El LiDAR se comunica con la Raspberry Pi 5 mediante UART, empleando el puerto `/dev/ttyAMA0` y una velocidad de comunicación de `460800 baudios`.

La alimentación del LiDAR se realiza externamente mediante un convertidor DC-DC LM2596 de 12 V a 5 V. La conexión UART se emplea únicamente para la comunicación de datos.
