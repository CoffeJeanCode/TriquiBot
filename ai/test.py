from serial import Serial
import time

ser = Serial('COM3', 9600)

time.sleep(2)

while True:
    ser.write(b'read')
    response = ser.readline().decode().strip()
    if response == 'LED ON':
        print('LED is on')
    else:
        print('LED is off')
    time.sleep(0.1)