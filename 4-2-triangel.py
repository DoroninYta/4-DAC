import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
bits = len(dac)
levels = 2**bits
maxU = 3.3

def dec2bin (value):
    return [int(bin) for bin in bin(value)[2:].zfill(bits)]

def dec2dac(value):
    signal = dec2bin(value)
    GPIO.output(dac, signal)



GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)

ti = 2
u = ti/510
try:
    while True:
        for i in range(255):
           dec2dac(i) 
           time.sleep(u)
        i = 255
        while i >= 0:
            dec2dac(i)
            time.sleep(u)
            i = i - 1
finally:
    GPIO.output(dac, 0)