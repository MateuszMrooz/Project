#What-if scenarios file

import Risk
import serial

Light = 10 # Assuming the sensor is in shade and is not affected by light

serial_port = serial.Serial()
serial_port.baudrate = 9600
serial_port.port = 'com7'
serial_port.open()


choice = input('Do you want to run a drought or strom scenario?: ')
no_days = int(input('For how many days do you want to run it?: '))

if choice.lower() == 'storm':
    
    temp_change = -5 #Rate of change of values and starting values are based of realistic assumptions for Irish weather
    humidity_change = 1 #Temperature and humidity generaly go up and down respectively during a storm
    wind_change = 10
    Temp = 10 # Starting values for each variable
    Humidity = 70
    Wind = 18
    
    for day in range(1,no_days+1):
        
        if day >= 8 :
            break #Assuming storms only last about a week
        
        Temp += temp_change
        Humidity += humidity_change
        Wind += wind_change
        
        Risk_factor,Potential,Fire = Risk.Risk_factor(Temp,Humidity,Light,Wind)
        
        Risk.Risk_level(Risk_factor,Potential,serial_port,Temp)
                
        Risk.Fire(Potential,Fire,serial_port)
        
        if Risk_factor == 1:
            print('on day',day)
        
        elif Risk_factor == 2:
            print('on day',day)
        
        elif Risk_factor == 3:
            print('on day',day)
        
        else:
            print('on day',day)
        


elif choice.lower() == 'drought':
    
    temp_change = +2 #Rate of change of values
    humidity_change = -5 #Droughts are caused by a lack of rainfall, decreasing humidity, which tends to increase temperature
    wind_change = 0 #Drought doesn't change wind speed
    Temp = 10 #Starting values
    Humidity = 70
    Wind = 18
    
    for day in range(1,no_days+1):
        
        if day >= 21:
           break #Assuming droughts don't last over 20 days in Ireland
        
        if Humidity > 10:  #This stops humidity from going to an unreasonably low point (below/close to 0)
            Humidity += humidity_change
        
        Temp += temp_change
        Wind += wind_change
        
        Risk_factor,Potential,Fire = Risk.Risk_factor(Temp,Humidity,Light,Wind)
        
        Risk.Risk_level(Risk_factor,Potential,serial_port,Temp)
        
        
        if Risk_factor == 1:
            print('on day',day)
        
        elif Risk_factor == 2:
            print('on day',day)

        
        elif Risk_factor == 3:
            print('on day',day)
        
        else:
            print('on day',day)

        
else:
    print('Neither option selected')