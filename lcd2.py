import sys
sys.path.append('/var/www/quick2wire-python-api')

import i2c_lcd
from time import * 


# Configuration parameters
# I2C Address, Port, Enable pin, RW pin, RS pin, Data 4 pin, Data 5 pin, Data 6 pin, Data 7 pin, Backlight pin (optional)
# below are correct settings for SainSmart IIC/I2C/TWI 1602 Serial LCD Module 

lcd = i2c_lcd.i2c_lcd(0x3f,1, 2, 1, 0, 4, 5, 6, 7, 3)

# If you want to disable the cursor, uncomment the following line
lcd.command(lcd.CMD_Display_Control | lcd.OPT_Enable_Display)

lcd.backLightOn()

lcd.writeString("Python I2C LCD")
lcd.setPosition(2, 3) 
lcd.writeString("For the Pi")
