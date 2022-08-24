import atexit
import qwiic
from Adafruit_MotorHAT import Adafruit_MotorHAT
import traitlets
from traitlets.config.configurable import Configurable



# Scan for devices on I2C bus
addresses = qwiic.scan()

class Motor(Configurable):


    value = traitlets.Float()
        
    # config
    alpha = traitlets.Float(default_value=1.0).tag(config=True)
    beta = traitlets.Float(default_value=0.0).tag(config=True)
    
    # Adafruit Hardware
    if 96 in addresses:
        
        def __init__(self, driver, channel, *args, **kwargs):
            super(Motor, self).__init__(*args, **kwargs)  # initializes traitlets

            self._driver = driver
            self._motor = self._driver.getMotor(channel)
            if(channel == 1):
                self._ina = 1
                self._inb = 0
            else:
                self._ina = 2
                self._inb = 3
            atexit.register(self._release)
            
        @traitlets.observe('value')
        def _observe_value(self, change):
            self._write_value(change['new'])

        def _write_value(self, value):
            """Sets motor value between [-1, 1]"""
            mapped_value = int(255.0 * (self.alpha * value + self.beta))
            speed = min(max(abs(mapped_value), 0), 255)
            self._motor.setSpeed(speed)
            if mapped_value < 0:
                self._motor.run(Adafruit_MotorHAT.FORWARD)
                # The two lines below are required for the Waveshare JetBot Board only
                self._driver._pwm.setPWM(self._ina,0,0)
                self._driver._pwm.setPWM(self._inb,0,speed*16)
            else:
                self._motor.run(Adafruit_MotorHAT.BACKWARD)
                # The two lines below are required for the Waveshare JetBot Board only
                self._driver._pwm.setPWM(self._ina,0,speed*16)
                self._driver._pwm.setPWM(self._inb,0,0)

        def _release(self):
            """Stops motor by releasing control"""
            self._motor.run(Adafruit_MotorHAT.RELEASE)
            # The two lines below are required for the Waveshare JetBot Board only
            self._driver._pwm.setPWM(self._ina,0,0)
            self._driver._pwm.setPWM(self._inb,0,0)    

    # SparkFun Hardware
    elif 93 in addresses:

        def __init__(self, driver, channel, *args, **kwargs):
            super(Motor, self).__init__(*args, **kwargs)  # initializes traitlets

            self._driver = driver
            atexit.register(self._release)
            self.channel = channel
            
        @traitlets.observe('value')
        def _observe_value(self, change):
            self._write_value(change['new'])

        def _write_value(self, value):
            """Sets motor value between [-1, 1]"""
            speed = int(255 * (self.alpha * value + self.beta))

            # Set Motor Controls: .set_drive( motor number, direction, speed)
            # Motor Number: A = 0, B = 1
            # Direction: FWD = 0, BACK = 1
            # Speed: (-255) - 255 (neg. values reverse direction of motor)

            if self.channel == 1:
                self._motor = self._driver.set_drive(self.channel-1, 0, speed)
            elif self.channel == 2:
                self._motor = self._driver.set_drive(self.channel-1, 0, speed)
            self._driver.enable()
                
        def _release(self):
            """Stops motor by releasing control"""
            self._driver.disable()
