import RPi.GPIO as GPIO
import time
from conf import ON, OFF


class HCRS04:
  min_distance = 10

  def __init__(self, trigger_pin, echo_pin):
    self.TRIGGER = trigger_pin
    self.ECHO = echo_pin
    self.delay = 0.1
    GPIO.setup(self.TRIGGER, GPIO.OUT)
    GPIO.setup(self.ECHO, GPIO.IN)
    GPIO.output(self.TRIGGER, OFF)

  def measure_distance(self):  # measure()
    GPIO.output(self.TRIGGER, ON)
    time.sleep(0.0001)
    GPIO.output(self.TRIGGER, OFF)
    start = time.time()
    #! what??
    while GPIO.input(self.ECHO) == 0:
      start = time.time()
    while GPIO.input(self.ECHO) == 1:
      stop = time.time()

    elapsed = stop-start
    distance = (elapsed * 34300)/2

    return distance

  def average_distance(self):
    count = 3
    distances_sum = 0
    for _ in range(count):
      distances_sum += self.measure_distance()
      time.sleep(self.delay)
    average = distances_sum / count
    return average

  def Is_OpenDoor(self):
    average = self.average_distance()
    if average > self.min_distance:
      return False
    return True
