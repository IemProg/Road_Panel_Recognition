#include <LiquidCrystal.h>
#define trigPin  12  // Arduino pin tied to trigger pin on the ultrasonic sensor.
#define echoPin   11  // Arduino pin tied to echo pin on the ultrasonic sensor.
char k;
LiquidCrystal lcd(8, 9, 7, 2, 3, 4);
int cm;
int spd;
void setup() {
  pinMode(6, INPUT);
  pinMode(5,INPUT);
  Serial.begin(9600);
  lcd.begin(16,2);
}

void normalstate(){
digitalWrite(6,HIGH);
digitalWrite(5,LOW);
lcd.setCursor(0,0);
lcd.print("Welcome Board");
lcd.setCursor(0,1);
lcd.print("Speed :");    
lcd.setCursor(9,1);
lcd.print(spd);
}

void loop() {
      spd=analogRead(A0);
      normalstate();
      long duration, inches;
      pinMode(trigPin, OUTPUT);
      digitalWrite(trigPin, LOW);
      delayMicroseconds(2);
      digitalWrite(trigPin, HIGH);
      delayMicroseconds(10);
      digitalWrite(trigPin, LOW);    
      pinMode(echoPin, INPUT);
      duration = pulseIn(echoPin, HIGH);
      cm = microsecondsToCentimeters(duration);
       if (Serial.available() >0)
{ 
       k=Serial.read();
       delay(50);
       if(k=='Y' && cm<=20){
           displayDistanceYield();
           YieldGear();
          }
      else if (k=='s'){             
            displayDistanceSpeed();
            SpeedLimitGear();
            }
      else if (k=='t' && cm<= 20)   {
            displayDistanceStop();
            StopGear();
                    }
      //else{normalstate();}
 }
 }
void StopGear(){

        for (int i=60;i>=0;i--){
          analogWrite(6,i);    
          analogWrite(5,0);
          displayDistanceStop();
          }
       for (int i=0;i<=60;i++){
          analogWrite(6,i);    
          analogWrite(5,0);
          displayDistanceStop();
          }
    
}
void YieldGear(){
    digitalWrite(5,LOW);
        for (int i=100;i<=255;i++){
          analogWrite(6,i);    
          analogWrite(5,0);
          }
}

void SpeedLimitGear(){

digitalWrite(6,LOW);
analogWrite(5,0);

}
long microsecondsToCentimeters(long microseconds){
  return microseconds / 29 / 2;}
  
void displayDistanceYield(){
             lcd.setCursor(0,1);
             lcd.print("Distance:");
             lcd.setCursor(10,1);
             lcd.print(cm);            
             lcd.setCursor(0,0);
             lcd.print("Yield Sign Ahead");
             delay(100);
             lcd.clear();
             }
void displayDistanceSpeed(){
             lcd.setCursor(0,1);
             lcd.print("Speed:");
             lcd.setCursor(10,1);
             lcd.print(spd);            
             lcd.setCursor(0,0);
             lcd.print("Speed LIMIT !!");
             delay(100);
             lcd.clear();
            }
void displayDistanceStop(){
             lcd.setCursor(0,1);
             lcd.print("Distance:");
             lcd.setCursor(10,1);
             lcd.print(cm);    
             lcd.setCursor(0,0);
             lcd.print("Stop Ahead !!");
             delay(100);
             lcd.clear();
            }        
                    
  
  
