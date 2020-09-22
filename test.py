import RPi.GPIO as IO
import time
import picamera
import os

IO.setwarnings(False)
IO.setmode(IO.BCM)

IO.setup(2,IO.IN) #GPIO 14 -> IR sensor as input
IO.setup(14, IO.OUT)
servo = IO.PWM(14, 50) # GPIO 17 for PWM with 50Hz
servo.start(0)

def numberFormat(num: int) -> str:
    if num < 10:
        return '000'+str(num)
    elif num >= 10 and num < 100:
        return '00'+str(num)
    elif num >= 100 and num < 1000:
        return '0' + str(num)
    else:
        return str(num)

def takePicture():
    with picamera.PiCamera() as camera:
        camera.resolution = (2592, 1944)
        camera.rotation = 90
        #camera.led = False
        time.sleep(2)
        num = len(next(os.walk("../pictures"))[2])
        camera.capture('../pictures/' + numberFormat(num) + '.jpg')
        print("Saved Picture as: " + numberFormat(num) + ".jpg")

def takeMultipleShots():
    with picamera.PiCamera() as camera:
        camera.resolution = (2592, 1944)
        camera.rotation = 90
        #camera.led = False
        time.sleep(2)
        for x in range(0,10):
            num = len(next(os.walk("../pictures"))[2])
            camera.capture('../pictures/'+ numberFormat(num) +'.jpg')
            print("Saved Picture as: " + numberFormat(num) +".jpg")
            time.sleep(.15)


def dropNut():
    duty = 2


    # turn back to 0 degrees
    print("Turning back to 0 degrees")
    servo.ChangeDutyCycle(12)
    time.sleep(0.5)
    servo.ChangeDutyCycle(0)

    # Wait a couple of seconds
    time.sleep(.5)
    print("Turning back to 0 degrees")
    servo.ChangeDutyCycle(2)
    time.sleep(0.5)
    servo.ChangeDutyCycle(0)

while True:
    takePicture()