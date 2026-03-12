#Database function file

import sqlite3

cursor = None 
db = None

#Function to create database

def creating_db():
    global cursor
    global db
    with sqlite3.connect('Arduino.db') as db:
      cursor = db.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Arduino (
    Temperature real NOT NULL,
    Humidity real NOT NULL,
    Light real NOT NULL,
    Wind real NOT NULL)''')
    db.commit()

#Function to read and write data to and from database
    
def dbase(Temp,Humidity,Light,Wind):
    global cursor
    global db
    
    #Writing to database
    cursor.execute('''INSERT INTO Arduino(Temperature,Humidity,Light,Wind)VALUES(?,?,?,?)''',(Temp,Humidity,Light,Wind,))
    db.commit()

    #Reading from database
    cursor.execute(''' SELECT * FROM Arduino''')
    values = cursor.fetchall()[-1]#Retrives last value from databse
    print(values) #For testing
    return(values)
    
    

