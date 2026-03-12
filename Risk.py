#Fire risk calculator function file

import serial
import colorama
from colorama import Fore,Style

#Function to check if sensor values are above the threshold for them to be a risk

def Risk_factor(db_Temp,db_Humidity,db_Light,db_Wind): 
    
    Risk_factor = 0
    Potential = False
    Fire = False
    
    if db_Temp >= 30:
        Risk_factor += 1
        if db_Temp >= 40:
            Fire = True 
                    
    if db_Humidity <= 30:
        Risk_factor += 1
                    
    if db_Light >= 100:
        Potential = True #Places temperature as a potential risk factor due to being in direct sunlight
                
    if db_Wind >= 30:
        Risk_factor += 1
        
    return (Risk_factor,Potential,Fire)

#Function to define the risk of a wildfire starting

def Risk_level(Risk_factor,Potential,serial_port,db_Temp):
    
    if Potential == True and Risk_factor > 0 and db_Temp >= 30:
        print('Potential ',end='')
        
        if Risk_factor == 1:
            print('low or no risk')
            #Blink 1st LED
            serial_port.write("1".encode())#1 corresponds to the ASCII value in VSCode

            
        elif Risk_factor == 2:
            print('moderate or low risk')
            #Blink 2nd LED + 1st on
            serial_port.write("3".encode())

            
        elif Risk_factor == 3:
            print('high or moderate risk')
            #Blink 3rd LED + 1st and 2nd on
            serial_port.write("5".encode())


            
    elif Risk_factor == 0:
        print('No risk')
        #Reset all LEDs when no risk including fire LED as it requires a risk factor of at least 1
        serial_port.write("8".encode())
        
    elif Risk_factor == 1:
        print('Low risk')
        #1st LED on
        serial_port.write("2".encode())

        
    elif Risk_factor == 2:
        print('Moderate risk')
        #Up to 2nd LED on
        serial_port.write("4".encode())

        
    elif Risk_factor == 3:
        print('High risk')
        #Up to 3rd LED on
        serial_port.write("6".encode())


#Function to check for possible fires
        
def Fire(Potential,Fire,serial_port):
    
    if Fire == True :
        if Potential == True:
            print('Potential fire')
            
        else:
            print(Fore.RED + Style.BRIGHT + 'FIRE!!!!!!!',end='')#Displays warning in red and bold text to alert user of fire
            print(Style.RESET_ALL +'')#Resets text colour and style
            #Fire LED
            serial_port.write("7".encode())
            
