#include <Servo.h>
#include <math.h>

class Motor : public Servo {
  public:
    // Constructor de la clase
    Motor() {}

    // Función para mover el motor a una posición determinada
    void move(float x, float y) {
      float angle = degrees(atan2(y,x));
      write(angle);
    }

    void add(float plus) {
      float angle = read();
      Serial.print(angle);
      write(angle + plus);
    }
};
