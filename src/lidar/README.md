# LiDAR RPLIDAR C1

Esta carpeta contiene los archivos utilizados para la validación del sensor **RPLIDAR C1** mediante **ROS 2 Humble** y **RViz2**.

El LiDAR se comunica con la Raspberry Pi 5 mediante UART, mientras que su alimentación se realiza de forma externa mediante un convertidor DC-DC LM2596 de 12 V a 5 V. Por tanto, la conexión UART se emplea únicamente para la comunicación de datos.

## Archivo principal

- `iniciar_lidar_rviz.sh`: script de arranque utilizado para lanzar el nodo del RPLIDAR C1 dentro del contenedor Docker y abrir RViz2 con la configuración guardada.

## Parámetros utilizados

| Parámetro | Valor |
|---|---|
| Contenedor Docker | `tfg_lidar_rviz_arm64` |
| Puerto serie | `/dev/ttyAMA0` |
| Baudrate | `460800` |
| Frame ID | `laser` |
| Inverted | `false` |
| Angle compensate | `true` |
| Configuración RViz2 | `/root/ros2_ws/lidar_c1_config.rviz` |

## Comando ROS 2 utilizado

```bash
ros2 run sllidar_ros2 sllidar_node --ros-args \
-p serial_port:=/dev/ttyAMA0 \
-p serial_baudrate:=460800 \
-p frame_id:=laser \
-p inverted:=false \
-p angle_compensate:=true
