#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import RPi.GPIO as GPIO
import threading

GPIO.setmode(GPIO.BCM)

# -----RGB-----
RGB_LED_PIN = [20, 16, 21]  # R, G, B
RGB_PWM = []
PWM_FREQ = 200

for i in range(3):
  GPIO.setup(RGB_LED_PIN[i], GPIO.OUT)
  GPIO.output(RGB_LED_PIN[i], False)

  RGB_PWM.append(GPIO.PWM(RGB_LED_PIN[i], PWM_FREQ))
  RGB_PWM[i].start(0)


def setColor(rgb=[0, 0, 0]):
  for i in range(3):
    RGB_PWM[i].ChangeDutyCycle(100 - int((rgb[i]/255) * 100))

# -----/RGB-----


# ----HC-SR04---
GPIO_TRIGGER = 15
GPIO_ECHO = 14


def measure():
  # This function measures a distance
  GPIO.output(GPIO_TRIGGER, True)
  time.sleep(0.00001)
  GPIO.output(GPIO_TRIGGER, False)
  start = time.time()

  while GPIO.input(GPIO_ECHO) == 0:
    start = time.time()
  while GPIO.input(GPIO_ECHO) == 1:
    stop = time.time()

  elapsed = stop-start
  distance = (elapsed * 34300)/2

  return distance


def measure_average():
  # This function takes 3 measurements and
  # returns the average.
  distance1 = measure()
  time.sleep(0.1)
  distance2 = measure()
  time.sleep(0.1)
  distance3 = measure()
  distance = distance1 + distance2 + distance3
  distance = distance / 3
  return distance
# ----/HC-SR04---


# ------CAM-----
GPIO_CAM_power = 18
GPIO_CAM_ctrl = 23
# ------/CAM-----


GPIO.setup(GPIO_TRIGGER, GPIO.OUT)  # Trigger
GPIO.setup(GPIO_ECHO, GPIO.IN)  # Echo

GPIO.setup(GPIO_CAM_power, GPIO.OUT)  # CAM
GPIO.setup(GPIO_CAM_ctrl, GPIO.OUT)  # CAM

GPIO.setup(7, GPIO.IN)  # RE
GPIO.setup(8, GPIO.OUT)  # RE

GPIO.output(GPIO_TRIGGER, False)
GPIO.output(GPIO_CAM_power, True)
GPIO.output(GPIO_CAM_ctrl, True)

GPIO.output(16, True)
setColor([0, 255, 0])  # LED(GREEN)
power = True


def MAIN_WORK():
  try:
    while True:
      print('main thread')
      global power
      distance = measure_average()
      if power and distance < 10:
        print("Distance : %.1f" % distance)
        from .connectMySQL import connect_INSTER
        connect_INSTER()   # 連線至SQL並儲存紀錄

        setColor([255, 0, 0])  # LED(RED)

        power = False
        GPIO.output(GPIO_CAM_power, False)  # turn on CAM
        time.sleep(0.1)
        GPIO.output(GPIO_CAM_power, True)

        time.sleep(6)  # turn on time

        GPIO.output(GPIO_CAM_ctrl, False)  # Start Video
        print("ctrl false")
        time.sleep(0.5)
        GPIO.output(GPIO_CAM_ctrl, True)
      time.sleep(1)

  except KeyboardInterrupt:
    print('ERROR')
  finally:
    print('FINAL')
    if not power:
      GPIO.output(GPIO_CAM_power, False)  # turn off CAM
      time.sleep(2)
      GPIO.output(GPIO_CAM_power, True)
    for i in range(3):  # stop RGB LED
      RGB_PWM[i].stop()
    GPIO.cleanup()


def RESTART():
  while True:
    global power
    print('re thread')
    if GPIO.input(7) == 1:
      print('restart')
      power = True
      GPIO.output(GPIO_CAM_power, False)  # turn off CAM
      time.sleep(2)
      GPIO.output(GPIO_CAM_power, True)
      setColor([0, 255, 0])  # LED(GREEN)
      time.sleep(3)
    time.sleep(0.7)


t = threading.Thread(target=MAIN_WORK)
t1 = threading.Thread(target=RESTART)

# 執行該子執行緒
t.start()
t1.start()

t.join()
t1.join()
GPIO.cleanup()
