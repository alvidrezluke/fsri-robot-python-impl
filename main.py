from robot import Robot
import time

exRbot = Robot()
def stop(change):
    exRbot.stop()
    
def step_forward(change):
    exRbot.forward(0.4)
    time.sleep(0.5)
    exRbot.stop()

def step_backward(change):
    exRbot.backward(0.4)
    time.sleep(0.5)
    exRbot.stop()

def step_left(change):
    exRbot.left(0.3)
    time.sleep(0.5)
    exRbot.stop()

def step_right(change):
    exRbot.right(0.3)
    time.sleep(0.5)
    exRbot.stop()

