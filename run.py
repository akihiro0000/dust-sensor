import RPi.GPIO as GPIO
import time

def pulseIn(PIN, start=1, end=0):
    if start==0: end = 1
    t_start = 0
    t_end = 0
    while GPIO.input(PIN) == end:
        t_start = time.time()
        
    while GPIO.input(PIN) == start:
        t_end = time.time()
    return t_end - t_start

def pcs2ugm3 (pcs):
  pi = 3.14159
  density = 1.65 * pow (10, 12)
  r25 = 0.44 * pow (10, -6)
  vol25 = (4/3) * pi * pow (r25, 3)
  mass25 = density * vol25 # μg
  K = 3531.5 # per m^3 
  return pcs * K * mass25

def get_pm25(PIN):
    t0 = time.time()
    t = 0
    ts = 30
    while(1):
        dt = pulseIn(PIN, 0)
        if dt<1: t = t + dt
        
        if ((time.time() - t0) > ts):
            ratio = (100*t)/ts
            concent = 1.1 * pow(ratio,3) - 3.8 * pow(ratio,2) + 520 * ratio + 0.62
            print(t, "[sec]")
            print(ratio, " [%]")
            print(concent, " [pcs/0.01cf]")
            print(pcs2ugm3(concent), " [ug/m^3]")
            print("-------------------")
            break

PIN = 14
# ピン番号をGPIOで指定
GPIO.setmode(GPIO.BCM)
# TRIG_PINを出力, ECHO_PINを入力
GPIO.setup(PIN,GPIO.IN)
GPIO.setwarnings(False)

for i in range(10):
    get_pm25(PIN)

# ピン設定解除
GPIO.cleanup()
