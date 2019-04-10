#include <SD.h>
#include <SPI.h>
#include <TimedAction.h>
#include "MPU9250.h"
#include <SFE_BMP180.h>
#include <Wire.h>
SFE_BMP180 pressure;

#define p0 101.325
File myFile;
File myfile1;
MPU9250 IMU(Wire,0x68);
int pinCS = 10; // Pin 10 on Arduino Uno
int irpin=8;
int status;
double count=0;
SFE_BMP180 pressure;

#define p0 101.325  
void mpu1()
{
IMU.readSensor();
  // display the data
  char s;
  double T,P,p0,a;
  Serial.print(IMU.getAccelX_mss(),6);
  Serial.print("\t");
  Serial.print(IMU.getAccelY_mss(),6);
  Serial.print("\t");
  Serial.print(IMU.getAccelZ_mss(),6);
  Serial.print("\t");
  Serial.print(IMU.getGyroX_rads(),6);
  Serial.print("\t");
  Serial.print(IMU.getGyroY_rads(),6);
  Serial.print("\t");
  Serial.print(IMU.getGyroZ_rads(),6);
  Serial.print("\t");
  Serial.print(IMU.getMagX_uT(),6);
  Serial.print("\t");
  Serial.print(IMU.getMagY_uT(),6);
  Serial.print("\t");
  Serial.print(IMU.getMagZ_uT(),6);
  Serial.print("\t");
  Serial.println(IMU.getTemperature_C(),6);
  myFile = SD.open("test.txt", FILE_WRITE);
  if (myFile) {    
        myFile.print(int(IMU.getAccelX_mss()));
        myFile.print(",");    
        myFile.println(int(IMU.getAccelY_mss()));
        myFile.print(",");
        myFile.println(int(IMU.getAccelZ_mss()));
        myFile.print(",");
//        myFile.println(int(IMU.getGyroX_rads()));
//        myFile.print(",");
//        myFile.println(int(IMU.getGyroY_rads()));
//        myFile.print(",");
//        myFile.println(int(IMU.getGyroZ_rads()));
//        myFile.print(",");
//        myFile.println(int(IMU.getMagX_uT()));
//        myFile.print(",");
//          myFile.println(int(IMU.getMagY_uT()));
//         myFile.print(",");
//         myFile.println(int(IMU.getMagZ_uT()));
//         myFile.print(",");
        if (status != 0)
  {
     s = pressure.getTemperature(T);
     if (s != 0)
     {
      // Print out the measurement:
     // myFile.print("temperature: ");
      myFile.print(int(T));
      myFile.print(" , ");

      s = pressure.startPressure(3);
      if (s != 0)
      {

        s = pressure.getPressure(P,T);
        if (s != 0)
        {
          // Print out the measurement:
         // Serial.print("absolute pressure: ");
          myFile.print(int((P/10)));
         myFile.print(" , ");

          a = pressure.altitude(P,p0);
         // Serial.print("Absolute altitude: ");
          myFile.print(int(a));
          myFile.print(" , ");
        }
        else Serial.println("error retrieving pressure measurement\n");
      }
      else Serial.println("error starting pressure measurement\n");
    }
    else Serial.println("error retrieving temperature measurement\n");
  }
         
         
      myFile.close(); // close the file  
      }
      else {
        Serial.println("error opening test.txt");
      }
      
}
void ir1()
{
  while(1)
  {
    if(irpin==HIGH)
    {
      count++;
    }
     myFile1.println(count);
         myFile1.print(",");
  }
}
TimedAction numberThread = TimedAction(1000,mpu1);
TimedAction textThread = TimedAction(1,ir1);
void setup() {
  // serial to display data
  Serial.begin(115200);
  // Serial.begin(9600);
      pinMode(pinCS, OUTPUT);
      
      // SD Card Initialization
      if (SD.begin())
      {
        Serial.println("SD card is ready to use.");
      } else
      {
        Serial.println("SD card initialization failed");
        return;
      }
       if (pressure.begin())
    Serial.println("BMP180 init success");
  else
  {
    // Oops, something went wrong, this is usually a connection problem,
    // see the comments at the top of this sketch for the proper connections.

    Serial.println("BMP180 init fail\n\n");
    while(1); // Pause forever.
  }
  while(!Serial) {}

  // start communication with IMU 
  status = IMU.begin();
  if (status < 0) {
    Serial.println("IMU initialization unsuccessful");
    Serial.println("Check IMU wiring or try cycling power");
    Serial.print("Status: ");
    Serial.println(status);
    while(1) {}
  }
  
}

void loop() {
           numberThread.check();
          textThread.check();
      
      
  delay(1000);
}


//Loop not touched for bmp
