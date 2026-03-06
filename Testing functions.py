#Test file

import Risk
import serial

ser_port = serial.Serial()
ser_port.baudrate = 9600
ser_port.port = 'com7'
ser_port.open()

#1st value is temperature
#2nd value is humidity
#3rd value is windspeed 
#4th value is light intensity

all_values = [
[31,1,31,101],
[31,1,31,1],
[31,1,1,101],
[31,1,1,1],
[31,31,31,101],
[31,31,31,1],
[31,31,1,101],
[31,31,1,1],
[1,1,31,101],
[1,1,31,1],
[1,1,1,101],
[1,1,1,1],
[1,31,31,101],
[1,31,31,1],
[1,31,1,101],
[1,31,1,1],
[41,1,31,101],
[41,1,31,1],
[41,1,1,101],
[41,1,1,1],
[41,31,31,101],
[41,31,31,1],
[41,31,1,101],
[41,31,1,1],
[35,1,31,101],
[35,1,31,1],
[35,1,1,101],
[35,1,1,1],
[35,31,31,101],
[35,31,31,1],
[35,31,1,101],
[35,31,1,1]]

for a in range(0,32):
    print(a + 1)# +1 is due to the list starting at 0
    print(all_values[a])
    
    current_list = all_values[a]
    
    Temp = float(current_list[0])
    Humidity = float(current_list[1])
    Wind = float(current_list[2])
    Light = float(current_list[3])

    Risk_factor,Potential,Fire = Risk.Risk_factor(Temp,Humidity,Light,Wind)
            
    Risk.Risk_level(Risk_factor,Potential,ser_port,Temp)

ser_port.close()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  