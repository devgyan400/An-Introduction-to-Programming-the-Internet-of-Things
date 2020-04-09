import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)
p = GPIO.PWM(7, 1000)
p.start(0)

while True:
    try:
        for i in range(1,100):
            p.ChangeDutyCycle(i)
            time.sleep(0.01)
        for i in range(100,0,-1):
            p.ChangeDutyCycle(i)
            time.sleep(0.01)
    except KeyboardInterrupt:
        p.stop()
        GPIO.cleanup()
