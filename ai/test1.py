from serial import Serial
import time
import keyboard


arduino = Serial("COM3", 9600)

time.sleep(2)
while True:
    request = input("Write 0 - 9: ").encode("ASCII")
    
    arduino.write(request)

    if keyboard.is_pressed('q'):
        arduino.close()
        break
