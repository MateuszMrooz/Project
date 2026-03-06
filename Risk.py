#Fire risk function file

import serial

#Function to check if sensor values are above the threshold for them to be a risk

def Risk_factor(db_Temp,db_Humidity,db_Light,db_Wind): 
    
    Risk_factor = 0
    Potential = False
    Fire = False
    
    if db_Temp >= 30:
        Risk_factor += 1
        if db_Temp >= 35:
            Fire = True 
                    
    if db_Humidity <= 30:
        Risk_factor += 1
                    
    if db_Light >= 100:
        Potential = True #Places temperature as a potential risk factor due to being in direct sunlight
                
    if db_Wind >= 30:
        Risk_factor += 1
        
    return (Risk_factor,Potential,Fire)

#Function to define the risk of a wildfire starting

def Risk_level(Risk_factor,Potential,ser_port,db_Temp):
    
    if Potential == True and Risk_factor > 0 and db_Temp >= 30:
        print('Potential ',end='')
        
        if Risk_factor == 1:
            print('low or no risk')
            #blink 1st LED
            ser_port.write("1".encode())

            
        elif Risk_factor == 2:
            print('moderate or low risk')
            #blink 2nd LED + 1st on
            ser_port.write("3".encode())

            
        elif Risk_factor == 3:
            print('high or moderate risk')
            #blink 3rd LED + 1st and 2nd on
            ser_port.write("5".encode())


            
    elif Risk_factor == 0:
        print('No risk')
        
    elif Risk_factor == 1:
        print('Low risk')
        #1st LED on
        ser_port.write("2".encode())#1 corresponds to the ASCII value in vscode

        
    elif Risk_factor == 2:
        print('Moderate risk')
        #Up to 2nd LED on
        ser_port.write("4".encode())

        
    elif Risk_factor == 3:
        print('High risk')
        #Up to 3rd LED on
        ser_port.write("6".encode())


#Function to check for possible fires
        
def Fire(Potential,Fire,ser_port):
    
    if Fire == True :
        if Potential == True:
            print('Potential fire')
            #blink fire led
            ser_port.write("7".encode())
            
        else:
            print('FIRE!!!!!!!')
            #fire led
            ser_port.write("8".encode())
            

        
        
        
        