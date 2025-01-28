# Complete project details at https://RandomNerdTutorials.com

from machine import Pin, I2C
import time
import BME280
from machine import Pin, SoftI2C
from machine_i2c_lcd import I2cLcd

# ESP32 - Pin assignment
i2c = I2C(scl=Pin(22), sda=Pin(21), freq=10000)
# ESP8266 - Pin assignment
#i2c = I2C(scl=Pin(5), sda=Pin(4), freq=10000)


# Define the LCD I2C address and dimensions
I2C_ADDR = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

i2c_display = SoftI2C(sda=Pin(12), scl=Pin(13), freq=400000)

devices = i2c_display.scan()
if len(devices) == 0:
    print("Ziadne i2c zariadenie!")
else:
    print('i2c zariadenia nájdené:',len(devices))
for device in devices:
    print("Hexa adresa: ",hex(device))

lcd = I2cLcd(i2c_display, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

lcd.putstr("Tvoj merac Romansa spusta :)!!!!")
time.sleep(5)


while True:
  bme = BME280.BME280(i2c=i2c)
  temp = bme.temperature
  hum = bme.humidity
  pres = bme.pressure
  # uncomment for temperature in Fahrenheit
  #temp = (bme.read_temperature()/100) * (9/5) + 32
  #temp = str(round(temp, 2)) + 'F'
  lcd.clear()
  lcd.move_to(0, 0)
  lcd.putstr("TH:" + str(temp))
  print('Temperature: ', temp)
 
  
  lcd.move_to(10, 0)
  lcd.putstr(str(hum))
  print('Humidity: ', hum)
     
  lcd.move_to(0, 1)
  lcd.putstr("P:" + str(pres))
  print('Pressure: ', pres)

  time.sleep(5)
