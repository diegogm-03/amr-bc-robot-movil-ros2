#include <Dynamixel2Arduino.h>

/*
  Control teleoperado de motores DYNAMIXEL XL430 mediante OpenRB-150.

  Robot móvil AMR-BC - Trabajo Fin de Grado
  Autor: Diego Luis García Montoya

  La Raspberry Pi 5 envía comandos por USB serie a la OpenRB-150.
  La OpenRB-150 interpreta esos comandos y controla los motores DYNAMIXEL
  conectados al bus TTL.

  Comandos:
    w -> avance
    s -> retroceso
    a -> giro izquierda
    d -> giro derecha
    x -> parada
*/

#define DXL_SERIAL   Serial1
#define DEBUG_SERIAL Serial

const int DXL_DIR_PIN = -1;

const uint8_t MOTOR_IZQ = 1;
const uint8_t MOTOR_DER = 2;

const float DXL_PROTOCOL_VERSION = 2.0;

Dynamixel2Arduino dxl(DXL_SERIAL, DXL_DIR_PIN);

using namespace ControlTableItem;

void setup() {

  DEBUG_SERIAL.begin(115200);

  dxl.begin(57600);
  dxl.setPortProtocolVersion(DXL_PROTOCOL_VERSION);

  dxl.torqueOff(MOTOR_IZQ);
  dxl.torqueOff(MOTOR_DER);

  dxl.setOperatingMode(MOTOR_IZQ, OP_VELOCITY);
  dxl.setOperatingMode(MOTOR_DER, OP_VELOCITY);

  dxl.torqueOn(MOTOR_IZQ);
  dxl.torqueOn(MOTOR_DER);

  DEBUG_SERIAL.println("CONTROL TELEOPERADO");
  DEBUG_SERIAL.println("W adelante");
  DEBUG_SERIAL.println("S atras");
  DEBUG_SERIAL.println("A izquierda");
  DEBUG_SERIAL.println("D derecha");
  DEBUG_SERIAL.println("X parar");
}

void loop() {

  if (DEBUG_SERIAL.available()) {

    char tecla = DEBUG_SERIAL.read();

    switch (tecla) {

      case 'w':
        dxl.setGoalVelocity(MOTOR_IZQ, 50);
        dxl.setGoalVelocity(MOTOR_DER, -50);
        break;

      case 's':
        dxl.setGoalVelocity(MOTOR_IZQ, -50);
        dxl.setGoalVelocity(MOTOR_DER, 50);
        break;

      case 'a':
        dxl.setGoalVelocity(MOTOR_IZQ, -50);
        dxl.setGoalVelocity(MOTOR_DER, -50);
        break;

      case 'd':
        dxl.setGoalVelocity(MOTOR_IZQ, 50);
        dxl.setGoalVelocity(MOTOR_DER, 50);
        break;

      case 'x':
        dxl.setGoalVelocity(MOTOR_IZQ, 0);
        dxl.setGoalVelocity(MOTOR_DER, 0);
        break;
    }
  }
}
