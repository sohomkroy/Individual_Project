#include "Adafruit_VL53L0X.h"

Adafruit_VL53L0X left_lox = Adafruit_VL53L0X();
Adafruit_VL53L0X right_lox = Adafruit_VL53L0X();
Adafruit_VL53L0X forward_lox = Adafruit_VL53L0X();
int left = 11;
int right = 13;
int forward = 12; 
  


void setup() {
  // put your setup code here, to run once:

  pinMode(left, OUTPUT);
  pinMode(right, OUTPUT); 
  pinMode(forward, OUTPUT); 

  Serial.begin(115200);

  // wait until serial port opens for native USB devices
  while (! Serial) {
    delay(1);
  }

  digitalWrite(left, LOW);
  digitalWrite(right, LOW);
  digitalWrite(forward, LOW);

  delay(100);

  digitalWrite(left, HIGH);
  digitalWrite(right, HIGH);
  digitalWrite(forward, HIGH);

  delay(100);

  digitalWrite(right, LOW);
  digitalWrite(forward, LOW);

  delay(10);

  left_lox.begin(0x31);
  left_lox.setAddress(0x31);

  delay(100);

  digitalWrite(right, HIGH);
  digitalWrite(forward, LOW);
  
  delay(100);

  right_lox.begin(0x33);
  right_lox.setAddress(0x33);
  
  delay(100);

  digitalWrite(forward, HIGH);
  
  delay(100);

  forward_lox.begin(0x35);
  forward_lox.setAddress(0x35);

  delay(100);
  
  
  Serial.println("Adafruit VL53L0X test");

}

void loop() {
  // put your main code here, to run repeatedly:
  VL53L0X_RangingMeasurementData_t left_measure;
  VL53L0X_RangingMeasurementData_t right_measure;
  VL53L0X_RangingMeasurementData_t forward_measure;
    
  //Serial.print("Reading a measurement... ");
  left_lox.rangingTest(&left_measure, false); // pass in 'true' to get debug data printout!
  delay(100);
  right_lox.rangingTest(&right_measure, false); // pass in 'true' to get debug data printout!
  delay(100);
  forward_lox.rangingTest(&forward_measure, false); // pass in 'true' to get debug data printout!
  delay(100);

  

  if (right_measure.RangeStatus != 4) {  // phase failures have incorrect data
    Serial.print("Distance Right (mm): "); Serial.println(right_measure.RangeMilliMeter);
  } else {
    Serial.println(" out of range ");
  }

  if (left_measure.RangeStatus != 4) {  // phase failures have incorrect data
    Serial.print("Distance Left (mm): "); Serial.println(left_measure.RangeMilliMeter);
  } else {
    Serial.println(" out of range ");
  }

  if (forward_measure.RangeStatus != 4) {  // phase failures have incorrect data
    Serial.print("Distance Forward (mm): "); Serial.println(forward_measure.RangeMilliMeter);
  } else {
    Serial.println(" out of range ");
  }

  
    
  delay(100);

}
