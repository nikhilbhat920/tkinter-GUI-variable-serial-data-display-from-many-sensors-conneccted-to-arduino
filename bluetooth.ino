 
void setup()
{
  Serial.begin(9600);
  pinMode(13, OUTPUT);
}

unsigned long long timer = 0;
void loop()
{
  
  if (millis() - timer > 2000)
  {
    
      Serial.print("3333.323 7");
      delay(2000); 
      Serial.print("6666.676 8");
      delay(2000); 
     
      Serial.print("3000.323 7");
      delay(2000); 
      Serial.print("6000.676 8");
      
    timer = millis();  
   }
   

}
