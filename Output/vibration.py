import time
import VL53L0X
import RPi.GPIO as GPIO
import numpy as np

# GPIO
vibrate_1 = 2
vibrate_2 = 3
vibrate_3 = 4
vibrate_4 = 17
vibrate_5 = 27
vibrate_6 = 22

GPIO.setwarnings(False)

# Setup GPIO for shutdown pins on each vibrator
GPIO.setmode(GPIO.BCM)
GPIO.setup(vibrate_1, GPIO.OUT)
GPIO.setup(vibrate_2, GPIO.OUT)
GPIO.setup(vibrate_3, GPIO.OUT)
GPIO.setup(vibrate_4, GPIO.OUT)
GPIO.setup(vibrate_5, GPIO.OUT)
GPIO.setup(vibrate_6, GPIO.OUT)


# Set all shutdown pins low to turn off each vibrator
GPIO.output(vibrate_1, GPIO.LOW)
GPIO.output(vibrate_2, GPIO.LOW)
GPIO.output(vibrate_3, GPIO.LOW)
GPIO.output(vibrate_1, GPIO.LOW)
GPIO.output(vibrate_2, GPIO.LOW)
GPIO.output(vibrate_3, GPIO.LOW)

for x in range(0, 5):
  GPIO.output(vibrate_1, GPIO.HIGH)
  time.sleep(2)
  GPIO.output(vibrate_1, GPIO.LOW)

  GPIO.output(vibrate_2, GPIO.HIGH)
  time.sleep(2)
  GPIO.output(vibrate_2, GPIO.LOW)

  GPIO.output(vibrate_3, GPIO.HIGH)
  time.sleep(2)
  GPIO.output(vibrate_3, GPIO.LOW)

  GPIO.output(vibrate_4, GPIO.HIGH)
  time.sleep(2)
  GPIO.output(vibrate_4, GPIO.LOW)

  GPIO.output(vibrate_5, GPIO.HIGH)
  time.sleep(2)
  GPIO.output(vibrate_5, GPIO.LOW)

  GPIO.output(vibrate_6, GPIO.HIGH)
  time.sleep(2)
  GPIO.output(vibrate_6, GPIO.LOW)
