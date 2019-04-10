#include <SFE_BMP180.h>
#include <Wire.h>


SFE_BMP180 pressure;

#define p0 101.325;

void setup()
{
  Serial.begin(9600);
  Serial.println("REBOOT");

  // Initialize the sensor (it is important to get calibration values stored on the device).

  if (pressure.begin())
    Serial.println("BMP180 init success");
  else
  {
    // Oops, something went wrong, this is usually a connection problem,
    // see the comments at the top of this sketch for the proper connections.

    Serial.println("BMP180 init fail\n\n");
    while(1); // Pause forever.
  }
}

void loop()
{
  char status;
  double T,P,p0,a;

  status = pressure.startTemperature();
  if (status != 0)
  {

    status = pressure.getTemperature(T);
    //Serial.print(status);
    if (status != 0)
    {
      // Print out the measurement:
      Serial.print("temperature: ");
      Serial.print(T,1);
      Serial.print(" deg C, ");

      status = pressure.startPressure(3);
      if (status != 0)
      {

        status = pressure.getPressure(P,T);
        if (status != 0)
        {
          // Print out the measurement:
          Serial.print("absolute pressure: ");
          Serial.print((P/10),2);
          Serial.print(" KPa, ");

          a = pressure.altitude(P,p0);
          Serial.print("Absolute altitude: ");
          Serial.print(a,1);
          Serial.print(" meters, ");
        }
        else Serial.println("error retrieving pressure measurement\n");
      }
      else Serial.println("error starting pressure measurement\n");
    }
    else Serial.println("error retrieving temperature measurement\n");
  }
  else Serial.println("error starting temperature measurement\n");

  delay(1000);  
}
