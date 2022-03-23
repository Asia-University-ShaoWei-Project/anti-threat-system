import RPi.GPIO as GPIO
from conf import OFF, GREEN, RED, ORANGE
RGB_PWM = []
PWM_FREQ = 200


class AlarmLamp:
  frequency = 200

  def __init__(self, led_pin):
    self.LED = led_pin
    self.RGB_PWM = []
    for i, pin in enumerate(self.LED):
      GPIO.setup(pin, GPIO.OUT)
      GPIO.output(pin, OFF)
      #! ???
      self.RGB_PWM.append(GPIO.PWM(pin, self.frequency))
      self.RGB_PWM[i].start(0)

  def Set_color(color):
    for i, v in enumerate(color):
      RGB_PWM[i].ChangeDutyCycle(100 - int((v/255) * 100))

  def Safe(self):
    GREEN = [0, 255, 0]
    self.Set_color(GREEN)

  def Boot(self):
    # TODO orange rgb code
    ORANGE = [0, 0, 0]
    self.Set_color(ORANGE)

  def Warning(self):
    RED = [255, 0, 0]
    self.Set_color(RED)
