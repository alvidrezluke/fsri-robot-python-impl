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
            move_claw_to_open()
        case "open":
            print("Claw already open")
        case "closed":
            print("Opening claw")
            # TODO: Actually open the claw
        case "opening":
            print("Already opening")
        case "closing":
            print("Already closing")
        case _:
            print("Invalid state")

def move_claw_to_open():
    print("Open plz")