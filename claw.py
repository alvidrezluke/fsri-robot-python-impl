from re import L
from shutil import move


SERVO_PIN = 10
CLAW_STATE = "unknown"

# Get claw state
# Move claw

def get_claw_state():
    return CLAW_STATE

def open_claw():
    state = get_claw_state();
    match state:
        case "unknown":
            print("Do not know state of claw")
            move_claw_to_open()
        case "open":
            print("Claw already open")
        case "closed":
            print("Opening claw")
            move_claw_to_open()
        case "opening":
            print("Already opening")
        case "closing":
            print("Already closing")
        case _:
            print("Invalid state")
import Jetson.GPIO as GPIO
import time

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(2.5) # Initialization

def move_claw_to_open():
    try:
        while True:
            p.ChangeDutyCycle(5)
            time.sleep(0.5)
            p.ChangeDutyCycle(7.5)
            time.sleep(0.5)
            p.ChangeDutyCycle(10)
            time.sleep(0.5)
            p.ChangeDutyCycle(12.5)
            time.sleep(0.5)
            p.ChangeDutyCycle(10)
            time.sleep(0.5)
            p.ChangeDutyCycle(7.5)
            time.sleep(0.5)
            p.ChangeDutyCycle(5)
            time.sleep(0.5)
            p.ChangeDutyCycle(2.5)
            time.sleep(0.5)
    except KeyboardInterrupt:
        p.stop()
        GPIO.cleanup()

if __name__ == "__main__":
    open_claw()