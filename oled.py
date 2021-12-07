#Jeldrik Hemme
#ETS 2021
#19.11.21

#Hardware: ESP 32 + BMP 180 + BH1750

#Sofware: libary für BH1750: https://github.com/PinkInk/upylib/blob/master/bh1750/bh1750/__init__.py

#Version: 0.8

from time import sleep                          # alle 10 Sekunden Temperatur messen 
from machine import Pin, SoftSPI, SoftI2C       # Pin (BMP180 & TFT), SoftSPI (TFT), SoftI2C(BMP180) 
import st7789py as st7789                       # TFT Display
from bmp180 import BMP180                       # BMP180 Temepratursensor 
from bh1750 import BH1750                       # BH1750 Lichtsensor 

from romfonts import vga2_16x16 as font         # Schriftart laden 
 
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))         # Objekt I2C(BMP180) instanzieren 
bmp = BMP180(i2c)                               # Objekt bmp instanzieren
bh = BH1750(i2c)                                # Objekt bh instanziert 


spi = SoftSPI(                                  # Objekt spi(TFT) instanzieren 
        baudrate=20000000,                      # Kommuniktionsgeschwindigkeit        
        polarity=1,                               
        phase=0,                                 
        sck=Pin(18),                             
        mosi=Pin(19),                            
        miso=Pin(13))                           

tft = st7789.ST7789(                            # Objekt (TFT) istanzieren  
       spi,                                     # Schnittstelle  
       135,                                     # Pixel x-Achse  
       240,                                     # Pixel y-Achse  
       reset=Pin(23, Pin.OUT),                  #
       cs=Pin(5, Pin.OUT),                      # 
       dc=Pin(16, Pin.OUT),                     #
       backlight=Pin(4, Pin.OUT),               #  
       rotation=1)                              # Rotation 1=90 Grad 

ledgrün = Pin(2, Pin.OUT)                       #
ledgelb = Pin(27, Pin.OUT)                      #
ledrot = Pin(26, Pin.OUT)                       #

#-------------Initialisierungs Ende--------------

tft.fill(st7789.BLACK)                                                  # Hintergrundfarbe Schwarz
line = 0                                                                # Zeile
col = 0                                                                 # Spalte
while True:
        ausgabe = str(round(bmp.temperature, 2))                            # ausgabe zuweisen
        ausgabe1= str(round(bmp.pressure / 100, 2))                         # ausgabe1 zuweisen
        ausgabe2= str(round(bh.luminance(BH1750.CONT_HIRES_2)))             # ausgabe2 zuweisen 
        ausgabe = ausgabe + '\xf8C'                                         # Einheit hinzugefügt
        ausgabe1 = ausgabe1 + str('hPascal')                                # Einheit hinzugefügt
        ausgabe2 = ausgabe2 + str('lux')                                    # Einheit hinzugefügt 
        tft.text(font, ausgabe, 0, 20, st7789.WHITE, st7789.BLACK)
        tft.text(font, 'Temperatur: ', 0, 0, st7789.WHITE, st7789.BLACK)            
        tft.text(font, ausgabe1, 0, 60, st7789.WHITE, st7789.BLACK)
        tft.text(font, 'Druck: ', 0, 40, st7789.WHITE, st7789.BLACK)
        tft.text(font, ausgabe2, 0, 100, st7789.WHITE, st7789.BLACK)
        tft.text(font, 'Helligkeit: ', 0, 80, st7789.WHITE, st7789.BLACK)

        temperatur = bmp.temperature                                        # temperatur zuweisen     
        if temperatur <= 23:                                                # LED nach Temperaturanzeige 
                ledgrün.value(1)                                            
                ledgelb.value(0)
                ledrot.value(0) 
        elif temperatur > 23 and temperatur <= 24:                          
                ledgrün.value(0)
                ledgelb.value(1)
                ledrot.value(0)
        elif temperatur > 24:
                ledgrün.value(0)
                ledgelb.value(0)
                ledrot.value(1)
        sleep(1)                                                             # Warten 5s




            
        



