#Test file

import Risk
import serial

serial_port = serial.Serial()
serial_port.baudrate = 9600
serial_port.port = 'com7'
serial_port.open()

#1st value is temperature
#2nd value is humidity
#3rd value is windspeed 
#4th value is light intensity

#All possible values which provide unique outputs
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
#Fire treshold
[36,1,31,101],
[36,1,31,1],
[36,1,1,101],
[36,1,1,1],
[36,31,31,101],
[36,31,31,1],
[36,31,1,101],
[36,31,1,1],
#Below fire treshold, above temperature risk treshold
[33,1,31,101],
[33,1,31,1],
[33,1,1,101],
[33,1,1,1],
[33,31,31,101],
[33,31,31,1],
[33,31,1,101],
[33,31,1,1]]

for a in range(0,32):#Iterates through all of the possible combination of values
    print(a + 1)# +1 is due to the list starting at 0. This number corresponds to the Iteration column in the truth table
    print(all_values[a])
    
    current_list = all_values[a]
    
    Temp = float(current_list[0])
    Humidity = float(current_list[1])
    Wind = float(current_list[2])
    Light = float(current_list[3])

    Risk_factor,Potential,Fire = Risk.Risk_factor(Temp,Humidity,Light,Wind)
            
    Risk.Risk_level(Risk_factor,Potential,serial_port,Temp)
    
    Risk.Fire(Potential,Fire,serial_port)

serial_port.close()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  