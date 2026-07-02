# Teleoperación

Esta carpeta contiene los scripts utilizados para la teleoperación del robot móvil **AMR-BC** desde la Raspberry Pi 5.

La teleoperación permite controlar manualmente el movimiento del robot mediante teclado, enviando comandos por comunicación serie hacia la placa **OpenRB-150**, encargada de controlar los motores **DYNAMIXEL XL430**.

## Archivos principales

- `iniciar_teleop.sh`: script de inicio que comprueba la conexión de la OpenRB-150, arranca el contenedor Docker y ejecuta el programa de teleoperación.
- `teleop.py`: script principal de control por teclado. Envía comandos serie a la OpenRB-150 mediante el puerto `/dev/ttyACM0`.

## Funcionamiento general

El sistema de teleoperación se basa en el envío de caracteres desde la Raspberry Pi 5 hacia la OpenRB-150.

| Tecla | Comando enviado | Acción |
|---|---|---|
| `W` | `w` | Avance |
| `S` | `s` | Retroceso |
| `A` | `a` | Giro a la izquierda |
| `D` | `d` | Giro a la derecha |
| `X` | `x` | Parada |

## Parámetros utilizados

| Parámetro | Valor |
|---|---|
| Puerto serie | `/dev/ttyACM0` |
| Baudrate | `115200` |
| Contenedor Docker | `tfg_robot_movimiento` |
| Script ejecutado | `teleop.py` |

## Ejecución

Para iniciar la teleoperación desde la Raspberry Pi 5:

```bash
./iniciar_teleop.sh
```

En caso de que el archivo no tenga permisos de ejecución, se puede aplicar:

```bash
chmod +x iniciar_teleop.sh
```

y después ejecutarlo de nuevo:

```bash
./iniciar_teleop.sh
```

## Validación

La validación consistió en comprobar el movimiento del robot en tiempo real mediante comandos de teclado, verificando la respuesta de los motores DYNAMIXEL y la comunicación correcta entre la Raspberry Pi 5 y la OpenRB-150.

```bash
./iniciar_teleop.sh
