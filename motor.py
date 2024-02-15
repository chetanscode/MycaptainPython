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
