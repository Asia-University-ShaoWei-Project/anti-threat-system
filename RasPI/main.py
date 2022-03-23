from conf import ON
from .mock import env
import RPi.GPIO as GPIO
import time
from .obj import User, API
import threading
import lamp
import cam
import hc_rs04
import button

GPIO.setmode(GPIO.BCM)
btn = button.Button(input_pin=7, output_pin=8)

# TODO: ?
# GPIO.output(16, True)


alarm_lamp = lamp.AlarmLamp(led_pin=[20, 16, 21])
hc_rs = hc_rs04.HCRS04(trigger_pin=15, echo_pin=14)
camera = cam.Camera(power_pin=18, control_pin=23)
user = User(
    ID=env('USER_ID'),
    password=env('USER_PASSWORD'),
)
api = API(
    domain=env('DOMAIN'),
    user=user,
)
# not sure
lock = False

# TODO 未實現在應用中


def RESTART():
  while True:
    if btn.Is_Click():
      alarm_lamp.Boot()
      camera.Restart()
      alarm_lamp.Safe()
      time.sleep(3)


t_restart = threading.Thread(target=RESTART)
t_restart.start()
t_restart.join()
try:
  while True:
    if lock:
      time.sleep(100000)
      # TODO lock time out 後續處理
    if hc_rs.Is_OpenDoor():
      lock = ON
      api.Record()
      alarm_lamp.Warning()
      camera.Boot()
      camera.Video()
    time.sleep(1)
except KeyboardInterrupt:
  print('type error')
finally:
  if not power:
    # camera.Shutdown()
    GPIO.output(GPIO_CAM_power, False)  # turn off CAM
    time.sleep(2)
    GPIO.output(GPIO_CAM_power, True)
  for i in range(3):  # stop RGB LED
    RGB_PWM[i].stop()
  GPIO.cleanup()

GPIO.cleanup()
