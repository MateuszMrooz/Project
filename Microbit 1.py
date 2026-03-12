#Python code to interface with the game
#code taken from
#https://stackoverflow.com/questions/58043143/how-to-set-up-serial-communication-with-microbit-using-pyserial
#https://stackoverflow.com/questions/35936644/python-read-from-the-serial-port-data-line-by-line-into-a-list-when-available
import serial
import serial.tools.list_ports as list_ports
import re
PID_MICROBIT = 516
VID_MICROBIT = 3368
TIMEOUT = 0.001
import sqlite3

#Program to create database

with sqlite3.connect('Microbit.db') as db:
    cursor = db.cursor()
    
cursor.execute('''CREATE TABLE IF NOT EXISTS Microbit_temp (Temperature NOT NULL)''')

fin = open('Microbit_temp.csv','w')

def find_comport(pid, vid, baud):
    ''' return a serial port '''
    ser_port = serial.Serial(timeout=TIMEOUT)
    ser_port.baudrate = baud
    ports = list(list_ports.comports())
    print('scanning ports')
    for p in ports:
        print('port: {}'.format(p))
        try:
            print('pid: {} vid: {}'.format(p.pid, p.vid))
        except AttributeError:
            continue
        if (p.pid == pid) and (p.vid == vid):
            print('found target device pid: {} vid: {} port: {}'.format(
                p.pid, p.vid, p.device))
            ser_port.port = str(p.device)
            return ser_port
    return None

def one(Temperature):
        cursor.execute('''INSERT INTO Microbit_temp(Temperature)VALUES(?)''',(Temperature,))
        db.commit()
        cursor.execute(''' SELECT * FROM Microbit_temp''')
        print(cursor.fetchall())


def main():
    print('looking for microbit')
    ser_micro = find_comport(PID_MICROBIT, VID_MICROBIT, 115200)
    if not ser_micro:
        print('microbit not found')
        return
    print('opening and monitoring microbit port')
    ser_micro.open()
    gameData = ''
    while True:
        #check if there is any data waiting in the serial buffer
            size = ser_micro.inWaiting()
            if size:
                data = ser_micro.read(size).decode('utf-8')
                gameData += data.strip(' ')
                t = gameData.split('\r\n')
                print(t[0])
                for i in t[0]:
                    print(repr(float(i)))
                    if float(float(i)) >= 30:
                        if float(float(i)) >= 40:
                            print('Temperature above 30 degrees')
                        else:
                            print('Temperature above 30 degrees')
                    else:
                        print('Temperature below 30 degrees')
                    one(gameData)
                

    ser_micro.close()
main()
