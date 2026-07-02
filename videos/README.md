# Vídeos de validación

Esta carpeta contiene los enlaces a los vídeos de validación y demostración del robot móvil **AMR-BC**.

Los vídeos se encuentran alojados en YouTube para evitar subir archivos pesados directamente al repositorio.

## Demostraciones disponibles

### Teleoperación del robot

Prueba de control manual del robot mediante teclado, verificando el movimiento de los motores DYNAMIXEL y la respuesta del sistema en tiempo real.

[Ver vídeo en YouTube](https://www.youtube.com/shorts/N6F5oDQjqJE)

---

### Lectura de la IMU BNO055

Validación de la comunicación I2C entre la Raspberry Pi 5 y la IMU BNO055, obteniendo datos de orientación, aceleración, giroscopio y magnetómetro.

[Ver vídeo en YouTube](https://www.youtube.com/shorts/N6F5oDQjqJE?feature=share)

---

### Validación del LiDAR RPLIDAR C1 en RViz2

Prueba de adquisición de datos del sensor RPLIDAR C1 mediante ROS 2 y visualización del escaneo 2D en RViz2.

[Ver vídeo en YouTube](https://www.youtube.com/watch?v=fPHqbw8lGJI)

---

### Teleoperación y escaneo LiDAR en tiempo real

Prueba conjunta donde el robot se controla por teleoperación mientras el LiDAR actualiza en tiempo real la representación del entorno en RViz2.

[Ver vídeo en YouTube](https://www.youtube.com/shorts/moTShs6l5g4?feature=share)

## Resumen de validaciones

| Prueba | Elementos validados |
|---|---|
| Teleoperación | Raspberry Pi 5, OpenRB-150 y motores DYNAMIXEL |
| IMU BNO055 | Comunicación I2C y lectura de datos inerciales |
| LiDAR en RViz2 | Comunicación UART, ROS 2 y visualización de `/scan` |
| Teleoperación + LiDAR | Funcionamiento conjunto de percepción y actuación |
