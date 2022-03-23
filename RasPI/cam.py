import RPi.GPIO as GPIO
from conf import ON, OFF
import time


class Camera:
  boot_time = 6
  shutdown_time = 2

  def __init__(self, power_pin, control_pin):
    self.status = OFF
    self.POWER = power_pin
    self.CONTROL = control_pin
    GPIO.setup(self.POWER, GPIO.OUT)
    GPIO.setup(self.CONTROL, GPIO.OUT)

    GPIO.output(self.POWER, ON)
    GPIO.output(self.CONTROL, ON)

  def Video(self):
    GPIO.output(self.CONTROL, OFF)
    time.sleep(0.5)
    GPIO.output(self.CONTROL, ON)

  def Boot(self):
    GPIO.output(self.POWER, OFF)
    time.sleep(0.1)
    GPIO.output(self.POWER, ON)
    time.sleep(self.boot_time)
    self.status = ON

  def Shutdown(self):
    GPIO.output(self.POWER, OFF)
    time.sleep(self.shutdown_time)
    self.status = OFF

  def Restart(self):
    self.Shutdown()
    self.Boot()
