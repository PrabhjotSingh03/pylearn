import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
for x in range(0,4):
	time.sleep(5)
	GPIO.output(11,0)
	time.sleep(5)
	GPIO.output(11,1)
GPIO.cleanup()