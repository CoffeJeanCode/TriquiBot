#include <Servo.h>

Servo motor1;
Servo motor2;
Servo motor3;

int buttonPin = 3;
int ledPin = 11;
char movement;

void moveContinuousServo(Servo miServo, int velocidad, unsigned long duracionMovimiento) {
  unsigned long tiempoInicio = millis(); // Inicializar el tiempo de inicio

  while (millis() - tiempoInicio < duracionMovimiento) { // Mover el servo hacia adelante a la velocidad deseada durante la duración especificada
    miServo.write(90 + velocidad);
  }
  miServo.write(90); // Detener el servo después de la duración especificada
}

void makeX(Servo motor) {
  moveContinuousServo(motor, -15, 600);
  delay(600);
  moveContinuousServo(motor, 15, 900);
  delay(400);
}

void setup() {
  motor1.attach(A3);
  motor2.attach(A4);
  motor3.attach(A5);
  
  Serial.begin(9600); 
 }

void resetMotors() {
  motor1.write(10);
  motor2.write(90);
}

void loop() {
  resetMotors();

  int buttonState = digitalRead(buttonPin);

  if(buttonState > 0) {
    Serial.write("capture");
  }  
  
  if(Serial.available() > 0){
    movement = Serial.read(); 
    
    switch(movement){
      case 'x':
        makeX(motor3);
        break;
      case '1':
        motor1.write(20);
        motor2.write(140);
        delay(400);
        makeX(motor3);
        break;
      case '2':
        motor1.write(15);
        motor2.write(160);
        delay(400);
        makeX(motor3);
        break;
      case '3':
        motor1.write(15);
        motor2.write(180);
        delay(400);
        makeX(motor3);
        break;
      case '4':
        motor1.write(40);
        motor2.write(125);
        delay(400);
        makeX(motor3);
        break; 
      case '5':
        motor1.write(35);
        motor2.write(145);        
        delay(400);
        makeX(motor3);
        break; 
      case '6':
        motor1.write(40);
        motor2.write(160);
        delay(400);
        makeX(motor3);
        break;
      case '7':
        motor1.write(70);
        motor2.write(85);
        delay(400);
        makeX(motor3);
        break; 
      case '8':
        motor1.write(60);
        motor2.write(120);
        delay(400);
        makeX(motor3);
        break;
      case '9':
        motor1.write(65);
        motor2.write(135);
        delay(400);
        makeX(motor3);
        break; 
    }
 }
}
