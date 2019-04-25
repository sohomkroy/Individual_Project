int vib1_l = 2;
int vib2_l = 3;
int vib3_l = 4;
int vib4_r = 5;
int vib5_r = 6;
int vib6_r = 7;
int vib7_f = 8;
int vib8_f = 9;
int vib9_f = 10;

void setup() {
  // put your setup code here, to run once:
  pinMode(vib1_l, OUTPUT); 
  pinMode(vib2_l, OUTPUT); 
  pinMode(vib3_l, OUTPUT); 
  pinMode(vib4_r, OUTPUT); 
  pinMode(vib5_r, OUTPUT); 
  pinMode(vib6_r, OUTPUT); 
  pinMode(vib7_f, OUTPUT); 
  pinMode(vib8_f, OUTPUT); 
  pinMode(vib9_f, OUTPUT);   


}

void loop() {
  // put your main code here, to run repeatedly:
  /*
  digitalWrite(2, HIGH);
  digitalWrite(3, HIGH);
  digitalWrite(4, HIGH);
  digitalWrite(5, HIGH);
  digitalWrite(6, HIGH);
  digitalWrite(7, HIGH);
  digitalWrite(8, HIGH);
  digitalWrite(9, HIGH);
  digitalWrite(10, HIGH);
  
  analogWrite(2, 255);
  analogWrite(3, 255);
  analogWrite(4, 255);
  analogWrite(5, 255);
  analogWrite(6, 255);
  analogWrite(7, 255);
  analogWrite(8, 255);
  analogWrite(9, 255);
  analogWrite(10, 255);
  */
  //vibrate_left(100);
  
  for (int x = 1; x < 765; x = x + 20) {
    vibrate_left(x);
    vibrate_right(x);
    vibrate_forward(x);
    delay(200);
  }
  
}

void vibrate_left(int power){
  if (power > 765) {
    power = 765;
  }
  if (power > 510) {
    analogWrite(vib1_l, 255);
    analogWrite(vib2_l, 255);
    analogWrite(vib3_l, power-510);
  }
  else if (power > 255) {
    analogWrite(vib1_l, 255);
    analogWrite(vib2_l, power - 255);
    analogWrite(vib3_l, 0);
  }
  else {
    analogWrite(vib1_l, power);
    analogWrite(vib2_l, 0);
    analogWrite(vib3_l, 0);
  }
}
void vibrate_right(int power){
  if (power > 765) {
    power = 765;
  }
  if (power > 510) {
    analogWrite(vib4_r, 255);
    analogWrite(vib5_r, 255);
    analogWrite(vib6_r, power-510);
  }
  else if (power > 255) {
    analogWrite(vib4_r, 255);
    analogWrite(vib5_r, power - 255);
    analogWrite(vib6_r, 0);
  }
  else {
    analogWrite(vib4_r, power);
    analogWrite(vib5_r, 0);
    analogWrite(vib6_r, 0);
  }
}
void vibrate_forward(int power){
  if (power > 765) {
    power = 765;
  }
  if (power > 510) {
    analogWrite(vib7_f, 255);
    analogWrite(vib8_f, 255);
    analogWrite(vib9_f, power-510);
  }
  else if (power > 255) {
    analogWrite(vib7_f, 255);
    analogWrite(vib8_f, power - 255);
    analogWrite(vib9_f, 0);
  }
  else {
    analogWrite(vib7_f, power);
    analogWrite(vib8_f, 0);
    analogWrite(vib9_f, 0);
  }
}
