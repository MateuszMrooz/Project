#include <Arduino.h>
#include <DHT.h>
DHT DHT11_Sensor(11,DHT11); //11 is a digital pin number which I'm using, can be replaced with the number of the pin being used, DHT11 is the sensor type


//Variables here with the necessary datatype
float Light;
float Temp;
float Humidity;
float Wind;
int LED_data = 0; // For writing to the LEDs
float Start_time;
float Current_time;

void setup() {
  Serial.begin(9600); // Initialize serial communication
  DHT11_Sensor.begin();
  delay(2000);// Wait 2 seconds after starting
  pinMode(7, OUTPUT);// Sets the digital pins as output for LEDs
  pinMode(6, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(4, OUTPUT);
  Start_time = millis();  //Initial start time
  }

void loop() {//Main loop which sends data to Thonny and controls LEDs
Light = analogRead(A2); // Read the analog input for whichever pin the sensors outputs are connected to. In this case I used A2 and A5
Wind = analogRead(A5);
Temp = DHT11_Sensor.readTemperature(false);//Read DHT temperature and humidity, false means degrees C true means degrees F
Humidity = DHT11_Sensor.readHumidity();

Current_time = millis();
if (Current_time - Start_time > 2000) //Small time delay to avoid breaking DHT11 sensor

{
Serial.print(" Temperature: ");
Serial.print(Temp);
Serial.print(" Humidity: ");
Serial.print(Humidity);
Serial.print(" Light_intensity: ");
Serial.print(Light);
Serial.print(" Wind: ");
Serial.println(Wind/20); //Dividing by 20 gives the windspeed a more realisic value
Start_time = millis(); 
}

  if (Serial.available() > 0) {
    // read the incoming byte as LED_data:
    LED_data = Serial.read();
  }
    if (LED_data == 49){//49 is ASCII for 1 which corresponds to the serial write code in Thonny in the Risk file (Risk_level function)
      digitalWrite(7,LOW);
      digitalWrite(6,LOW);
      digitalWrite(5,LOW);//Resets all of the LEDs
      digitalWrite(4,LOW);
      digitalWrite(7,HIGH);//LED on, 7 represtents digital pin 7 which is what one of my LEDs in connected to
      delay(500);//Delay to make LED blink
      digitalWrite(7,LOW);//LED off to complete blink
      delay(500);
      digitalWrite(7,HIGH);//Stays on and repeats due to being in a loop until new data is sent from lines 39-47(every 2 seconds)
    }
  
    if (LED_data == 50){
      digitalWrite(7,LOW);
      digitalWrite(6,LOW);
      digitalWrite(5,LOW);
      digitalWrite(4,LOW);
      digitalWrite(7,HIGH);//Keeps LED on constantly
    }

    if (LED_data == 51){//All of these if statements do the same for all of the other LEDs with a odd number being a constant on and an even being a flashing LED
      digitalWrite(7,LOW);
      digitalWrite(6,LOW);
      digitalWrite(5,LOW);
      digitalWrite(4,LOW);
      digitalWrite(7,HIGH);
      digitalWrite(6,HIGH);
      delay(500);
      digitalWrite(6,LOW);
      delay(500);
      digitalWrite(6,HIGH);
    }

    if (LED_data == 52){
      digitalWrite(7,LOW);
      digitalWrite(6,LOW);
      digitalWrite(5,LOW);
      digitalWrite(4,LOW);
      digitalWrite(7,HIGH);
      digitalWrite(6,HIGH);
    }
    
    if (LED_data == 53){
      digitalWrite(7,LOW);
      digitalWrite(6,LOW);
      digitalWrite(5,LOW);
      digitalWrite(4,LOW);
      digitalWrite(5,HIGH);
      digitalWrite(6,HIGH);
      digitalWrite(7,HIGH);
      delay(500);
      digitalWrite(5,LOW);
      delay(500);
      digitalWrite(5,HIGH);
    }
    
    if (LED_data == 54){
      digitalWrite(7,LOW);
      digitalWrite(6,LOW);
      digitalWrite(5,LOW);
      digitalWrite(4,LOW);
      digitalWrite(5,HIGH);
      digitalWrite(6,HIGH);
      digitalWrite(7,HIGH);
    }

    if (LED_data == 55){
      digitalWrite(7,LOW);
      digitalWrite(6,LOW);
      digitalWrite(5,LOW);
      digitalWrite(4,LOW);
      digitalWrite(4,HIGH);
      delay(500);
      digitalWrite(4,LOW);
      delay(500);
      digitalWrite(4,HIGH);
    }

    if (LED_data == 56){
      digitalWrite(7,LOW);
      digitalWrite(6,LOW);
      digitalWrite(5,LOW);
      digitalWrite(4,LOW);
      digitalWrite(4,HIGH);

    }
    
    

  
}
