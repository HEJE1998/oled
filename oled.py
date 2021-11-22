#Jeldrik Hemme
#ETS 2021
#19.11.21

#Hardware: ESP 32 + BMP 180

#Version: 0.3

from time import sleep                          #Von time den Befehl sleep importieren 
from machine import Pin, SoftSPI, SoftI2C       #Von machine die Klasse Pin, SoftSPI, SoftI2C importieren 
import st7789py as st7789                       #importiere st7789py als st7789 
from bmp180 import BMP180                       #Von bmp180 die Klasse BMP180 importieren 

#Chosse fonts

from romfonts import vga2_16x16 as font         #Von romfonts die Klasse (Schriftart) vga2_16x16 als font iportieren 

#Schnittelen des I2C-Bus festegelegt  
ic2 = SoftI2C(scl=Pin(22), sda=Pin(21))         #Schnittstellen für den I2C-Bus sind scl=Pin22 und sda=Pin21
bmp = BMP180(i2c)                               #Variable bmp wird über den I2C-Bus des Klasse BMP180 bestimmt 

#Konfiguration des SPI-Protokolls 
spi = SoftSPI(
        baudrate=20000000,                      #defeniert die Geschwindigkeit der Kommunikation        
        polarity=1,                             #kann 0 oder 1 sein und geibt den Pegel an auf, welchem sich die Leerlauftaktleistung sich befindet 
        phase=0,                                #kann 0 oder 1 sein, bei 1 überprüft sie Daten an der ersten oder zweiten Taktflanke 
        sck=Pin(18),                            #hier wird festegelegt das der 18.Pin vom Controller der Pin für sck ist 
        mosi=Pin(19),                           #hier wird festegelegt das der 19.Pin vom Controller der Pin für mosi ist 
        miso=Pin(13))                           #hier wird festegelegt das der 13.Pin vom Controller der Pin für miso ist 

tft = st7789.ST7789(
       spi,                                     #Angabe des Kommunikations-Protokoll 
       135,                                     #Angabe der Breite des Displays 
       240,                                     #Angabe der Länge des Displays 
       reset=Pin(23, Pin.OUT),                  #hier wird festgelegt das der 23.Pin vom Controller der Pin für reset ist 
       cs=Pin(5, Pin.OUT),                      #hier wird festegelegt das der 5.Pin vom Controller der Pin für cs ist 
       dc=Pin(16, Pin.OUT),                     #hier wird festegelegt das der 16.Pin vom Controller der Pin für dc ist 
       backlight=Pin(4, Pin.OUT),               #hier wird festegelegt das der 4.pin vom Controller der Pin für backlight ist  
       rotation=1)                              #Darstellungseinstellung (1=Protrait) 

tft.fill(st7789.BLACK)                  #tft.fill, sagt aus welche Farbe der gemsate Hintergrund haben soll 
line = 0
col = 0
while True:
    ausgabe = str(bmp.temperature)                                      #Variable ausgabe wird mit dem Wert des Temperatur-Sensors gefüllt/überschrieben 
    tft.text(font, ausgabe, 20, 20, st7789.YELLOW, st7789.BLACK)        #tft.text sagt aus welche Schriftart, welche Position, welche Farbe die Schrift und welche Farbe der Hintergrund haben soll 