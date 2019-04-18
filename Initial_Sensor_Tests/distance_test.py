import time
import VL53L0X
import RPi.GPIO as GPIO

# GPIO for left sensor shutdown pin
left = 20
# GPIO for right shutdown pin
right = 16
#GPIO for forward shutdown pin
forward = 21

GPIO.setwarnings(False)

# Setup GPIO for shutdown pins on each VL53L0X
GPIO.setmode(GPIO.BCM)
GPIO.setup(left, GPIO.OUT)
GPIO.setup(right, GPIO.OUT)
GPIO.setup(forward, GPIO.OUT)


# Set all shutdown pins low to turn off each VL53L0X
GPIO.output(left, GPIO.LOW)
GPIO.output(right, GPIO.LOW)
GPIO.output(forward, GPIO.LOW)

# Keep all low for 500 ms or so to make sure they reset
time.sleep(0.50)

# Create one object per VL53L0X passing the address to give to
# each.
tof_left = VL53L0X.VL53L0X(address=0x2B)
tof_right = VL53L0X.VL53L0X(address=0x2D)
tof_forward = VL53L0X.VL53L0X(address=0x29)

# Set shutdown pin high for the first VL53L0X then 
# call to start ranging 
GPIO.output(left, GPIO.HIGH)
time.sleep(0.50)
tof_left.start_ranging(VL53L0X.VL53L0X_BETTER_ACCURACY_MODE)

# Set shutdown pin high for the second VL53L0X then 
# call to start ranging 
GPIO.output(right, GPIO.HIGH)
time.sleep(0.50)
tof_right.start_ranging(VL53L0X.VL53L0X_BETTER_ACCURACY_MODE)

# Set shutdown pin high for the first VL53L0X then 
# call to start ranging 
GPIO.output(forward, GPIO.HIGH)
time.sleep(0.50)
tof_forward.start_ranging(VL53L0X.VL53L0X_BETTER_ACCURACY_MODE)

timing = tof_left.get_timing()
if (timing < 20000):
    timing = 20000
print ("Timing %d ms" % (timing/1000))

for count in range(1,101):
    left_distance = tof_left.get_distance()
    if (left_distance > 0):
        print ("left distance in mm is %d mm" % left_distance)
    else:
        print ("%d - Error" % tof_left.my_object_number)

    right_distance = tof_right.get_distance()
    if (right_distance > 0):
        print ("right distance in mm is %d mm" % right_distance)
    else:
        print ("%d - Error" % tof_right.my_object_number)
    
    forward_distance = tof_right.get_distance()
    if (forward_distance > 0):
        print ("forward distance in mm is %d mm" % forward_distance)
    else:
        print ("%d - Error" % tof_forward.my_object_number)

    time.sleep(timing/1000000.00)

tof_left.stop_ranging()
GPIO.output(left, GPIO.LOW)

tof_right.stop_ranging()
GPIO.output(right, GPIO.LOW)

tof_forward.stop_ranging()
GPIO.output(forward, GPIO.LOW)
