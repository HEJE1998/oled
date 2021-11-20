#Jeldrik Hemme
#ETS 2021
#19.11.21

#Hardware: ESP 32 + BMP 180

#Version: 0.2

from time import sleep                          #Von time den Befehl sleep importieren 
from machine import Pin, SoftSPI, SoftI2C       #Von machine die Klasse Pin, SoftSPI, SoftI2C importieren 
import st7789py as st7789                       #importiere st7789py als st7789 
from bmp180 import BMP180                       #Von bmp180 die Klasse BMP180 importieren 

#Chosse fonts

from romfonts import vga2_16x16 as font         #Von romfonts die Klasse (Schriftart) vga2_16x16 als font iportieren 

#Schnittelen des I2C-Bus festegelegt  
ic2 = SoftI2C(scl=Pin(22), sda=Pin(21))         #Schnittstellen für den I2C-Bus sind scl=Pin22 und sda=Pin21
bmp = BMP180(i2c)                               #Variable bmp wird über den I2C-Bus des Klasse BMP180 bestimmt 

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

tft.fill(st7789.BLACK)                  #tft.fill, sagt aus welche Farbe der Hintergrund haben soll 
line = 0
col = 0
while True:
    ausgabe = str(bmp.temperature)                                      #Variable ausgabe wird mit dem Wert des Temperatur-Sensors gefüllt/überschrieben 
    tft.text(font, ausgabe, 20, 20, st7789.YELLOW, st7789.BLACK)        #tft.text sagt aus welche Schriftart, welche Position, welche Farbe die Schrift und welche Farbe der Hintergrund haben soll 