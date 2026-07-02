#!/bin/bash

# Script de arranque del sistema LiDAR + RViz2
# Robot móvil AMR-BC - Trabajo Fin de Grado
# Sensor: RPLIDAR C1
# Entorno: ROS 2 Humble sobre Docker

CONTENEDOR="tfg_lidar_rviz_arm64"

echo "Dando permisos gráficos a Docker..."
xhost +local:docker >/dev/null 2>&1 || true
xhost +local:root >/dev/null 2>&1 || true

echo "Arrancando contenedor $CONTENEDOR..."
docker start "$CONTENEDOR" >/dev/null 2>&1 || true

echo "Cerrando posibles procesos anteriores..."
docker exec "$CONTENEDOR" bash -lc "pkill -f sllidar_node || true"
docker exec "$CONTENEDOR" bash -lc "pkill -f rviz2 || true"

echo "Lanzando RPLIDAR C1..."
docker exec -d "$CONTENEDOR" bash -lc "
cd /root/ros2_ws &&
source /opt/ros/humble/setup.bash &&
source install/setup.bash &&
ros2 run sllidar_ros2 sllidar_node --ros-args \
-p serial_port:=/dev/ttyAMA0 \
-p serial_baudrate:=460800 \
-p frame_id:=laser \
-p inverted:=false \
-p angle_compensate:=true \
> /tmp/lidar_c1.log 2>&1
"

sleep 4

echo "Abriendo RViz2..."

DISPLAY_ACTUAL=${DISPLAY:-:0.0}

xhost +local:docker >/dev/null 2>&1 || true
xhost +local:root >/dev/null 2>&1 || true

docker exec \
-e DISPLAY=$DISPLAY_ACTUAL \
-e QT_X11_NO_MITSHM=1 \
-e XDG_RUNTIME_DIR=/tmp/runtime-root \
-e LIBGL_ALWAYS_SOFTWARE=1 \
-e QT_OPENGL=software \
-e LIBGL_DRI3_DISABLE=1 \
-e MESA_LOADER_DRIVER_OVERRIDE=llvmpipe \
"$CONTENEDOR" bash -lc "
mkdir -p /tmp/runtime-root &&
chmod 700 /tmp/runtime-root &&

cd /root/ros2_ws &&
source /opt/ros/humble/setup.bash &&
source install/setup.bash &&

rviz2 -d /root/ros2_ws/lidar_c1_config.rviz
"
