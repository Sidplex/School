#define trigPin 7
#define echoPin 6
#define motorPin 5
#define buzzer 3

int sound = 1000;

void setup()
{ 
  Serial.begin(9600);// to use the serial monitor
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(motorPin, OUTPUT);
  pinMode(buzzer,OUTPUT);
}

void loop()
{
  int duration,distance;
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  distance = (duration/2)/29.1;
  Serial.print(distance);//to print the distance on the serial monitor
  Serial.println("cm");

  // to make the motor vibrate depending on the distance
  // if the ultrasonic sensor is too far from the obstacle it will vibrate slowly
  // if the ultrasonic sensor is very close to the obstacle it will vibrate very fast

    if(distance <= 50 && distance >= 30)
    {
      // to make the motor vibrate
    digitalWrite(motorPin, HIGH); // making the motor on

    delay(200);
    digitalWrite(motorPin, LOW);// making the motor off
    delay(200);
    sound = 200;
    }
    else if(distance < 29 && distance >= 20)
    {
    digitalWrite(motorPin, HIGH);
    delay(100);
    digitalWrite(motorPin, LOW);
    delay(100);
    sound = 400;
   }
    else if(distance < 19 && distance >= 10)
    {
    
    digitalWrite(motorPin, HIGH);
    delay(100);
    digitalWrite(motorPin, LOW);
    delay(100);
    sound = 600;
   }

    else if(distance < 9 && distance >= 1)
    {
    
    digitalWrite(motorPin, HIGH);
    delay(100);
    digitalWrite(motorPin, LOW);
    delay(100);
    sound = 800;
   }
    else if(distance < 0){

   
    digitalWrite(motorPin, HIGH);
    delay(50);
    digitalWrite(motorPin, LOW);
    delay(50); 
    sound=1000;
  } 
  else 
  {
    digitalWrite(motorPin, LOW);
  }
}

