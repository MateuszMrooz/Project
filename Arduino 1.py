#Main code

import serial
import sqlite3
import Risk
import Database

Database.creating_db()

ser_port = serial.Serial()
ser_port.baudrate = 9600 #The buadrate which the arduino runs at
ser_port.port = 'com7' #This number is randomly assigned by the computer
 
 
if not ser_port:
    print('Device not found') #Prints message if a device isn't found

else:
    ser_port.open()
    Sensor = ''
    while True:
            size = ser_port.inWaiting()
            if size:
                data = ser_port.read(size).decode('utf-8')
                Sensor = data.strip()
                print(Sensor)
                values = Sensor.split(' ')
                
                Temp = float(values[1])
                Humidity = float(values[3])
                Light = float(values[5])
                Wind = float(values[7])
                
                db_Temp,db_Humidity,db_Light,db_Wind = Database.dbase(Temp,Humidity,Light,Wind)

                Risk_factor,Potential,Fire = Risk.Risk_factor(db_Temp,db_Humidity,db_Light,db_Wind)
            
                Risk.Risk_level(Risk_factor,Potential,ser_port,db_Temp)
                
                Risk.Fire(Potential,Fire,ser_port)
                    
                
    ser_port.close() #Closes the serial port if the code crashes
