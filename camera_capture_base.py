# Maixpy Amigo Setup
from machine import I2C
axp173 = I2C(I2C.I2C3, freq=100000, scl=24, sda=27)
axp173.writeto_mem(0x34, 0x27, 0x20)
axp173.writeto_mem(0x34, 0x28, 0x0C)
#axp173.writeto_mem(0x34, 0x36, 0xCC, mem_size=8)

import sensor, image, time, lcd

lcd.init()

while True:

    try:
        print("#1")
        sensor.reset(choice=1)
        sensor.set_pixformat(sensor.YUV422)
        sensor.set_framesize(sensor.QVGA)
        sensor.set_hmirror(1)
        sensor.set_vflip(1)
        #sensor.skip_frames(time=2000)
        for i in range(100):
            img = sensor.snapshot()
            lcd.display(img)
    except Exception as e:
        print(e)

    try:
        print("#2")
        sensor.reset(choice=2)
        sensor.set_pixformat(sensor.YUV422)
        sensor.set_framesize(sensor.QVGA)
        sensor.set_hmirror(1)
        #sensor.set_vflip(1)
        #sensor.skip_frames(time=2000)
        for i in range(100):
            img = sensor.snapshot().rotation_corr(z_rotation = +90)
            lcd.display(img)
    except Exception as e:
        print(e)
