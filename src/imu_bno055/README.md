# IMU BNO055

Esta carpeta contiene el script utilizado para validar la comunicación entre la **Raspberry Pi 5** y la **IMU BNO055** mediante el bus **I2C**.

La IMU permite obtener datos de orientación, aceleración, velocidad angular, campo magnético y temperatura, siendo utilizada como sensor inercial dentro de la arquitectura del robot móvil AMR-BC.

## Archivo principal

- `prueba_bno055_i2c.py`: script de prueba para comprobar la comunicación I2C con la IMU BNO055 y visualizar sus medidas en tiempo real.

## Conexión utilizada

| Señal IMU BNO055 | Raspberry Pi 5 |
|---|---|
| VIN | 3.3 V |
| GND | GND |
| SDA | GPIO2 / Pin 3 |
| SCL | GPIO3 / Pin 5 |

La Raspberry Pi 5 actúa como maestro del bus I2C, mientras que la IMU BNO055 funciona como dispositivo esclavo.

## Datos mostrados por el script

El script permite visualizar en terminal las siguientes magnitudes:

| Magnitud | Descripción |
|---|---|
| Temperatura | Temperatura interna del sensor |
| Orientación Euler | Heading, Roll y Pitch |
| Aceleración | Aceleración lineal en m/s² |
| Giroscopio | Velocidad angular en rad/s |
| Magnetómetro | Campo magnético en µT |

## Ejecución

Para ejecutar la prueba:

```bash
python3 prueba_bno055_i2c.py
