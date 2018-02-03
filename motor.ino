#include<NewPing.h>

#define trigPin  12  // Arduino pin tied to trigger pin on the ultrasonic sensor.
#define echoPin   11  // Arduino pin tied to echo pin on the ultrasonic sensor.
char k;
void setup() {
  pinMode(6, INPUT);
  pinMode(5,INPUT);
  Serial.begin(9600);
}
void loop(){
  long duration, inches, cm;
  pinMode(trigPin, OUTPUT);
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  pinMode(echoPin, INPUT);
  duration = pulseIn(echoPin, HIGH);
  cm = microsecondsToCentimeters(duration);
  delay(100);

 if (cm <= 20){
    Serial.println("j");}
 else {
    Serial.println("z");}
 if (Serial.available()){
    k=Serial.read();
    if (k=='s'){
      digitalWrite(8,HIGH);
    }else{    
      digitalWrite(8,LOW);
      }
    }  
    
 
/*  digitalWrite(6,HIGH);
  digitalWrite(5,LOW);
  delay(2000);
 if (Serial.available())
    {
      k=Serial.parseInt();
      if (k == 's')
      {
        StopGear();
    digitalWrite(8,HIGH);    
  }
      
      if (k == 'y'){
      YieldGear();
      }
      if (k =='w'){
      SpeedLimitGear();
      }
      }
  */ 
 }
void StopGear(){
    digitalWrite(6,LOW);
    digitalWrite(5,HIGH);
    delay(250);
    digitalWrite(6,LOW);
    digitalWrite(5,LOW);  
}
void YieldGear()
{
    analogWrite(6,30);
    analogWrite(5,0);
    delay(1000);
    analogWrite(6,255);
    analogWrite(5,0);
}
void SpeedLimitGear(){
  analogWrite(6,100);
  analogWrite(5,0);
  delay(1000);
}
long microsecondsToCentimeters(long microseconds){
  return microseconds / 29 / 2;
}
