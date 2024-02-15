import os
AF_DCmotor_1 motor(1)
AF_DCmotor_2 motor(2)
AF_DCmotor_3 motor(3)
AF_DCmotor_4 motor(4)

void(loop){
if(Serial.available() > 0){ 
   command = Serial.read(); 
   Stop(); //initialize with motors stoped
   
   //Serial.println(command);
   switch(command){
   case 'F':  
     forward();
     break;
   case 'B':  
      back();
     break;
   case 'L':  
     left();
     break;
   case 'R':
     right();
     break;
   }
 } 
}


void forward()
{
 motor1.setSpeed(255); //Define maximum velocity
 motor1.run(FORWARD); //rotate the motor clockwise
 motor2.setSpeed(255); //Define maximum velocity
 motor2.run(FORWARD); //rotate the motor clockwise
 
 motor3.setSpeed(255); //Define maximum velocity
 motor3.run(FORWARD); //rotate the motor clockwise
 motor4.setSpeed(255); //Define maximum velocity
 motor4.run(FORWARD); //rotate the motor clockwise
}

void back()
{
 motor1.setSpeed(255); //Define maximum velocity
 motor1.run(FORWARD); //rotate the motor clockwise
 motor2.setSpeed(255); //Define maximum velocity
 motor2.run(FORWARD); //rotate the motor clockwise
 
 motor3.setSpeed(255); //Define maximum velocity
 motor3.run(FORWARD); //rotate the motor clockwise
 motor4.setSpeed(255); //Define maximum velocity
 motor4.run(FORWARD); //rotate the motor clockwise
}

void left()
{
 motor1.setSpeed(255); //Define maximum velocity
 motor1.run(FORWARD); //rotate the motor clockwise
 motor2.setSpeed(255); //Define maximum velocity
 motor2.run(FORWARD); //rotate the motor clockwise
 
 motor3.setSpeed(255); //Define maximum velocity
 motor3.run(FORWARD); //rotate the motor clockwise
 motor4.setSpeed(255); //Define maximum velocity
 motor4.run(FORWARD); //rotate the motor clockwise
}

void right()
{
 motor1.setSpeed(255); //Define maximum velocity
 motor1.run(FORWARD); //rotate the motor clockwise
 motor2.setSpeed(255); //Define maximum velocity
 motor2.run(FORWARD); //rotate the motor clockwise
 
 motor3.setSpeed(255); //Define maximum velocity
 motor3.run(FORWARD); //rotate the motor clockwise
 motor4.setSpeed(255); //Define maximum velocity
 motor4.run(FORWARD); //rotate the motor clockwise
}

void stop()
{
 motor1.setSpeed(255); //Define maximum velocity
 motor1.run(FORWARD); //rotate the motor clockwise
 motor2.setSpeed(255); //Define maximum velocity
 motor2.run(FORWARD); //rotate the motor clockwise
 
 motor3.setSpeed(255); //Define maximum velocity
 motor3.run(FORWARD); //rotate the motor clockwise
 motor4.setSpeed(255); //Define maximum velocity
 motor4.run(FORWARD); //rotate the motor clockwise
}
