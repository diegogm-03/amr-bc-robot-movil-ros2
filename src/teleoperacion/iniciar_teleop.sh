#!/bin/bash

# Script de inicio de la teleoperación del robot móvil AMR-BC
# Robot móvil AMR-BC - Trabajo Fin de Grado
# Controlador: OpenRB-150
# Puerto utilizado: /dev/ttyACM0
# Contenedor Docker: tfg_robot_movimiento

echo "======================================"
echo "  INICIO TELEOPERACIÓN ROBOT TFG"
echo "======================================"

echo "[1/3] Comprobando OpenRB-150..."

if [ ! -e /dev/ttyACM0 ]; then
    echo "ERROR: No se ha detectado /dev/ttyACM0"
    echo "Revise la conexión USB de la OpenRB-150."
    exit 1
fi

echo "OpenRB-150 detectada en /dev/ttyACM0"

echo "[2/3] Iniciando contenedor Docker tfg_robot_movimiento..."

docker start tfg_robot_movimiento > /dev/null

echo "[3/3] Ejecutando teleoperación..."

docker exec -it tfg_robot_movimiento bash -c "python3 teleop.py"
