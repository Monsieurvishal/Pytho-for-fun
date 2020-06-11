#TMP102 I2C temperature sensor was used

import RPi.GPIO as GPIO
import smbus #I2c Protocol
import time

I2C_BUS = 0
bus = smbus.SMBus(I2C_BUS)
   

DEVICE_ADDRESS = 0x48      
TEMP_THRESHOLD = 78
TEMP_HYST = 2


GPIO.setmode(GPIO.BCM)
FAN_PIN = 23
GPIO.setup(FAN_PIN, GPIO.OUT)

while True:
    time.sleep(1)
    #Read the temp register
    temp_reg_12bit = bus.read_word_data(DEVICE_ADDRESS , 0 )
    temp_low = (temp_reg_12bit & 0xff00) >> 8
    temp_high = (temp_reg_12bit & 0x00ff)
    #byreffering Datasheet
    temp  = ((( temp_high * 256 )  temp_low) >> 4 )
    #handle negative temps
    if temp > 0x7FF:
        temp = temp-4096;
        
    temp_C = float(temp) * 0.0625
    temp_F = temp_C * 9/5 32
    
    print "Temp = %3.1f C -- %3.1f F" % (temp_C,temp_F)

    #control the fan based on the temp
    if(temp_F > TEMP_THRESHOLD):
        GPIO.output(FAN_PIN, True)
        
    if(temp_F < (TEMP_THRESHOLD - TEMP_HYST)):
        GPIO.output(FAN_PIN, False)
                
