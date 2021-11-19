#Jeldrik Hemme
#ETS 2021
#19.11.21

#Hardware: ESP 32 + BMP 180

#Version: 0.1

from time import sleep
from machine import Pin, SoftSPI, SoftI2C
import st7789py as st7789
from bmp180 import BMP180

#Chosse fonts

from romfonts import vga2_16x16 as font 

ic2 = SoftI2C(scl=Pin(22), sda=Pin(21))
bmp = BMP180(ic2)

spi = SoftSPI(
        baudrate=20000000,
        polarity=1,
        phase=0,
        sck=Pin(18),
        mosi=Pin(19),
        miso=Pin(13))

tft = st7789.ST7789(
       spi,
       135,
       240,
       reset=Pin(23, Pin.OUT),
       cs=Pin(5, Pin.OUT),
       dc=Pin(16, Pin.OUT),
       backlight=Pin(4, Pin.OUT),
       rotation=1)

tft.fill(st7789.BLACK)
line = 0
col = 0
while True:
    ausgabe = str(bmp.temperature)
    tft.text(font, ausgabe, 20, 20, st7789.YELLOW, st7789.BLACK)