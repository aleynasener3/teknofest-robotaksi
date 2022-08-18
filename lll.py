#!/usr/bin/python

from i2clibraries import i2c_lcd_smbus

lcd = i2c_lcd_smbus.i2c_lcd(0x3f,1, 2, 1, 0, 4, 5, 6, 7, 3)

lcd.command(lcd.CMD_Display_Control | lcd.OPT_Enable_Display)
lcd.backLightOn()
lcd.writeString("Python I2C LCD")
lcd.setPosition(2, 0) 
lcd.writeString("with python 2")