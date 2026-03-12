#Main code

import serial
import sqlite3
import Risk
import Database

Database.creating_db()

serial_port = serial.Serial()
serial_port.baudrate = 9600 #The buadrate which the arduino runs at
serial_port.port = 'com7' #This number is randomly assigned by the computer
 
 
if not serial_port:
    print('Device not found') #Prints message if a device isn't found

else:
    serial_port.open()
    Sensor = ''
    while True:
            port = serial_port.inWaiting()
            if port:
                data = serial_port.read(port).decode('utf-8')
                Sensor = data.strip()
                print(Sensor)
                values = Sensor.split(' ')
                
                Temp = float(values[1])
                Humidity = float(values[3])
                Light = float(values[5])
                Wind = float(values[7])
                
                #Function to write to database
                db_Temp,db_Humidity,db_Light,db_Wind = Database.dbase(Temp,Humidity,Light,Wind)

                #Functions to calculate risk and occurence of fire
                Risk_factor,Potential,Fire = Risk.Risk_factor(db_Temp,db_Humidity,db_Light,db_Wind)
            
                Risk.Risk_level(Risk_factor,Potential,serial_port,db_Temp)
                
                Risk.Fire(Potential,Fire,serial_port)
                    
                
    serial_port.close() #Closes the serial port if the code crashes
