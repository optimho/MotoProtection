import machine
from machine import Pin

import lcd
from lcd import LCD_1inch14
import time

BL = 13


pwm = machine.PWM(Pin(BL))
pwm.freq(1000)
pwm.duty_u16(65535)  # max 65535

LCD = lcd.LCD_1inch14()
# color BRG
LCD.fill(LCD.white)

LCD.show()
LCD.text("this is a test", 60, 40, LCD.red)
LCD.text("PicoGo", 60, 60, LCD.green)
LCD.text("Pico-LCD-1.14", 60, 80, LCD.blue)

LCD.hline(10, 10, 220, LCD.blue)
LCD.hline(10, 125, 220, LCD.blue)
LCD.vline(10, 10, 115, LCD.blue)
LCD.vline(230, 10, 115, LCD.blue)

LCD.rect(12, 12, 20, 20, LCD.red)
LCD.rect(12, 103, 20, 20, LCD.red)
LCD.rect(208, 12, 20, 20, LCD.green)
LCD.rect(208, 103, 20, 20, LCD.red)

LCD.show()
time.sleep(5)
key0 = Pin(2, Pin.IN, Pin.PULL_UP)
key1 = Pin(18, Pin.IN, Pin.PULL_UP)
key2 = Pin(16, Pin.IN, Pin.PULL_UP)
key3 = Pin(20, Pin.IN, Pin.PULL_UP)
while True:
    if key0.value() == 0:
        LCD.fill_rect(12, 12, 20, 20, LCD.green)
        LCD.text("HELLO", 60, 40, LCD.red)
    else:
        LCD.fill_rect(12, 12, 20, 20, LCD.white)
        LCD.rect(12, 12, 20, 20, LCD.red)
    if (key1.value() == 0):
        LCD.fill_rect(12, 103, 20, 20, LCD.blue)
    else:
        LCD.fill_rect(12, 103, 20, 20, LCD.white)
        LCD.rect(12, 103, 20, 20, LCD.red)
    if (key2.value() == 0):
        LCD.fill_rect(208, 12, 20, 20, LCD.red)
    else:
        LCD.fill_rect(208, 12, 20, 20, LCD.white)
        LCD.rect(208, 12, 20, 20, LCD.red)
    if (key3.value() == 0):
        LCD.fill_rect(208, 103, 20, 20, LCD.red)
    else:
        LCD.fill_rect(208, 103, 20, 20, LCD.white)
        LCD.rect(208, 103, 20, 20, LCD.red)

    time.sleep(0.1)
    LCD.show()
    LCD.fill(0xFFFF)

